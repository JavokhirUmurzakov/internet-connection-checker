from tkinter import *
import threading
import socket
import time

def is_connected():
    try:
        socket.create_connection(("www.google.com",80))
        print('online')
    except OSError:
        print('offline')

tt3 = threading.Event()

while 1:
    t3 = threading.Thread(target=is_connected())
    t3.start()
    time.sleep(1)