import UserController
import app
import audio
import threading

threading.Thread(target=audio.play_startup_sound).start()
threading.Thread(target=audio.play_idle_sound).start() 

UserController.register()

app.init()