# PiLogic64 🎮✨

> An open-source logic puzzle console 
## What is this?

**PiLogic64** is a handheld logic puzzle gaming console powered by a Raspberry Pi Pico. This project brings interactive logic puzzles and games to makers everywhere—at a fraction of the cost and with infinite customizability.

### Features 🚀

- **8x8 NeoPixel Matrix Display** - Bright, colorful LED matrix for puzzle visualization
- **OLED Screen** - Navigate menus and game selection with ease
- **Dual Rotary Encoders** - Intuitive controller input for puzzle solving
- **Audio Output** - Up to dual speakers for satisfying sound effects and feedback
- **SD Card Support** - Easily add new puzzles and games by dropping files on an SD card
- **Rechargeable Power** - 2 18650 Li-ion battery with TP4056 charging circuit and MT3608 buck converter for stable 5V power
- **100% Open Source** - PCB designs, schematics, and code available for the community

### Tech Specs 🔧

- **Microcontroller**: Raspberry Pi Pico (or Pico 2)
- **Display**: 8x8 NeoPixel Matrix + OLED
- **Power**: 2 18650 cells (3.7V) → TP4056 charger → MT3608 boost to 5V
- **Audio**: PAM8403 amplifier
- **Input**: 2x Rotary Encoders
- **Storage**: SD Card slot

## Game Examples 🎯

Here are some games I have thought for the PiLogic64!
(Some I will code myself, but feel free to make any of these!)

### Logic Puzzles
- **Mastermind** - Crack the color code using logic and deduction
- **Color Sudoku** - 8x8 Sudoku with colored LEDs instead of numbers
- **Lights Out** - Toggle lights to turn them all off in a cascading puzzle
- **Pattern Memory** - Simon-style memory game with increasing sequences
- **Minesweeper** - Classic logic game adapted for the LED matrix

### Action Games
- **Snake** - Classic snake game with colorful trails
- **Tetris Mini** - Block-stacking puzzle on a compact grid

### Creative Puzzles

- **Color Match** - Pattern matching and replication challenges
- **Logic Gates** - Educational puzzles teaching boolean logic

*...and infinitely more! Just code and drop new game files on the SD card.*

## Development Journey 📔

This project is being documented on [Hack Club Blueprint](https://blueprint.hackclub.com/projects/380). Check it out for detailed build logs, photos, and the full story!

## Credit
-   Footprints
    - [MT3608](https://github.com/kubabuda/misc_footprints/)
    -   [TP4056](https://github.com/ccadic/TP4056-18650) (I did modify this one)
    -   [PAM8403](https://github.com/johnnycubides/pam8403-module-kicad-lib/tree/main) (I did modify this one)
    -   [BK-18650-PC4](https://www.snapeda.com/parts/BK-18650-PC4/Memory%20Protection%20Devices/view-part/?p=BK-18650-PC2&welcome=home&ref=mpd_rel&t=None)