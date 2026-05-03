from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows = [], [], []
high_index = header_row.index('TMAX')
low_index = header_row.index('TMIN')
date_index = header_row.index('DATE')
for row in reader:
    current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
    try:
        high = int(row[high_index])
        low = int(row[low_index])        
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        lows.append(low)
        highs.append(high)


# Plot
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='cyan', alpha=0.05)

ax.set_title('Daily High and Low Temperatures, 2021\nDeath Valley, CA', fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() # Draws the labels diagonally
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=12)

plt.show()
