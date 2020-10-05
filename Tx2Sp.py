import pyttsx3
import tkinter
window = tkinter.Tk()
text = tkinter.StringVar()
window.title("Talk to me")
entry = tkinter.Entry(window,textvariable = text,width = 50, bd =4, font =15,).pack()

def play():
    speaker = pyttsx3.init()
    txt = text.get()
    speaker.say(txt)
    speaker.runAndWait()

btn = tkinter.Button(window,text = "SUBMIT", width=20,font = 15,bg="yellow",command = play)
btn.pack()

window.mainloop()