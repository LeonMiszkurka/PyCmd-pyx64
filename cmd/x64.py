from tkinter import *
import platform  # Import the platform module to retrieve system information

def launch():
    windows_version = platform.version()  # Get the Windows version
    cmd = Tk()
    cmd.title(f"PyCmd-pyx64 1.0.0 --windows:{windows_version}")  # Include the version in the title
    cmd.mainloop()

main = Tk()
main.title("PyCmd")
launch_button = Button(main, text="Launch cmd", command=launch)
launch_button.pack()
main.geometry('300x300')
main.mainloop()
