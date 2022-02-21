import pygame
#import time
from pygame.locals import * # constants used by pygame

def block_draw(): #This function will go inside the event while loop
    game_window.fill((110, 100, 50))  #In this function. This will create a new surface everytime the block_draw fun is called, which will clearn the screen
    game_window.blit(block,(block_x,block_y)) #blit is used to place an imagine on the UI surface
    pygame.display.update() # Using .update portions of the screen for software displays. This must come fter the .fill method to update the display




if __name__ == "__main__" :
    pygame.init() # initialize the module of pygame

    #Creation of the surface object#

    game_window = pygame.display.set_mode((1000,500)) #Initializing a window for display & setting the game's window size. This will return a surface object
    game_window.fill((110,100,50)) #Selecting the color for the surface object. From the surface doc .fill can be found

    block = pygame.image.load("resources/blackblock.png").convert() #this line is to bring the image we have loaded into the UI
    block_x = 100
    block_y=100
    game_window.blit(block,(block_x,block_y)) #blit is used to place an imagine on the UI surface
    pygame.display.update() # Using .update portions of the screen for software displays. This must come fter the .fill method to update the display
    #time.sleep(5) #time module to pause the execution of the program for a set sec

    #Create an event loop#

    #Create an event loop ( a while loop) this is essential for all UIs in any programming language
    ##This is a loop that waits for the user's input to perfrom a specific output
    #This loop will allow us to close the program once we click Esc or the x mark
    #this loop will control the movement's of the block

    execution = True
    while execution == True:
        for event in pygame.event.get(): #This is useful after importing pygame.locals
            if event.type == KEYDOWN: #KEYDOWN is from  pygame.locals
                if event.key == K_ESCAPE:  #K_ESCAPE is the act of clicking on the Esc button
                    execution = False
                if event.key == K_UP:  #K_UP is the up key
                    block_y = block_y - 10
                    block_draw()
                if event.key == K_DOWN:
                    block_y = block_y + 10
                    block_draw()
                if event.key == K_LEFT:
                    block_x = block_x - 10
                    block_draw()
                if event.key == K_RIGHT:
                    block_x = block_x + 10
                    block_draw()
            elif event.type == QUIT: #QUIT is the act of clicking on the x of a window
                execution = False

