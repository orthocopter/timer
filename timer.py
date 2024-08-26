from config.config import save_config, load_config
import pygame
from settings import SettingsDialog
import time
import tkinter as tk
from tkinter import messagebox

pygame.mixer.init()

def start_timer():
    try:
        if total_seconds.get() == 0:
            total_seconds.set(initial_time.get())
        
        interval_counter = 0
        while total_seconds.get() > 0:
            mins, secs = divmod(total_seconds.get(), 60)
            time_format = f'{mins:02d}:{secs:02d}'
            label.config(text=time_format)
            root.update()
            time.sleep(1)
            total_seconds.set(total_seconds.get() - 1)
            
            if interval_seconds.get() > 0:
                interval_counter += 1
                if interval_counter >= interval_seconds.get():
                    pygame.mixer.music.load("assets/media/Connected.mp3")
                    pygame.mixer.music.play()
                    interval_counter = 0

        # Play sound when timer expires
        pygame.mixer.music.load("assets/media/Concern.mp3")
        pygame.mixer.music.play()

        label.config(text="Time's up!")
        messagebox.showinfo("Timer", "Time's up!")

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number of seconds")
        
def open_settings():
    dialog = SettingsDialog(root, initial_time.get(), interval_seconds.get())
    root.wait_window(dialog)
    if dialog.result:
        new_time, new_interval = dialog.result
        total_seconds.set(new_time)
        initial_time.set(new_time)
        interval_seconds.set(new_interval)
        mins, secs = divmod(total_seconds.get(), 60)
        label.config(text=f'{mins:02d}:{secs:02d}')# Set up the main window
root = tk.Tk()
root.title("Countdown Timer")

# Set up variables
total_seconds = tk.IntVar(value=900)  # Default to 15 minutes
initial_time = tk.IntVar(value=900)  # Store the initial time value
interval_seconds = tk.IntVar(value=300)  # Default to 5 minutes

# Load configuration from file on application start
config = load_config()
if config:
    root.geometry(config['geometry'])
    initial_time.set(config['time'])
    interval_seconds.set(config['interval'])

# Save the configuration when closing the window
def on_closing():
    save_config(root.geometry(), initial_time.get(), interval_seconds.get())
    root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)

# Set up the GUI components
label = tk.Label(root, font=('Helvetica', 72), text="15:00")  # Increased font size
label.pack(pady=20)

start_button = tk.Button(root, text="Start Timer", command=start_timer, font=('Helvetica', 18))
start_button.pack(pady=20)

# Add settings button with gear icon
gear_icon = "⚙"  # Unicode gear symbol
settings_button = tk.Button(root, text=gear_icon, command=open_settings, font=('Helvetica', 18))
settings_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Run the main event loop
root.mainloop()
