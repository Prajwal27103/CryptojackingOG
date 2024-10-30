import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import animation
import psutil
import matplotlib.pyplot as plt
import numpy as np
from threading import Thread
import threading
from tkinter import messagebox, Tk
import time

# The rest of your code continues here...


CPU_THRESHOLD=80
#initialize plotting
fig,ax=plt.subplots()
cpu_usage_data=[]

def update_graph(i):
    # Get CPU usage for each core
    cpu_usage_per_core = psutil.cpu_percent(interval=1, percpu=True)
    cpu_usage_data.append(cpu_usage_per_core)
    
    # Limit the displayed data points to 100 for each core
    if len(cpu_usage_data) > 100:
        cpu_usage_data.pop(0)

    ax.clear()
    for core_num, core_usage in enumerate(zip(*cpu_usage_data)):  # Unpack usage data for each core
        ax.plot(core_usage, label=f'Core {core_num} Usage (%)')
    
    ax.axhline(y=CPU_THRESHOLD, color='r', linestyle='--', label='Threshold')
    ax.legend(loc='upper right')
    ax.set_ylim(0, 100)
    ax.set_title('Per-Core CPU Usage Over Time')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('CPU Usage (%)')
def monitor_cpu():
    while True:
        # Get CPU usage for each core
        cpu_usage_per_core = psutil.cpu_percent(interval=1, percpu=True)
        
        # Check if any core's usage exceeds the threshold
        if any(core_usage > CPU_THRESHOLD for core_usage in cpu_usage_per_core):
            show_warning()

        time.sleep(5)  # Check every 5 seconds

# Function to show warning
def show_warning():
    response = messagebox.askyesno("Warning", "High CPU usage detected on one or more cores!\nAre you performing a CPU-intensive task?")
    if not response:  # If user clicks 'No'
        troubleshooting = (
            "1. Check running processes.\n"
            "2. Reboot the system.\n"
            "3. Change SSH credentials.\n"
            "4. Scan for malware."
        )
        messagebox.showinfo("Warning", "You may have been cryptojacked.\nPlease consider the following steps:\n\n" + troubleshooting)

# Set up main Tkinter window
root = Tk()
root.title("CPU Usage Monitor")

# Embed matplotlib plot into Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Set up CPU monitoring in a separate thread
threading.Thread(target=monitor_cpu, daemon=True).start()

# Set up live plot update
ani = animation.FuncAnimation(fig, update_graph, interval=1000)

# Run the application
root.mainloop()
