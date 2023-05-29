# PyHop

This repository contains a Python script that enables bunny hopping in Counter-Strike: Global Offensive (CS:GO) using memory manipulation techniques. Bunny hopping is a movement technique where players repeatedly jump to maintain or gain speed.

## Features

- Automatic bunny hopping in CS:GO
- Customizable key binding
- Configuration file for easy customization

## Disclaimer

Using this script for memory manipulation in CS:GO may violate the game's terms of service and result in penalties or bans. Use it responsibly at your own risk.

## Requirements

- Python 3.x
- `pymem` library: Install using `pip install pymem`
- `pywin32` library: Install using `pip install pywin32`

## Usage

1. Ensure that CS:GO is running.
2. Install the required Python libraries mentioned above.
3. Customize the script's behavior by editing the `config.ini` file.
4. Run the script using the command `python bhop.py`.
5. In CS:GO, press the specified bind key (default: spacebar) to enable bunny hopping.
6. Enjoy bunny hopping in the game!

## Configuration

The `config.ini` file contains the following customizable values:

- `LOCAL_PLAYER`: The offset value used to locate the local player object in memory.
- `FORCE_JUMP`: The offset value used to locate the force jump variable in memory.
- `HEALTH`: The offset value used to locate the health variable in memory.
- `FLAGS`: The offset value used to locate the flags variable in memory.
- `BIND_KEY`: The key code for the key that triggers bunny hopping (default: 0x20 for spacebar).
- `JUMP_DELAY`: The delay between jumps in seconds (default: 0.1).

Feel free to modify these values in the `config.ini` file to suit your preferences.



