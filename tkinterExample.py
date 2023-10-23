import tkinter as t

def createWindow(title:str)->t.Tk:
    window = t.Tk()
    window.title(title)
    window.geometry("720x720")
    return window
def addElements(root:t.Tk) -> None:
    increment_label = t.Label(root,text="0")
    buttons_frame = t.Frame(root)
    add_button = t.Button(buttons_frame,text="Add")
    add_button.config(command=lambda: increment_label.config(text=str(int(increment_label.cget("text"))+1)))
    sub_button = t.Button(buttons_frame,text="Subtract")
    sub_button.config(command=lambda: increment_label.config(text=str(int(increment_label.cget("text"))-1)))

    increment_label.pack(side=t.TOP,fill="x")
    buttons_frame.pack(side=t.TOP,fill="x")
    add_button.pack(side=t.LEFT,expand=True)
    sub_button.pack(side=t.LEFT,expand=True)
 
root = createWindow("Application")

addElements(root)

root.mainloop()