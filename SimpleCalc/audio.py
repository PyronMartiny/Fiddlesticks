import os
import pygame
import threading
import time
import config

pygame.mixer.init()

startup_channel = pygame.mixer.Channel(0)
idle_channel = pygame.mixer.Channel(1)
shutdown_channel = pygame.mixer.Channel(2)
beep_channel = pygame.mixer.Channel(3)


def play_startup_sound():
	hdd_start_path = config.get_project_dir('Audio\\hddstart.wav')
	startup_sound = pygame.mixer.Sound(hdd_start_path)
	startup_channel.play(startup_sound)

def play_idle_sound():
	hdd_idle_path = config.get_project_dir('Audio\\hddidle.wav')
	idle_sound = pygame.mixer.Sound(hdd_idle_path)
	idle_channel.play(idle_sound)
	

def play_shutdown_sound():
	# global idle_channel
	hdd_shutdown_path = config.get_project_dir('Audio\\hddshutd.wav')
	shutdown_sound = pygame.mixer.Sound(hdd_shutdown_path)
	
	startup_channel.stop()
	idle_channel.stop()
	
	shutdown_channel.play(shutdown_sound)

def play_beep_sound():
	beep_path = config.get_project_dir('Audio\\beep.wav')
	beep_sound = pygame.mixer.Sound(beep_path)
	beep_channel.stop()
	beep_channel.play(beep_sound)
	fade_duration = 180
	beep_channel.fadeout(fade_duration)
	

if __name__ == "__main__":
    threading.Thread(target=play_startup_sound).start()
    threading.Thread(target=play_idle_sound).start()
    threading.Thread(target=play_shutdown_sound).start()
    threading.Thread(target=play_beep_sound).start()

