import os
import pygame as py

class Character:
    def __init__(self, image_location):
        self.image = py.image.load(image_location)

def window(screen_width, screen_height, player_start_position_x, player_start_position_y):
    # Initialize the pygame window
    py.display.init()

    # Sets the users display size 
    window = py.display.set_mode([screen_width,screen_height])
    
    # Use the os module to find the actual path, then assign my_character to the image
    image_directory = os.path.expanduser("~/python-projects/pokemon-clone/assets/R.png")
    my_character = Character(image_directory)

    #Stores the characters movement velocity
    velocity = 5

    # Initilizes the pygame clock
    clock = py.time.Clock()
    
    # While running is true, window will loop
    running = True
    while running:
        # Fills the window with the grass colour
        window.fill((112,200,160))

        # Draw the character and update the display
        window.blit(my_character.image, (player_start_position_x, player_start_position_y))
       
        # Sets the frame rate to 60fps
        clock.tick(60)

        # Event loop
        for event in py.event.get():
            if event.type == py.QUIT:
                running == False
                py.quit()
                quit()
            
            # Checks if user presses a key, moves the players x and y using velocity 
            # with the respective key and direction
            key_pressed = py.key.get_pressed()

            if key_pressed[py.K_LEFT] or key_pressed[py.K_a]:
                player_start_position_x -= velocity
            if key_pressed[py.K_RIGHT] or key_pressed[py.K_d]:
                player_start_position_x += velocity
            if key_pressed[py.K_UP] or key_pressed[py.K_w]:
                player_start_position_y -= velocity
            if key_pressed[py.K_DOWN] or key_pressed[py.K_s]:
                player_start_position_y += velocity
            
            # Draws to the screen
            py.display.update()

    # Quit pygame
    py.quit()

def main():
    player_x = 100
    player_y = 100

    display_width = int(input("Please enter your display width: "))
    display_height = int(input("Please enter your display height: "))
    window(display_width,display_height, player_x, player_y)

if __name__ == "__main__":
    main()
