# 21. Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Deusa_de_Itamaraca.mp3')
pygame.mixer.music.play()

input('Pressione Enter para parar a música...')
pygame.mixer.music.stop()
