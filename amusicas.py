import pygame
import time
import threading
def tocar_musica(caminho_do_arquivo):
    pygame.mixer.init() # Inicializa o mixer de áudio
    pygame.mixer.music.load(caminho_do_arquivo) # Carrega a música
    pygame.mixer.music.play(-1) # Toca a música em loop (-1 para tocar indefinidamente)
def parar_musica():
    pygame.mixer.music.stop() # Para a reprodução da música
def ini():
    caminho_da_musica = 'Inicil.mp3'
    musica_thread = threading.Thread(target=tocar_musica, args=(caminho_da_musica,))
    musica_thread.start()
def cidade01():
    caminho_da_musica = 'cidade1.mp3'
    musica_thread = threading.Thread(target=tocar_musica, args=(caminho_da_musica,))
    musica_thread.start()
def rotasmm():
    caminho_da_musica = 'cidade1.mp3'
    musica_thread = threading.Thread(target=tocar_musica, args=(caminho_da_musica,))
    musica_thread.start()
def batalhas():
    caminho_da_musica = 'batalha.mp3'
    musica_thread = threading.Thread(target=tocar_musica, args=(caminho_da_musica,))
    musica_thread.start()
def labirinto_music():
    caminho_da_musica = 'cidade1.mp3'
    musica_thread = threading.Thread(target=tocar_musica, args=(caminho_da_musica,))
    musica_thread.start()
def cidade02():
    caminho_da_musica = 'cidade2.mp3'
    musica_thread = threading.Thread(target=tocar_musica, args=(caminho_da_musica,))
    musica_thread.start()
def cidade03():
    caminho_da_musica = 'cidade3.mp3'
    musica_thread = threading.Thread(target=tocar_musica, args=(caminho_da_musica,))
    musica_thread.start()
def music_boss():
    caminho_da_musica = 'Gym.mp3'
    musica_thread = threading.Thread(target=tocar_musica, args=(caminho_da_musica,))
    musica_thread.start()
def combat():
    caminho_da_musica = 'batalha.mp3'
    musica_thread = threading.Thread(target=tocar_musica, args=(caminho_da_musica,))
    musica_thread.start()
def vitoria():
    caminho_da_musica = 'vitoria.mp3'
    musica_thread = threading.Thread(target=tocar_musica, args=(caminho_da_musica,))
    musica_thread.start()
def cidade04():
    caminho_da_musica = 'cidade4.mp3'
    musica_thread = threading.Thread(target=tocar_musica, args=(caminho_da_musica,))
    musica_thread.start()