# Logged hours in Elite
Short script to parse journals from the game Elite: Dangerous and extract time spent in game across multiple accounts.

## Contents

- [Logged hours in Elite](#logged-hours-in-elite)
    - [Getting started](#getting-started)
        - [.exe version](#exe-version)
        - [Python version](#python-version)
    - [How does it work?](#how-does-it-work-)
        - [Remarks](#remarks)

## Getting started

### .exe version

- Download the .exe file from the latest release
- Put the .exe in a (preferabily) dedicated folder
- Double click the .exe
- Let the script scrap the info from your journals and keep what's interesting !

### Python version

Requires [Python 3.x](https://www.python.org/downloads/)
- Download the source code from the latest release
- Extract and put the .py file in a (preferabily) dedicated folder
- Double click the .py
- Let the script scrap the info from your journals and keep what's interesting !

## How does it work ?
In Elite: Dangerous a lot of game informations are dumped into .log files: the game journals. Among the data dumped, at each beginning of a session the game logs the time played on this accounts. This tool simply searches through the last 100 journals all different accounts and then links it to it's total playtime by dumping data into a .JSON file.

### Remarks
Worth noting that: 
- This script assumes you are playing on Windows 10/11 and that your journals are stored at the default location ("%userprofile%\Saved Games\Frontier Developments\Elite Dangerous\")
- Journal data being stored locally means that data can be very outdated for accounts you haven't logged in a long time on the machine you're running the script from.
- Play time is dumped in the journal when logging into the game, not when accessing main menu.
- Given the point above: you might notice differences with the play time tracked by game launchers (Steam/Epic Games Store), the Elite launcher doesn't count as playtime for Elite