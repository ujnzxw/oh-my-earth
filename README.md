# oh-my-earth
*Put near-realtime picture of Earth as your desktop background*

This is a python 2.7 version of [boramalper/himawaripy](https://github.com/boramalper/himawaripy)

## Installation

    cd ~  <OR OTHER PATH YOU WANT>
    git clone https://github.com/ujnzxw/oh-my-earth.git

    # configure
    cd ~/oh-my-earth/
    vi config.py

    # install
    sudo bash install.sh

    # test whether it's working
    oh-my-earth

    # Set oh-my-earth to be called periodically

        ## Either set up a cronjob
            crontab -e

            ### Add the line:
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
