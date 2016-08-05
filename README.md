# oh-my-earth

*Put near-realtime picture of Earth as your Wallpaper*

**oh-my-earth** differs in that:

* It doesn't install python3 and extra python packages, python2.7 is enough
* The installation procedure is simplify
* More easier to customization by yourself


## Example

![Picture 1. oh-my-earth Wallpaper Example 1](https://github.com/ujnzxw/picture/blob/master/oh-my-earth-example-1.png)
![Picture 2. oh-my-earth Wallpaper Example 2](https://github.com/ujnzxw/picture/blob/master/oh-my-earth-example-2.png)

## Installation

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

## Uninstallation
    # Remove the cronjob
    crontab -e
    # Remove the line
    */10 * * * * <INSTALLATION_PATH>

    # Remove the data directory
     rm -rf ~/oh-my-earth  <OR OTHER PATH YOU INSTALLED>

    # Remove the soft link
    rm -rf /usr/local/bin/oh-my-earth

## Attributions
This Script come from the python3 version:
[boramalper/himawaripy](https://github.com/boramalper/himawaripy)

---
[MIT License](LICENSE)
