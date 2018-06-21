# DB-410C-spidev

Communication between DB-410C as a master with ARDUINO Mega as a slave device

## Installation
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install spidev
```

## Enabling SPI on Dragonboard 410c with SPIDEV
This driver can be enabled by the following Kconfig option:
```
CONFIG_SPI_SPIDEV=y (or) CONFIG_SPI_SPIDEV=m
```
## Modifying device tree
```
git clone https://github.com/96boards/dt-update
cd dt-update
make
sudo scripts/db410c/enable-spidev.sh
sudo reboot now
```
## Wiring

| DB410C        | ARDUINO MEGA |
|---------------|--------------|
| CLK(8)        | SCK          |
| MISO(10)      | MISO         |  
| CS(12)        | SS           |
| MOSI(14)      | MOSI         |

### NOTE: Use 8-bit Bidirectional Voltage-Level Translator
[Datasheet](https://cdn-shop.adafruit.com/datasheets/txb0108.pdf)

## Download & Run Code
```
git clone https://github.com/alokm014/DB-410C-spidev.git
cd DB-410C-spidev
sudo python spidev.py
```

## Project Details

- **Creator:** ALOK MISHRA
- **Project Name:** DB-410C-spidev
- **Type of Project:** Demonstration
- **Project Category:** spi
- **Board(s) used:** DragonBoard 410c
- **Difficulty level:** Beginner

## Resources

### RSS URL
- [GitHUb Repository](https://github.com/alokm014/DB-410C-spidev)
- [Enable SPI](https://www.96boards.org/documentation/consumer/dragonboard410c/guides/enable-spi.md.html)

### Social Media Link

ALOK MISHRA: [Website](http://robopathshala.66ghz.com/) | [Linkedin](https://www.linkedin.com/in/alok-mishra-23055a74/) | [Facebook](https://www.facebook.com/alokmishra.mishra3) | [YouTube](https://www.youtube.com/channel/UCNOHaiZpf-HhyazeYqTeXvA) | [iceUp](http://iceup.in/)

***
