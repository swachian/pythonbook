from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

def extract_row(row):
    return (datetime.strptime(row[2], '%Y-%m-%d'), int(row[4]), int(row[5]))

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)
# for index, column_header in enumerate(header_row):
#     print(index, column_header)
dates, highs, lows = zip(*[extract_row(row) for row in reader])



plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
print(dates)
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature(F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

print(plt.style.available)