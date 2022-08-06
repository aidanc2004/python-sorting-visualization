#!/bin/python3

import sys
import pygame
import random
import time

n = int(sys.argv[1]) # move this please

def selection_sort(array, i):
    m = i
    for j in range(i+1, n):
        if array[j] < array[m]:
            m = j
    array[m], array[i] = array[i], array[m]

    return array

def main():
    pygame.init()

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    if n > width:
        print("error: n is too big")
        sys.exit(1)

    black = 0, 0 ,0
    white = 255, 255, 255
    
    array = list(range(1,n+1))
    random.shuffle(array)

    loops = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(black)
        
        for i, v in enumerate(array):
            x = i * width / n
            y = height - (v * (height / n))
            w = width / n
            h = height
            
            rect = pygame.Rect((x, y), (w, h))
            pygame.draw.rect(screen, white, rect)

        array = selection_sort(array, loops)
        loops += 1
        
        pygame.display.flip()

        time.sleep(0.1)

if __name__ == '__main__':
    main()
    
