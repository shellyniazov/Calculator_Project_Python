
from tkinter import *


class Calculator:


    def __init__(self, parent, x, y):

        self.button_font = ('Verdana', 15)
        self.entry_font = ('Verdana', 20)

        self.parent = parent

        self.button_width = 4
        self.button_height = 1

        self.container = Frame(self.parent) #אחראי על הארגון ועל הסדר
        self.container.grid(row=x, column=y)

        self.string = ''

        self.entry()

        self.ClickButton('7', 1, 0)
        self.ClickButton('8', 1, 1)
        self.ClickButton('9', 1, 2)

        self.ClickButton('4', 2, 0)
        self.ClickButton('5', 2, 1)
        self.ClickButton('6', 2, 2)

        self.ClickButton('1', 3, 0)
        self.ClickButton('2', 3, 1)
        self.ClickButton('3', 3, 2)

        self.ClickButton('0', 4, 0)
        self.ClickButton('(', 3, 3)
        self.ClickButton(')', 3, 4)

        self.ClickButton('+', 1, 3)
        self.ClickButton('-', 1, 4)
        self.ClickButton('*', 2, 3)
        self.ClickButton('/', 2, 4)

        self.buttonEqual('=', 4, 1)

        self.buttonClear('clear', 4, 3)
        self.buttonRemove('x', 4, 4)


    def entry(self): #אחראי על הצגה ועיצוב של הכנסת נתונים

        self.entry = Text(
            self.container, font=self.entry_font, state=DISABLED,
            height=self.button_height, width=self.button_width)

        self.entry.grid(columnspan=5, sticky='we')



    def ClickButton(self, char, x, y):

        self.b = Button(
            self.container, text=char, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            # פקודה אחראית ללחיצה מסוימת של תו ומעבירה לפונקציה שמקבלת תו(פונקציה אנונימית)
            command=lambda: self.StringThreading(char))

        self.b.grid(row=x, column=y)



    def StringThreading(self, text):#פונקציה עוסקת בשרשור של המחרוזת

        self.string += text#שרשור מחרוזת
        self.display(self.string)



    def buttonEqual(self, char, x, y):#פונקציה קשורה להצגת חישוב

        self.b = Button(
            self.container, text=char, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            command=self.equalButtonClick)

        self.b.grid(row=x, column=y, sticky='we', columnspan=2)



    def equalButtonClick(self):#פונקציה מבצעת חישוב מתמטי לפי מחרוזת לאחר שרשור

        #השיטה eval() מנתחת את הביטוי המועבר לשיטה זו ומריצה ביטוי python (קוד) בתוך התוכנית.
        self.display(eval(self.string))





    def display(self, text):#פונקציה אחראית על הצגת נתונים

        self.entry.config(state=NORMAL)
        self.entry.delete('1.0', END)
        self.entry.insert('1.0', text)
        self.entry.config(state=DISABLED)




    def buttonRemove(self, char, x, y):#פונקציה אחראית על מחיקה של תו אחד בודד

        self.b = Button(
            self.container, text=char, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            command=self.removeButtonClick)

        self.b.grid(row=x, column=y)





    def removeButtonClick(self):

        self.string = '' + self.string[0:-1]
        self.display(self.string)





    def buttonClear(self, char, x, y):#פונקציה אחראית על מחיקה של הכול

        self.b = Button(
            self.container, text=char, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            command=self.clearButtonClick)

        self.b.grid(row=x, column=y)



    def clearButtonClick(self):
        self.display('')
        self.string = ''







