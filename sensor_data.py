# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:57:17 2019

@author: abdulgafarg
"""
import matplotlib.pyplot as plt
import pandas as pd  
data = pd.read_csv("Sensor_record.csv", sep =",")
data.dropna(inplace = True)  # dropping null value columns to avoid errors 
print(data)

plt.figure(figsize=(15,10))
plt.plot('Time ms','AX', data=data, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4, label="AX")
plt.plot('Time ms','AY', data=data, marker='', color='olive', linewidth=2, label="AY")
plt.plot('Time ms','AZ', data=data, marker='', color='olive', linewidth=2, linestyle='dashed', label="AZ")
plt.xlabel('Time Since Start (milliseconds)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Acceleration vs Time')
plt.legend()
plt.show()

plt.figure(figsize=(12,4))
plt.plot('Time ms','GYROX', data=data, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4, label="GYROX")
plt.plot('Time ms','GYROY', data=data, marker='', color='olive', linewidth=2, label="GYROY")
plt.plot('Time ms','GYROZ', data=data, marker='', color='olive', linewidth=2, linestyle='dashed', label="GYROZ")
plt.xlabel('Time Since Start (milliseconds)')
plt.ylabel('Angular Acceleration (rad/s^2)')
plt.title('Angular Acceleration vs Time')
plt.legend()
plt.show()