import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)

def command_line():
    print(
        "Choose command: 'High' to display the high temperatures, "
        "'Low' to display the low temperatures, "
        "and 'Exit' to Exit the program."
        )
    user_input = input(">>")
    user_input.upper()
    print("")
    if user_input != "HIGH" and user_input != "LOW" and user_input != "EXIT":
        print("Please input proper instruction.")
        print("")
        command_line()
    elif user_input == "HIGH":
        high_print()
        print("The Highs have been successfully printed.")
        print("")
        command_line()
    elif user_input == "LOW":
        low_print()
        print("The Lows have been successfully printed.")
        print("")
        command_line()
    elif user_input == "EXIT":
        print("Exiting Program. Thank you for using!")
        sys.exit()

def high_print():
    # Plot the high temperatures.
    #plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    # Format plot.
    plt.title("Daily high temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def low_print():
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')
    # Format plot.
    plt.title("Daily low temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()


command_line()