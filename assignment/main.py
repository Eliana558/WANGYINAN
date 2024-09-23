import csv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

filename = "daily_HKA_RF_2024.csv"

dates = []
rainfall = []

try:
    
    with open(filename, 'r', encoding='UTF8') as f:
        spamreader = csv.reader(f, delimiter=',')
        header = next(spamreader)  
        print(f"Header: {header}") 
        for row in spamreader:
            try:
                date_str = f"{row[0]}-{row[1].zfill(2)}-{row[2].zfill(2)}"
                date = datetime.strptime(date_str, '%Y-%m-%d')
                dates.append(date)
                
                
                if row[3] == 'Trace':
                    rainfall.append(0.01)  
                else:
                    rainfall.append(float(row[3]))
            except Exception as e:
                print(f"Error processing row {row}: {e}")
except FileNotFoundError:
    print(f"File {filename} not found.")
except Exception as e:
    print(f"An error occurred: {e}")

if dates and rainfall:

    fig, ax = plt.subplots(figsize=(10, 5))

 
    fig.patch.set_facecolor('#f5f5dc')
    ax.set_facecolor('#f5f5dc')

    
    ax.set_title('Daily Rainfall in HKA for January 2024')
    ax.set_xlabel('Date')
    ax.set_ylabel('Rainfall (mm)')
    ax.grid(True)

    line, = ax.plot([], [], marker='o', linestyle='-', color='darkblue')  


    def update(frame):
        line.set_data(dates[:frame], rainfall[:frame])
        ax.set_xlim(dates[0], dates[-1])
        ax.set_ylim(0, max(rainfall) + 1)

    ani = FuncAnimation(fig, update, frames=len(rainfall), repeat=False, interval=100)  

    plt.tight_layout()
    plt.show()
else:
    print("No data to plot.")