#!/bin/python3

import sys
import pygame
import random
import time

def selection_sort(array, i, n):
    m = i
    for j in range(i+1, n):
        if array[j] < array[m]:
            m = j
    array[m], array[i] = array[i], array[m]

    return array

def main():
    size = width, height = 800, 600
    
    try:
        n = int(sys.argv[1])
    except IndexError:
        print("Usage: %s n" % sys.argv[0])
        sys.exit(1)
    except ValueError:
        print("Please enter a valid number")
        sys.exit(1)

    if n <= 0:
        print("number has to be greater than 1")
        sys.exit(1)
    elif n > width:
        print("error: n is too big")
        sys.exit(1)

    pygame.init()
    screen = pygame.display.set_mode(size)

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

        array = selection_sort(array, loops, n)
        loops += 1
        
        pygame.display.flip()

        time.sleep(0.1)

if __name__ == '__main__':
    main()
    
