"""
Create a simple calculator app
"""
import tkinter as tk

# TODO Make a calculator app like the one shown in the calculator.png image
#  located in this folder.
#  HINT: you'll need: 2 text fields, 4 buttons, and 1 label
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.field_a = tk.Entry(self)
        self.field_a.place(relx=0.05, rely=0.1, relwidth=0.4, relheight=0.1)
        self.field_b = tk.Entry(self)
        self.field_b.place(relx=0.55, rely=0.1, relwidth=0.4, relheight=0.1)
        self.button_add = tk.Button(self, text="add", command=self.button_add_onclick)
        self.button_add.place(relx=0.1, rely=0.25, relwidth=0.1, relheight=0.1)
        self.button_sub = tk.Button(self, text="subtract", command=self.button_sub_onclick)
        self.button_sub.place(relx=0.3, rely=0.25, relwidth=0.1, relheight=0.1)
        self.button_mul = tk.Button(self, text="multiply", command=self.button_mul_onclick)
        self.button_mul.place(relx=0.5, rely=0.25, relwidth=0.1, relheight=0.1)
        self.button_div = tk.Button(self, text="divide", command=self.button_div_onclick)
        self.button_div.place(relx=0.7, rely=0.25, relwidth=0.1, relheight=0.1)
        self.output = tk.Label(self, font=('Rockwell', 20, 'normal'))
        self.output.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)
    def button_add_onclick(self):
        self.output.config(text=str(int(self.field_a.get()) + int(self.field_b.get())))
    def button_sub_onclick(self):
        self.output.config(text=str(int(self.field_a.get()) - int(self.field_b.get())))
    def button_mul_onclick(self):
        self.output.config(text=str(int(self.field_a.get()) * int(self.field_b.get())))
    def button_div_onclick(self):
        self.output.config(text=str(int(self.field_a.get()) / int(self.field_b.get())))
if __name__ == "__main__":
    app = Calculator()
    app.title("Calculator")
    app.geometry("1000x500")
    app.mainloop()