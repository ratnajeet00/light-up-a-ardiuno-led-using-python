import serial
import time
import tkinter as tk

ser = serial.Serial('COM4', 9600, timeout=1)
ser.flushInput()

def send_command(command):
    byte_command = command.encode()
    ser.write(byte_command)
    time.sleep(0.5)  # wait 0.5 seconds

def on_button_click():
    send_command('H')

def off_button_click():
    send_command('L')

def quit_button_click():
    send_command('q')
    print('q entered. Exiting the program')
    ser.close()
    root.quit()

root = tk.Tk()
root.title('Bulb Control')

on_button = tk.Button(root, text='Turn On', command=on_button_click)
on_button.pack(pady=10)

off_button = tk.Button(root, text='Turn Off', command=off_button_click)
off_button.pack(pady=10)

quit_button = tk.Button(root, text='Quit', command=quit_button_click)
quit_button.pack(pady=10)

root.mainloop()
