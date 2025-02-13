"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade
from arcade import draw_polygon_filled

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.EERIE_BLACK)

# Stars
arcade.draw_lrtb_rectangle_filled(0,800,200,000,arcade.color.ELECTRIC_GREEN)
arcade.draw_lrtb_rectangle_filled(0,800,400,200,arcade.color.HARVARD_CRIMSON)

# Cohete


# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

