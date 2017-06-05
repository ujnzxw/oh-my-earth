#-*- coding: utf-8 -*-
'''
@author ujnzxw <ujnzxw@gmail.com>
'''
import os.path
import appdirs

'''
Global settings
'''

''' set display model: random, earth, momentumdash'''
display_model = "momentumdash"

''' get the output file '''
# earth output file
earth_output_file = os.path.join(appdirs.user_cache_dir(appname="oh-my-earth",
                                                  appauthor=False),
                           "earth.latest.png")
# bing.com output file
bing_output_file = os.path.join(appdirs.user_cache_dir(appname="oh-my-earth",
                                                  appauthor=False),
                           "bing.random.jpg")

# momentumdash.com output file
momentumdash_output_file = os.path.join(appdirs.user_cache_dir(appname="oh-my-earth",
                                                  appauthor=False),
                           "momentumdash.random.jpg")


''' Xfce4 displays to change the background of '''
xfce_displays = ["/backdrop/screen0/monitor0/image-path",
                 "/backdrop/screen0/monitor0/workspace0/last-image"]

'''
Earth images settings
'''

'''
Increases the quality and the size. Possible values: 4, 8, 16, 20
'''
level = 8

'''
Define a hourly offset or let the script calculate it depending on your timezone

If auto_offset is True, then script will calculate your hour offset
automatically depending on your location.

If hour_offset is greater than 0, then script will use it.
If both of the variables are set different than their default values below,
then script will raise an error. Here, using the default values, script will
put the realtime picture of Earth.
'''
auto_offset = True
hour_offset = 0

