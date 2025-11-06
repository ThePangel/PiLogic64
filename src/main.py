from machine import Pin, SPI
from machine import I2C
from ssd1306 import SSD1306_I2C
import neopixel
import time
import os, sdcard

REC1_A = 12
REC1_B = 12
REC1_SW = 13

REC2_A = 7
REC2_B = 6
REC2_SW = 8

AUD_R = 14
AUD_L = 15

MATX = 22

DSP_SDA = 20
DSP_SCL = 21

SD_CS = 1
SD_MOSI = 3
SD_CLK = 2
SD_MISO = 4

clk1 = Pin(REC1_A, Pin.IN, Pin.PULL_UP)
dt1 = Pin(REC1_B, Pin.IN, Pin.PULL_UP)
sw1 = Pin(REC1_SW, Pin.IN, Pin.PULL_UP)

clk2 = Pin(REC2_A, Pin.IN, Pin.PULL_UP)
dt2 = Pin(REC2_B, Pin.IN, Pin.PULL_UP)
sw2 = Pin(REC2_SW, Pin.IN, Pin.PULL_UP)

built_games = ["Mastermind", "Snake", "Sudoku"]
game_idx = 0

matrix = neopixel.NeoPixel(Pin(MATX), 64)
matrix.write()

dsp = I2C(0, scl=Pin(DSP_SCL), sda=Pin(DSP_SDA))
oled = SSD1306_I2C(128, 64, dsp)

card = spi = SPI(0,
          baudrate=1_000_000,  
          polarity=0,
          phase=0,
          bits=8,
          firstbit=SPI.MSB,
          sck=Pin(SD_CLK),
          mosi=Pin(SD_MOSI),
          miso=Pin(SD_MISO))

sd = sdcard.SDCard(card, Pin(SD_CS))

os.mount(sd, "/")

oled.fill(0)

oled.text("Initializing...",4 , 32)
                   
oled.show()

time.sleep(0.5)

last_step1 = clk1.value()
last_step2 = clk2.value()
print(len(built_games) - 1)
while True:
    clk_now = clk1.value()
    dt_now = dt1.value()

    if clk_now == 1 and last_step1 == 0:  
        if dt_now != clk_now:
            game_idx = (game_idx + 1) % len(built_games)
        else:
            game_idx = (game_idx - 1) % len(built_games)
    last_step1 = clk_now


    clk2_now = clk2.value()
    dt2_now = dt2.value()

    if clk2_now == 1 and last_step2 == 0:  
        if dt2_now != clk2_now:
            game_idx = (game_idx + 1) % len(built_games)
        else:
            game_idx = (game_idx - 1) % len(built_games)
    last_step2 = clk2_now
    
    oled.fill(0)
    prev_idx = (game_idx - 1) % len(built_games)
    next_idx = (game_idx + 1) % len(built_games)

    oled.text(built_games[prev_idx], (128 - len(built_games[prev_idx]) * 8) // 2, 8)
    oled.text(built_games[game_idx], (128 - len(built_games[game_idx]) * 8) // 2, 32)
    oled.text(built_games[next_idx], (128 - len(built_games[next_idx]) * 8) // 2, 56)
    oled.show()
    
    last_step1 = current_step1
    last_step2 = current_step2
