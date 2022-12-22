#!/usr/bin/env python3

import serial
import time

arduino = serial.Serial("/dev/ttyUSB0", 9600)
time.sleep(2)

'''
print("Enter 1 to turn on LED and 0 to turn off LED")

while 1:
    dataFromUser=input()

    if dataFromUser == '1':
        arduino.write(b'1')
        print("LED turned on")
    elif dataFromUser == '0':
        arduino.write(b'0')
        print("LED turned off")

'''

while True:
    line = arduino.readline()
    # print(line)
    string = line.decode()
    # print(string)
    # print(len(string))

    # list = string.split('\r')
    # print(list)
    # print(list[0])
    # print(len(list[0]))

    # list2 = list[0].split('\n')
    # print(list2[0])
    # print(len(list2[0]))

    stripped_string = string.strip()
    # print(string)

    num_int = int(stripped_string)
    # print(string)

    try:
        f = open("blabla_2_5.txt", "r")
        content = f.read()
        f.close()
# except FileNotFoundError:
#     content = '<<< NOT FOUND >>>'
#     print(content)
    except OSError as e:
        # print(e.args[1])
        print("--except:{0}".format(e.args[1]))
        f = open("blabla_2_5.txt", "w")
        f.close()

    f = open("blabla_2_5.txt", "a")
    # content = f.write(list[0])
    # content = f.write(list[1])
    f.write(stripped_string)


    # out_str = ""
    # out_str.join(list)
    # print(out_str)
    # content = f.write(out_str)
    f.close()


arduino.close()