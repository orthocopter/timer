
import tkinter as tk
from tkinter import messagebox

class SettingsDialog(tk.Toplevel):
    def __init__(self, parent, initial_time, initial_interval):
        super().__init__(parent)
        self.title("Timer Settings")
        self.result = None

        # Position the dialog relative to the parent window
        self.geometry(f"+{parent.winfo_x()}+{parent.winfo_y()}")

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
