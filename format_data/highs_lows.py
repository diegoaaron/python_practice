import csv

from datetime import datetime

from matplotlib import pyplot as plt

# filename = "sitka_weather_07-2014.csv"
# filename = "sitka_weather_2014.csv"
filename = "death_valley_2014.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    dates = []
    lows = []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
            
        except ValueError:
            print(current_date, "FALTA DATA")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# plot data

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha = 0.1)

# format plot

plt.title("Temperaturas de 2014", fontsize = 20)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperatura (F)", fontsize = 16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()