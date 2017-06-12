#!/usr/bin/env python

#-*- coding: utf-8 -*-
'''
Created on Jun 04, 2017

@author ujnzxw <ujnzxw@gmail.com>
'''

import urllib,re,sys,os,random,json
from   config    import momentumdash_output_file
from   utils     import set_background, get_desktop_environment

class MomentumdashManager():
    '''
    momentumdash.com background image manager
    '''

    def __init__(self):
        pass

    def get_bg_picture(self):
        '''
        get background picture from https://momentumdash.com
        '''

        '''
        background image json file:

        https://momentumdash.com/app/backgrounds.json
        '''
        index     = random.randint(0,13)
        json_url  = "https://momentumdash.com/app/backgrounds.json"
        response  = urllib.urlopen(json_url)
        json_data = json.loads(response.read())
        filename  = json_data['backgrounds'][index]['filename']

        imgurl = 'https://momentumdash.com/backgrounds/' + filename
        urllib.urlretrieve(imgurl, momentumdash_output_file)

    def run(self):
        ''' main function '''

        ''' get background picture from momentumdash.com '''

        print("Updating momentumdash image...")

        self.get_bg_picture()

        print("\nSaving to '%s'..." % (momentumdash_output_file))

        ''' set background picture as wallpaper '''
        ''' scaled, wallpaper, stretched, spanned '''
        if not set_background(momentumdash_output_file, "stretched"):
            exit("Your desktop environment '{}' is not supported.".format(get_desktop_environment()))

        print("Done!")

if __name__ == "__main__":
    b = MomentumdashManager()
    b.run()
