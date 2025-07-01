from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)
# for index, column_header in enumerate(header_row):
#     print(index, column_header)
dates, highs = zip(*[(datetime.strptime(row[2], '%Y-%m-%d'), int(row[4])) for row in reader])


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
print(dates)
ax.plot(dates, highs, color='red')

ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature(F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

print(plt.style.available)