import os
import utils
import time
import UserController
import messages
import sys
import winsound



def init():
	utils.loading()
	time.sleep(0.3)
	utils.print_color (messages.line)
	time.sleep(0.5)
	utils.print_color (messages.title)
	time.sleep(0.8)
	utils.print_color (messages.version)
	time.sleep(1.1)
	utils.print_color (messages.copyright)
	time.sleep(0.5)

	UserController.calculator()