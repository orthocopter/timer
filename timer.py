import tkinter as tk
from tkinter import messagebox, simpledialog
import pygame
import time

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
                    pygame.mixer.music.load("media/Connected.mp3")
                    pygame.mixer.music.play()
                    interval_counter = 0

        # Play sound when timer expires
        pygame.mixer.music.load("media/Concern.mp3")
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
        label.config(text=f'{mins:02d}:{secs:02d}')

class SettingsDialog(tk.Toplevel):
    def __init__(self, parent, initial_time, initial_interval):
        super().__init__(parent)
        self.title("Timer Settings")
        self.result = None

        tk.Label(self, text="Time (seconds):").grid(row=0, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(self)
        self.time_entry.insert(0, str(initial_time))
        self.time_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text="Interval (seconds):").grid(row=1, column=0, padx=5, pady=5)
        self.interval_entry = tk.Entry(self)
        self.interval_entry.insert(0, str(initial_interval))
        self.interval_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self, text="OK", command=self.on_ok).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(self, text="Cancel", command=self.on_cancel).grid(row=2, column=1, padx=5, pady=5)

    def on_ok(self):
        try:
            time = int(self.time_entry.get())
            interval = int(self.interval_entry.get())
            if 1 <= time <= 3600 and 0 <= interval <= 3600:
                self.result = (time, interval)
                self.destroy()
            else:
                messagebox.showerror("Invalid input", "Time must be between 1 and 3600, and interval between 0 and 3600")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers")

    def on_cancel(self):
        self.destroy()
# Set up the main window
root = tk.Tk()
root.title("Countdown Timer")

# Set up variables
total_seconds = tk.IntVar(value=900)  # Default to 15 minutes (900 seconds)
initial_time = tk.IntVar(value=900)  # Store the initial time value
interval_seconds = tk.IntVar(value=0)  # Default to 0 (no interval)

def set_interval():
    new_interval = simpledialog.askinteger("Interval Settings", "Enter interval in seconds (0 for no interval):", parent=root, minvalue=0, maxvalue=3600)
    if new_interval is not None:
        interval_seconds.set(new_interval)


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
