import tkinter as tk
from tkinter import messagebox

class SettingsDialog(tk.Toplevel):
    def __init__(self, parent, initial_time, initial_interval):
        super().__init__(parent)
        self.title("Timer Settings")
        self.result = None

        # Position the dialog relative to the parent window
        self.geometry(f"+{parent.winfo_x()}+{parent.winfo_y()}")

        # Convert initial_time to hours, minutes, seconds
        hours, remainder = divmod(initial_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Time fields
        tk.Label(self, text="Time:").grid(row=0, column=0, padx=5, pady=5)
        self.hours_entry = tk.Entry(self, width=3)
        self.hours_entry.insert(0, str(hours))
        self.hours_entry.grid(row=0, column=1, padx=2, pady=5)
        tk.Label(self, text="h").grid(row=0, column=2)

        self.minutes_entry = tk.Entry(self, width=3)
        self.minutes_entry.insert(0, str(minutes))
        self.minutes_entry.grid(row=0, column=3, padx=2, pady=5)
        tk.Label(self, text="m").grid(row=0, column=4)

        self.seconds_entry = tk.Entry(self, width=3)
        self.seconds_entry.insert(0, str(seconds))
        self.seconds_entry.grid(row=0, column=5, padx=2, pady=5)
        tk.Label(self, text="s").grid(row=0, column=6)

        # Interval field (keeping it in seconds for simplicity)
        tk.Label(self, text="Interval (seconds):").grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.interval_entry = tk.Entry(self)
        self.interval_entry.insert(0, str(initial_interval))
        self.interval_entry.grid(row=1, column=2, columnspan=5, padx=5, pady=5)

        tk.Button(self, text="OK", command=self.on_ok).grid(row=2, column=0, columnspan=3, padx=5, pady=5)
        tk.Button(self, text="Cancel", command=self.on_cancel).grid(row=2, column=3, columnspan=4, padx=5, pady=5)

    def on_ok(self):
        try:
            hours = int(self.hours_entry.get())
            minutes = int(self.minutes_entry.get())
            seconds = int(self.seconds_entry.get())
            interval = int(self.interval_entry.get())
            
            total_seconds = hours * 3600 + minutes * 60 + seconds
            
            if 1 <= total_seconds <= 86400 and 0 <= interval <= 3600:
                self.result = (total_seconds, interval)
                self.destroy()
            else:
                messagebox.showerror("Invalid input", "Time must be between 1 second and 24 hours, and interval between 0 and 3600 seconds")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers")

    def on_cancel(self):
        self.destroy()
