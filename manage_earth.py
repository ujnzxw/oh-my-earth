#!/usr/bin/env python

#-*- coding: utf-8 -*-
'''
Created on Jun 03, 2017

@author ujnzxw <ujnzxw@gmail.com>
'''

import os, urllib, urllib2
import multiprocessing

from datetime  import datetime, timedelta
from io        import BytesIO
from itertools import product
from json      import loads
from time      import strptime, strftime, mktime
from PIL       import Image
from pytz      import timezone
from tzlocal   import get_localzone
from config    import level, output_file, auto_offset, hour_offset
from utils     import set_background, get_desktop_environment

counter = None
height  = 550
width   = 550

def download_chunk(args):
    '''
    download a picture section from website
    x      - coordinate x
    y      - coordinate y
    latest - requested time
    '''

    global counter
    x, y, latest = args
    url_format = "http://himawari8.nict.go.jp/img/D531106/{}d/{}/{}_{}_{}.png"
    url        = url_format.format(level,
                                   width,
                                   strftime("%Y/%m/%d/%H%M%S", latest), x, y)
    tile_w   = urllib2.urlopen(url)
    tiledata = tile_w.read()

    with counter.get_lock():
        counter.value += 1
        print("\rDownloading tiles: %s/%s completed" % (counter.value, level * level))
    return x, y, tiledata

class EarthManager():
    '''
    Earth Picture Manager
    '''
    def __init__(self):
        pass
    def get_time_offset(self, latest_date):
        '''
        get time offset based on auto_offset or hour_offset
        '''
        if auto_offset is not None:
            local_date    = datetime.now(timezone(str(get_localzone())))
            himawari_date = datetime.now(timezone('Asia/Shanghai'))
            local_offset  = local_date.strftime("%z")
            himawari_offset = himawari_date.strftime("%z")

            offset = int(local_offset) - int(himawari_offset)
            offset /= 100

            offset_tmp  = datetime.fromtimestamp(mktime(latest_date))
            offset_tmp += timedelta(hours=offset)
            offset_time = offset_tmp.timetuple()

        elif hour_offset > 0:
            offset_tmp  = datetime.fromtimestamp(mktime(latest_date))
            offset_tmp -= timedelta(hours=hour_offset)
            offset_time = offset_tmp.timetuple()

        return offset_time


    def run(self):
        '''
        main function
        '''

        global counter

        ''' check if setting data is correct or not '''
        if auto_offset and hour_offset:
            exit("You can not set `auto_offset` to True and `hour_offset` to a value that is different than zero.")
        elif hour_offset < 0:
            exit("`hour_offset` must be greater than or equal to zero. I can't get future images of Earth for now.")

        ''' start to download picture '''

        print("Updating...")

        ''' get latest updating time '''
        url = 'http://himawari8-dl.nict.go.jp/himawari8/img/D531106/latest.json'
        latest_json=None
        try:
            latest_json =  urllib2.urlopen(url)
        except urllib2.URLError:
            print('ERROR: Site himawari8-dl.nict.go.jp cannot be reached')

        latest = strptime(loads(latest_json.read().decode("utf-8"))["date"], "%Y-%m-%d %H:%M:%S")

        print("Latest version: {} GMT".format(strftime("%Y/%m/%d %H:%M:%S", latest)))

        if auto_offset or hour_offset > 0:
            requested_time = self.get_time_offset(latest)

            print("Offset version: {} GMT".format(strftime("%Y/%m/%d %H:%M:%S", requested_time)))
        else:
            requested_time = latest

        print

        ''' use Python Imaging Library (PIL) to generate png '''
        png = Image.new('RGB', (width * level, height * level))

        counter = multiprocessing.Value("i", 0)
        p = multiprocessing.Pool(multiprocessing.cpu_count() * level)

        print("Downloading tiles: 0/%s completed" % (level * level))

        res = p.map(download_chunk, product(range(level), range(level), (requested_time,)))

        for (x, y, tiledata) in res:
            tile = Image.open(BytesIO(tiledata))
            png.paste(tile, (width * x, height * y, width * (x + 1), height * (y + 1)))

        print("\nSaving to '%s'..." % (output_file))
        if not os.path.exists(os.path.dirname(output_file)):
            os.makedirs(os.path.dirname(output_file))
        png.save(output_file, "PNG")

        if not set_background(output_file):
            exit("Your desktop environment '{}' is not supported.".format(get_desktop_environment()))

        print("Done!")

if __name__ == "__main__":
    earth = EarthManager()
    earth.run()
