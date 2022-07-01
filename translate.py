from msilib.schema import ComboBox
from tkinter import *
import tkinter.ttk as exTk
import googletrans
from googletrans import Translator

window = Tk()
window.title("Google translate v1.0")
window.geometry("800x600")
window.resizable(False, False)

# def


def clear():
    pass


def trans():
    src = 'en'
    dest = 'vi'
    if cmb.current(0):
        src = 'en'
        dest = 'vi'
    if cmb.current(1):
        src = 'vi'
        dest = 'en'
    input = text_input.get(1.0, END)
    trans = Translator()
    output = trans.translate(text=input, src=src, dest=dest)
    text_output.insert(END, output.text)


# label
lbl = Label(window, text="Google Translate", font="arial 20", fg="black")
lbl.place(x=300, y=50)
# input
frame_input = LabelFrame(window, text="Bản gốc")
frame_input.place(x=70, y=200)

text_input = Text(frame_input, width=70, height=7, font="arial 12")
text_input.pack()
# output
frame_output = LabelFrame(window, text="Bản dịch")
frame_output.place(x=70, y=400)

text_output = Text(frame_output, width=70, height=7, font="arial 12")
text_output.pack()

# options
frame_option = LabelFrame(window, text="Chọn ngôn ngữ")
frame_option.place(x=70, y=150)
# cmb
cmb = exTk.Combobox(frame_option, width=20, font="arial 10")
cmb['values'] = ('English to Vietnamese', 'Vietnamese to English')
cmb['state'] = 'readonly'
cmb.current(0)
cmb.pack()
# lang = ["EN to VI", "VI to EN"]
# x = IntVar()
# x.set("0")
# for i in range(len(lang)):
#     radiobutton = Radiobutton(
#         frame_option, text=lang[i], variable=x, value=i, font="arial 10")
#     radiobutton.pack()
# options

# options

btn_trans = Button(window, text="Translate", width=15, height=2, command=trans)
btn_trans.place(x=300, y=150)

btn_clear = Button(window, text="Clear Text",
                   width=15, height=2, command=clear)
btn_clear.place(x=450, y=150)


# translator = Translator()
# output = translator.translate("xin chào !", src="vi", dest="en")
# print(output.text)
window.mainloop()
