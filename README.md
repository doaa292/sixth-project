# Mouse Coordinates + Simple Auto-Search — README

## Overview
This project contains two small tools:

1. mouse_coords.py — a utility that captures mouse coordinates on your device.
2. auto_search.py — a very simple automated search script that uses hard-coded coordinates to interact with a UI (e.g., click a search field, type a term, click search).

Why both?

Coordinates (x,y) are device-dependent (screen resolution, window size, display scaling/DPI). Use mouse_coords.py to get accurate coordinates for *your* machine, then paste them into auto_search.py so the automation works correctly.
Note:

you have to install pyautogui by writting pip statment in terminal

