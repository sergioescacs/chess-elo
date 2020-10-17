import elo
from tkinter import *
from tkinter import messagebox

root = Tk()

opt = ["10", "13", "16", "20", "23", "24", "30", "32", "40"] #k constant option list
variable = StringVar(root)
variable.set(opt[0])

results = ["1", "0.5", "0"]#result option list
variable_r = StringVar(root)
variable_r.set(results[0])

#Deploy Labels and various content as buttons and option lists
main = LabelFrame(root, text="Chess ELO app - beta 0.1.1.")
txt1 = Label(main, text = "Your ELO: ")
E1 = Entry(main, bd =3)
txt2 = Label(main, text = "Your enemy's ELO: ")
E2 = Entry(main, bd =3)

#K option list
mb = OptionMenu(main, variable, *opt )
mb.config(width=20, font=('Helvetica', 12))

#Result option list
mb_r = OptionMenu(main, variable_r, *results )
mb_r.config(width=20, font=('Helvetica', 12))

def submit_info(): #first grab all information and prepare the call to the elo.py algorithm
    messagebox.showinfo("ELO variation", E1.get()+"  -->  "+ str(elo.calcular(int(variable.get()), int(E1.get()), int(E2.get()), int(variable_r.get()))))

Submit = Button(main, text ="Submit", command = submit_info) #submit button

#pack content & show on screen
main.pack(fill="both", expand="yes")
txt1.pack()
E1.pack()
txt2.pack()
E2.pack()
mb.pack()
mb_r.pack()

Submit.pack(side = RIGHT)
 
root.mainloop()