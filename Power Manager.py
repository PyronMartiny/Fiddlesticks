from tkinter import *
import os

root=Tk()
root.title('Power Manager')
root.geometry("300x200")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = screen_width - 300
y = 0

root.geometry(f"300x200+{x}+{y}")
root.resizable(False, False)

# def restarttime():
# 	os.system('shutdown /r /t 30')

def restart():
	os.system('shutdown /r /t 3')

def shutdown():
	os.system('shutdown /s /t 1')

def logout():
	os.system('shutdown -l')

#first button
# restart_time_button = Button(root, text="Restart", borderwidth=1, cursor="hand2", width=10, height=1, command=restarttime )
# restart_time_button.place(x=10,y=200)

restart_button = Button(root, text="Restart", borderwidth=1, cursor="hand2", width=10, height=1, command=restart)
# restart_button.pack(pady=20)
restart_button.place(x=115,y=30)

shutdown_button = Button(root, text="Shutdown", borderwidth=1, cursor="hand2",width=10, height=1, command=shutdown)
# shutdown_button.pack(pady=20)
shutdown_button.place(x=115,y=70)

logout_button = Button(root, text="Log out", borderwidth=1, cursor="hand2",width=10, height=1, command=logout)
# logout_button.pack(pady=20)
logout_button.place(x=115,y=110)

close_button = Button(root, text="Close", borderwidth=1, cursor="hand2",width=10, height=1, command=root.destroy)
# close_button.pack(pady=20)
close_button.place(x=115,y=150)

root.mainloop()