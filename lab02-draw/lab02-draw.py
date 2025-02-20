"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

import arcade

WIDTH = 800
HEIGHT = 600
boat_x = 0
boat_y = 125
boat_speed = 2

arcade.open_window(800, 600)
arcade.set_background_color(arcade.color.SINOPIA)


# Drawing here
def dibujar_barco(x, y):
    arcade.draw_line(425, 200, 1000, 1000, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(425, 200, 950, 950, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(425, 200, 900, 900, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(425, 200, 850, 850, arcade.color.SELECTIVE_YELLOW, 10)

    arcade.draw_line(375, 200, -200, 1000, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(375, 200, -150, 950, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(375, 200, -100, 900, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(375, 200, -50, 850, arcade.color.SELECTIVE_YELLOW, 10)

    arcade.draw_line(400, 200, 400, 1000, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(400, 200, 415, 1000, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(400, 200, 385, 1000, arcade.color.SELECTIVE_YELLOW, 10)

    arcade.draw_line(400, 180, 1000, 370, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(400, 180, 1000, 360, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(400, 180, 1000, 350, arcade.color.SELECTIVE_YELLOW, 10)

    arcade.draw_line(400, 180, -200, 370, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(400, 180, -200, 360, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(400, 180, -200, 350, arcade.color.SELECTIVE_YELLOW, 10)

    arcade.draw_circle_filled(400, 200, 100, arcade.color.ORANGE_PEEL)
    arcade.draw_circle_filled(400, 200, 90, arcade.color.SELECTIVE_YELLOW)

    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.SPACE_CADET)

    arcade.draw_ellipse_filled(200, 490, 300, 100, arcade.color.LIGHT_PINK, 0)
    arcade.draw_circle_filled(120, 485, 55, arcade.color.LIGHT_PINK)
    arcade.draw_circle_filled(170, 485, 55, arcade.color.LIGHT_PINK)
    arcade.draw_circle_filled(230, 495, 55, arcade.color.LIGHT_PINK)
    arcade.draw_circle_filled(280, 490, 55, arcade.color.LIGHT_PINK)

    arcade.draw_ellipse_filled(200, 490, 290, 90, arcade.color.PINK_LACE, 0)
    arcade.draw_circle_filled(120, 485, 50, arcade.color.PINK_LACE)
    arcade.draw_circle_filled(170, 485, 50, arcade.color.PINK_LACE)
    arcade.draw_circle_filled(230, 495, 50, arcade.color.PINK_LACE)
    arcade.draw_circle_filled(280, 490, 50, arcade.color.PINK_LACE)

    arcade.draw_ellipse_filled(700, 450, 310, 110, arcade.color.LIGHT_PINK, 0)
    arcade.draw_circle_filled(620, 455, 60, arcade.color.LIGHT_PINK)
    arcade.draw_circle_filled(670, 445, 60, arcade.color.LIGHT_PINK)
    arcade.draw_circle_filled(730, 455, 60, arcade.color.LIGHT_PINK)
    arcade.draw_circle_filled(780, 445, 60, arcade.color.LIGHT_PINK)

    arcade.draw_ellipse_filled(700, 450, 300, 100, arcade.color.PINK_LACE, 0)
    arcade.draw_circle_filled(620, 455, 55, arcade.color.PINK_LACE)
    arcade.draw_circle_filled(670, 445, 55, arcade.color.PINK_LACE)
    arcade.draw_circle_filled(730, 455, 55, arcade.color.PINK_LACE)
    arcade.draw_circle_filled(780, 445, 55, arcade.color.PINK_LACE)

    arcade.draw_ellipse_filled(400, -20, 300, 150, arcade.color.SPACE_CADET, 0)
    arcade.draw_ellipse_filled(500, -20, 300, 150, arcade.color.SPACE_CADET, 0)
    arcade.draw_ellipse_filled(620, -20, 300, 150, arcade.color.SPACE_CADET, 0)



    arcade.draw_ellipse_filled(x, y, 300, 150, arcade.color.BISTRE  , 0)
    arcade.draw_rectangle_filled(x, y+30, 300, 90, arcade.color.SPACE_CADET)
    arcade.draw_line(x, y, x, y+210, arcade.color.BISTRE, 5)
    arcade.draw_line(x-100, y, x+100, y, arcade.color.BISTRE, 5)
    arcade.draw_triangle_filled(x-4, 130, x-98, 130, x-4, 275, arcade.color.WHITE)
    arcade.draw_triangle_filled(x+3, 130, x+100, 130, x+3, 275, arcade.color.WHITE)

def on_draw(self):
    arcade.start_render()

    """ Draw everything """
    global boat_x, boat_speed
    arcade.start_render()

    dibujar_barco(boat_x, boat_y)
    boat_x += boat_speed
    if boat_x > WIDTH + 100:
        boat_x = -200



arcade.schedule(on_draw, 1 / 60)
arcade.run()