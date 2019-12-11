import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pb1 import utility

def a():
    df = utility.read_csv()
    
def b():
    df = utility.read_data()
    fig, axs = plt.subplots(2)
    axs[0].plot(df['DATE'], df['SRAD'])
    axs[0].set(xlabel='DATE', ylabel='Solar irradiance')

    axs[1].plot(df['DATE'], df['RAIN'])
    axs[1].set(xlabel='DATE', ylabel='Rain')

    plt.tight_layout()
    plt.savefig("pb1/solar_rain.png")
    plt.clf()

    fig, axs = plt.subplots(3)
    axs[0].plot(df['DATE'], df['TMAX'])
    axs[0].set(xlabel='DATE', ylabel='max Temp')
    axs[1].plot(df['DATE'], df['TMIN'])
    axs[1].set(xlabel='DATE', ylabel='min Temp')
    axs[2].plot(df['DATE'], df['TAVE'])
    axs[2].set(xlabel='DATE', ylabel='avg Temp')
    plt.tight_layout()
    plt.savefig("pb1/temp.png")
    plt.clf()