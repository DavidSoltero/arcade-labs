import arcade

SCREEN_WIDTH = 2496
SCREEN_HEIGHT = 1664
MOVEMENT_SPEED = 9
DEAD_ZONE = 0.02


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

    def on_update(self, screen_width, screen_height):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > screen_width - self.radius:
            self.position_x = screen_width - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > screen_height - self.radius:
            self.position_y = screen_height - self.radius


class MyGame(arcade.Window):

    def __init__(self):
        screen_width, screen_height = arcade.get_display_size()

        # Call the parent class's init function
        super().__init__(screen_width, screen_height, "Juego en Pantalla Completa", fullscreen=True)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(screen_width // 2, screen_height // 2, 0, 0, 15, arcade.color.AUBURN)

        # Get a list of all the game controllers that are plugged in
        joysticks = arcade.get_joysticks()

        # If we have a game controller plugged in, grab it and
        # make an instance variable out of it.
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            print("There are no joysticks.")
            self.joystick = None

    def on_draw(self):

        """ Called whenever we need to draw the window. """
        self.clear()
        self.ball.draw()

    def on_update(self, delta_time):
        # Update the position according to the game controller
        if self.joystick:

            # Aplicar una zona muerta para evitar movimientos no deseados
            x_movement = self.joystick.x if abs(self.joystick.x) > DEAD_ZONE else 0
            y_movement = self.joystick.y if abs(self.joystick.y) > DEAD_ZONE else 0

            # Actualizar la velocidad de la bola en función del joystick
            self.ball.change_x = x_movement * MOVEMENT_SPEED
            self.ball.change_y = -y_movement * MOVEMENT_SPEED

            if self.joystick.buttons[9]:
                print("Botón Start presionado. Cerrando el juego...")
                arcade.close_window()

        self.ball.on_update(self.width, self.height) #La bola se actualiza



def main():
    window = MyGame()
    arcade.run()


main()