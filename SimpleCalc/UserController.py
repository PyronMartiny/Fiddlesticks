# import os
import utils
import random
import messages
import time
from pymongo import MongoClient
import sys
import audio
import app
import threading
import pygame

client = MongoClient('mongodb://127.0.0.1:27017/')

db = client.mydatabase

users = db.registry
# print('users', users)
# user = users.find_one({"username": "alex"})
# print('user', user)

# hdd_idle_path = r"C:\Users\Kyron\Desktop\Desktop\Sublime Code\SimpleCalc\Audio\hddidle.wav"
# winsound.PlaySound(hdd_idle_path,winsound.SND_FILENAME)

def register():
    time.sleep(7)
    try:
        while True:
            utils.print_color(messages.input_username)
            username = input('').strip()
            # print(f"Username entered: '{username}'")
            
            if not username:
                utils.print_color("Username cannot be empty.")
                continue

            if users.find_one({'username': username}):
                utils.print_color("Username already exists.")
                continue
            break    
        while True:
            utils.print_color(messages.choose_password)
            password = input('').strip()

            if len(password) < 6:
                utils.print_color(messages.password_error)
                continue
            else:
                break
        
        users.insert_one({'username': username, 'password': password})

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def login():
    time.sleep(7)
    while True:
        utils.print_color(messages.enter_username)
        username_input = input('')
        user = users.find_one({'username': username_input}) 
        if not user:
            utils.print_color(messages.no_user_found)
            continue
        else:
            break

    while True:
        utils.print_color(messages.enter_password)
        password_input = input('')

        if user['password'] != password_input:
            utils.print_color(messages.invalid_password)
            continue
        else:
            utils.memcheck()
            # utils.loading()
            time.sleep(0)
            break

def calculator():
    while True:
        utils.print_color('> ')
        calculation = input('')
        if calculation.strip().lower() == 'exit':
            threading.Thread(target=audio.play_shutdown_sound).start()
            time.sleep(10)
            break

        if len(calculation) == 0:
            continue

        try:
            result = eval(calculation)
            if isinstance(result, float):
                result = round(result, 2)
            utils.print_color(f'{result}\n')
        except Exception as e:
            utils.print_color(f'Error: {e}\n')
