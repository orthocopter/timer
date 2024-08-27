import time
from threading import Thread
from typing import Callable

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class TimerControl:
    def __init__(self):
        self.running = False
        self.initial_time = 900
        self.interval_seconds = 300
        self.current_time = self.initial_time
        self.on_tick = None
        self.on_timeout = None
        pygame.mixer.init()

    def start_timer(self, on_tick: Callable[[str], None], on_timeout: Callable[[], None]):
        self.on_tick = on_tick
        self.on_timeout = on_timeout
        self.current_time = self.initial_time
        self.running = True
        Thread(target=self._run_timer).start()

    def _run_timer(self):
        interval_counter = 0
        while self.running and self.current_time > 0:
            minutes, seconds = divmod(self.current_time, 60)
            time_format = f"{minutes:02d}:{seconds:02d}"
            self.on_tick(time_format)
            time.sleep(1)
            self.current_time -= 1
            
            if self.interval_seconds > 0:
                interval_counter += 1
                if interval_counter >= self.interval_seconds:
                    self.play_interval_sound()
                    interval_counter = 0

        if self.current_time <= 0:
            self.play_end_sound()
            self.on_timeout()

    def stop_timer(self):
        self.running = False

    def set_initial_time(self, time):
        self.initial_time = time

    def set_interval(self, interval):
        self.interval_seconds = interval

    def play_interval_sound(self):
        pygame.mixer.music.load("assets/media/Connected.mp3")
        pygame.mixer.music.play()

    def play_end_sound(self):
        pygame.mixer.music.load("assets/media/Concern.mp3")
        pygame.mixer.music.play()
