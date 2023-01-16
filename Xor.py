import tkinter as tk
from tkinter import messagebox
class Xor():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Xor")
        self.window.geometry("450x450")
        self.window.config(bg="skyblue")
    def help(self):
        txt = open("help.txt","r")
        l = txt.read()
        messagebox.showinfo("Xor","{}".format(l))
    def calculate(self):
        try:
            usernumber = self.input.get()
            l = usernumber.split()            
            s = 0
            for i in l:
                s^=int(i)
                self.input.set("")
                self.input.set(str(s))
        except:
            messagebox.showerror("Xor","please enter number")
    def vars(self):
        self.input = tk.StringVar()
    def body(self):
        tk.Label(self.window,text="Enter your numbers",fg="black"
        ,bg="skyblue",font=("Bahnschrift Condensed",24)).grid(row=1,column=0)
        tk.Button(self.window,text="help",fg="black"
        ,bg="skyblue",bd=0,font=("Bahnschrift Condensed",20),cursor="hand2",command=(self.help)).grid(row=1,column=4)
        tk.Entry(self.window,textvariable=self.input,
        bg="skyblue",fg="black",font=("Bahnschrift Condensed",19)).grid(row=2,column=0)
        tk.Button(self.window,text="Calculate",fg="black"
        ,bg="skyblue",bd="0",cursor="hand2",
        font=("Bahnschrift Condensed",24),command=(self.calculate)).grid(row=3,column=0)        
    def main(self):
        self.vars()
        self.body()
        self.window.mainloop()
xor = Xor()
xor.main()