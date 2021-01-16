import os
from serial import Serial
import numpy as np
import matplotlib.pyplot as plt
import time

ser = Serial('COM3', 9600)
time.sleep(2)       # Sleep for two seconds
option = 'y'
while ((option == 'y') or (option == 'Y')) :
    os.system("CLS")

    V1 = np.array([])
    V2 = np.array([])
    T = np.array([])

    print('SYSTEM READY') 
    string = 'blank'
    start_time = time.time()
    while (string != 'STOP SAMPLING\r\n'):
        confirm = ser.readline()
        string = confirm.decode()       # Converts serial data which is in byte code into Unicode
        string.strip(' ,\n,\r')
        disint = string.split(' ')
        try:
            V1 = np.append(V1, float(disint[1]))
            V2 = np.append(V2, float(disint[3]))
            T = np.append(T, time.time() - start_time)
            t += 40e-6
        except : 
            pass
    print("SAMPLING STOPPED. \nPREPARING THE PLOT. PLEASE WAIT...")
    print(V1, V2, T)
    plt.figure()
    plt.plot(T, V1, color = 'red')
    plt.plot(T, V2, color = 'green')
    plt.show()
    option = input("Take another sample? (Y/N) (not case-sensitive): ")   