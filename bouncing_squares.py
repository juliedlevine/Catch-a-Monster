import pygame

class Square(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.x_dir = 1
        self.y_dir = 1
        self.color = color
        self.width = 100
        self.height = 100

    def update(self):
        self.x += self.x_dir
        self.y += self.y_dir

    def display(self, screen):
        pygame.draw.rect(
        screen,
        self.color,
        (self.x, self.y, self.width, self.height),
        0)

def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)

    # Game initialization
    pygame.init()
    screen = pygame.display.set_mode((width, height))

    squares = [
        Square(200, 200, (255, 0, 0)),
        Square(100, 50, (170, 66, 244)),
        Square(10, 300, (65, 244, 193)),
        Square(300, 300, (244, 184, 65))
    ]

    pygame.display.set_caption("Julie's Game")
    clock = pygame.time.Clock()

    # Game initialization

    stop_game = False
    while not stop_game:

        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        # Make square move diagonally across screen
        for square in squares:
            square.update()

        # Draw background
        screen.fill(blue_color)

        # Render
        for square in squares:
            square.display(screen)

        # Game display
        pygame.display.update()
        clock.tick(60)

        for square in squares:
            # RIGHT: square goes past right side of display:
            if square.x + square.width > width:
                # Change values to negative to make it change direction
                square.x_dir = -square.x_dir

            # LEFT: square goes above top of display:
            if square.y + square.height > height:
                square.y_dir = -square.y_dir

            # TOP: square goes past left side of display:
            if square.x < 0:
                square.x_dir = -square.x_dir

            # BOTTOM: square goes past bottom of display:
            if square.y < 0:
                square.y_dir = -square.y_dir

    pygame.quit()

if __name__ == '__main__':
    main()
