# Tocando música no Python

import pygame
pygame.init()
pygame.mixer.music.load('Desafios/ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()