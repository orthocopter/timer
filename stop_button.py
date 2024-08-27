import customtkinter as ctk
from PIL import Image
import cairosvg
import io

class StopButton(ctk.CTkButton):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, command=command, **kwargs)
        
        # Load the stop icon from SVG
        svg_path = "assets/icons/stop.svg"
        png_data = cairosvg.svg2png(url=svg_path, output_width=20, output_height=20)
        stop_icon = Image.open(io.BytesIO(png_data))
        
        self.stop_image = ctk.CTkImage(light_image=stop_icon, dark_image=stop_icon, size=(20, 20))
        
        # Set the image for the button
        self.configure(image=self.stop_image, text="")
        
        # You can customize the button appearance here
        self.configure(
            width=40,
            height=40,
            corner_radius=20,
            hover_color="darkred"
        )