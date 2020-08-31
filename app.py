import pygame
import game_config as gc
from animal import Animal
from pygame import display, event, image
from time import sleep



def find_index(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return index

pygame.init()

display.set_caption("Matching Animals")

screen = display.set_mode((512, 512))

matched = image.load('other_assets/matched.png')



#screen.blit(matched, (0, 0))
#display.flip()

running = True

tiles = [Animal(i) for i in range(gc.NUM_TILES_TOTAL)]

current_images = []



while running:
    current_events = event.get()

    for e in current_events:
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            index = find_index(mouse_x, mouse_y)
            if index not in current_images:
                current_images.append(index)
            if len(current_images) > 2:
                current_images = current_images[1:]

    screen.fill((255, 255, 255))

    total_skips = 0

    for tile in tiles:
        image_i = tile.image if tile.index in current_images else tile.box
        
        if not tile.skip:
            screen.blit(image_i, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
        else:
            total_skips += 1


    display.flip()

    if len(current_images) == 2:
        i, j = current_images
        if tiles[i].name == tiles[j].name:
            tiles[i].skip = True
            tiles[j].skip = True
            sleep(0.4)
            screen.blit(matched, (0,0))
            display.flip()
            sleep(0.4)
            current_images = []

    
    if total_skips == len(tiles):
        running == False


print("Goodbye")