from cgitb import text
from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as exTk
import googletrans
from googletrans import Translator
import clipboard

window = Tk()
window.title("Google translate v1.0")
window.geometry("800x700")
window.resizable(False, False)

# def


# label
lbl = Label(window, text="Google Translate", font="arial 20", fg="black")
lbl.place(x=300, y=50)
# input
frame_input = LabelFrame(window, text="Original", font="Times 13")
frame_input.place(x=70, y=270)

text_input = Text(frame_input, width=70, height=8, font="Times 13")
text_input.pack()
# output
frame_output = LabelFrame(window, text="Translations", font="Times 13")
frame_output.place(x=70, y=480)

text_output = Text(frame_output, width=70, height=8, font="Times 13")
text_output.pack()

# options
frame_option = LabelFrame(window, text="Select language")
frame_option.place(x=70, y=120)
# cmb
# cmb = exTk.Combobox(frame_option, width=20, font="arial 10")
# cmb['values'] = ('English to Vietnamese', 'Vietnamese to English')
# cmb['state'] = 'readonly'
# cmb.current(0)
# cmb.pack()
lang = ["English to Vietnamese", "Vietnamese to English",
        "Chinese to Vietnamese", "Vietnamese to Chinese"]
x = IntVar()
x.set("0")
for i in range(len(lang)):
    radiobutton = Radiobutton(
        frame_option, text=lang[i], variable=x, value=i, font="arial 10")

    radiobutton.pack()
# options


def clear():
    text_input.delete(1.0, END)
    text_output.delete(1.0, END)


def trans():

    input = text_input.get(1.0, END)
    if len(input) > 2 and len(input) < 3000:
        translate = Translator()
    # src = 'en'
    # dest = 'vi'
        if x.get() == 0:
            src = 'en'
            dest = 'vi'
        elif x.get() == 1:
            src = 'vi'
            dest = 'en'
        elif x.get() == 2:
            src = 'zh-tw'
            dest = 'vi'
        elif x.get() == 3:
            src = 'vi'
            dest = 'zh-tw'

        output = translate.translate(text=input, src=src, dest=dest)
        text_output.insert(END, output.text)
    else:
        messagebox.showerror(
            "Error! ", "Please enter text below 3000 words!")


def hadleCopy():
    output = text_output.get(1.0, END)
    if len(output) > 2:
        clipboard.copy(output)
        messagebox.showinfo(
            "Notification! ", "Copied translation to clipboard")
    else:
        messagebox.showwarning("Warning!", "The translation content is empty")


def hadlePaste():
    text_input.insert(END, clipboard.paste())
    trans()
    # messagebox.showinfo("Notification ! ", "Pasted to clipboard")
# options


btn_trans = Button(window, text="Translate", width=15, height=2, command=trans)
btn_trans.place(x=300, y=150)

btn_clear = Button(window, text="Clear Text",
                   width=17, height=2, command=clear)
btn_clear.place(x=430, y=150)

btn_copy = Button(window, text="Copy to clipboard",
                  width=15, height=2, command=hadleCopy)
btn_copy.place(x=300, y=200)

btn_pasteToClipboard = Button(window, text="Paste from clipboard",
                              width=17, height=2, command=hadlePaste)
btn_pasteToClipboard.place(x=430, y=200)
window.mainloop()
