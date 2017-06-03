# oh-my-earth

Put near-realtime picture of Earth as your Wallpaper
----------------------------------------------------

- oh-my-earth is a Python 2.7 Script that fetches near-realtime picture of Earth as your Wallpaper
- The picture is taken by [Himawari 8 (向日葵8号)](https://en.wikipedia.org/wiki/Himawari_8)
- The web site of [Himawari 8](http://himawari8.nict.go.jp/)

**oh-my-earth** differs in that:

* It doesn't install python3 and extra python packages, python2.7 is enough and is default version for most OS
* The installation procedure is simplify
* More easier to customization by yourself


## Example

![Picture 1. oh-my-earth Wallpaper Example 3](https://github.com/ujnzxw/picture/blob/master/oh-my-earth-example-3.png)
![Picture 4. oh-my-earth Wallpaper Example 4](https://github.com/ujnzxw/picture/blob/master/oh-my-earth-example-4.png)
![Picture 2. oh-my-earth Wallpaper Example 2](https://github.com/ujnzxw/picture/blob/master/oh-my-earth-example-2.png)

##Supported Desktop Environments

Tested
-----
* Unity 7
* Mate 1.8.1
* Pantheon
* LXDE
* OS X

Not Tested
----------
* GNOME 3
* KDE

## Configuration
You can configure the level of detail, by modifying the script. You can set the global variable `level` to `4`, `8`, `16`, or `20` to increase the quality (and thus the file size as well). Please keep in mind that it will also take more time to download the tiles.


### xfce4

On xfce4, you can set which displays you want to change the background of using the xfce displays variable. If you get an error and you're not sure which display to use, you can find your display in the output of:

    xfconf-query --channel xfce4-desktop --list | grep last-image

### Nitrogen
  If you use nitrogen for setting your wallpaper, you have to enter this in your `~/.config/nitrogen/bg-saved.cfg`.

    [:0.0]
    file=/home/USERNAME/.cache/ujnzxw/latest.png
    mode=4
    bgcolor=#000000



## Installation


#### Pre-install
[Please install PIL package first](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00140767171357714f87a053a824ffd811d98a83b58ec13000)

Others:

sudo easy_install image
sudo easy_install pytz
sudo easy_install tzlocal
sudo easy_install appdirs

```
cd ~  <OR OTHER PATH YOU WANT>
git clone https://github.com/ujnzxw/oh-my-earth.git

# Configure
cd ~/oh-my-earth/
vi config.py

# Install
sudo bash install.sh

# Test whether it's working
oh-my-earth

# Set oh-my-earth to be called periodically

- Set up a cronjob
crontab -e

- Add the line:
 */10 * * * * <INSTALLATION_PATH>
```
## Uninstallation
```
# Remove the cronjob
crontab -e
# Remove the line
*/10 * * * * <INSTALLATION_PATH>

# Remove the data directory
 rm -rf ~/oh-my-earth  <OR OTHER PATH YOU INSTALLED>

# Remove the soft link
rm -rf /usr/local/bin/oh-my-earth
```

## Reference

[boramalper/himawaripy](https://github.com/boramalper/himawaripy)

[PIL Download](http://www.pythonware.com/products/pil/index.htm)

[PIL HandBook](http://effbot.org/imagingbook/)

---
[MIT License](LICENSE.md) © 2017 Steven ZHAO
