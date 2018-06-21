# DB-410C-spidev

Communication between DB-410C as a master with ARDUINO Mega as a slave device

## Installation
'''
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install spidev
sudo apt-get install libmraa-dev
'''

## Enabling SPI on Dragonboard 410c with SPIDEV
This driver can be enabled by the following Kconfig option:
'''
CONFIG_SPI_SPIDEV=y (or) CONFIG_SPI_SPIDEV=m
'''
## Modifying device tree
'''
git clone https://github.com/96boards/dt-update
cd dt-update
make
sudo scripts/db410c/enable-spidev.sh
sudo reboot now
'''

## Project Details

- **Creator:** ALOK MISHRA
- **Project Name:** DB-410C-spidev
- **Type of Project:** Demonstration
- **Project Category:** spi
- **Board(s) used:** DragonBoard 410c
- **Difficulty level:** Beginner

## Videos

< Link to YouTube video >

## Resources

### RSS URL

< Provide URL to any source instructions/code >

### Social Media Link

ALOK MISHRA: [Website](http://robopathshala.66ghz.com/) | [Linkedin](https://www.linkedin.com/in/alok-mishra-23055a74/) | [Facebook](https://www.facebook.com/alokmishra.mishra3) | [YouTube](https://www.youtube.com/channel/UCNOHaiZpf-HhyazeYqTeXvA) | [iceUp](http://iceup.in/)

***
