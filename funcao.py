import pygame
import sys
import msvcrt
import time

def tocar_musica(caminho, repetir=True):
    pygame.mixer.init()
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play(-1 if repetir else 0) 

def parar_musica():
    pygame.mixer.music.stop()

def trocar_musica(nova_musica):
    parar_musica() 
    tocar_musica(nova_musica, repetir=True)

def digitar_texto(texto, velocidade=0.05):
    for caractere in texto:
        if msvcrt.kbhit():  # Verifica se alguma tecla foi pressionada
            tecla = msvcrt.getch()
            if tecla == b'\r':  # ENTER foi pressionado
                print(texto)
                return


        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(velocidade)

tocar_musica('audios\\silvio-santos-abertura-show-do-milhao.mp3')

