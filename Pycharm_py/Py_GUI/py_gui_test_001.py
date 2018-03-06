# -*- coding:UTF-8 -*-



from Tkinter import *
root = Tk()
def helloButton():
   print ("你输入的是：",test_contents.get())

test_contents=StringVar()
input_info=Entry(root,textvariable=test_contents)
#input_info.get()
input_info.pack()
Button(root, text='hello', command=helloButton).pack()


input_info.bind("<Button-1>",helloButton())

root.mainloop()
