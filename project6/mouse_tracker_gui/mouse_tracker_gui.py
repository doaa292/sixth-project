import tkinter as tk
import pyautogui

root = tk.Tk()
root.title("Mouse Coordinates")
root.attributes("-topmost", True)
root.resizable(False, False)
label = tk.Label(root, text="X=0 Y=0", font=("Consolas", 40), padx=10, pady=6)
label.pack()

def update():
    x, y = pyautogui.position()
    label.config(text=f"X={x}  Y={y}")
    root.after(50, update)

update()
root.mainloop()
