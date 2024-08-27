import tkinter as tk
from tkinter import messagebox
from timer_control import TimerControl
from settings import SettingsDialog
from config.config import save_config, load_config

timer_control = TimerControl()

def update_ui(time_format):
    label.config(text=time_format)
    root.update()

def on_timeout():
    messagebox.showinfo("Timer", "Time's up!")

def start_timer():
    timer_control.start_timer(update_ui, on_timeout)

def stop_timer():
    timer_control.stop_timer()

def open_settings():
    dialog = SettingsDialog(root, timer_control.initial_time, timer_control.interval_seconds)
    root.wait_window(dialog)
    if dialog.result:
        timer_control.set_initial_time(dialog.result[0])
        timer_control.set_interval(dialog.result[1])
        update_ui(f"{dialog.result[0] // 60:02d}:{dialog.result[0] % 60:02d}")

# Set up the main window
root = tk.Tk()
root.title("Countdown Timer")

# Load configuration from file on application start
config = load_config()
if config:
    root.geometry(config['geometry'])
    timer_control.set_initial_time(config['time'])
    timer_control.set_interval(config['interval'])

# Save the configuration when closing the window
def on_closing():
    save_config(root.geometry(), timer_control.initial_time, timer_control.interval_seconds)
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Set up the GUI components
label = tk.Label(root, font=('Helvetica', 72), text="15:00")
label.pack(pady=20)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Create start button
start_button = tk.Button(button_frame, text="Start", command=start_timer)
start_button.pack(side=tk.LEFT, padx=5)

# Create stop button
stop_button = tk.Button(button_frame, text="Stop", command=stop_timer)
stop_button.pack(side=tk.LEFT, padx=5)

# Create settings button
settings_button = tk.Button(button_frame, text="Settings", command=open_settings)
settings_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
