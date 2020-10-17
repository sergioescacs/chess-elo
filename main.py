import elo
from tkinter import *
from tkinter import messagebox

root = Tk()

photo = PhotoImage(file = "xadrez.png") #set the future icon photo as a variable

#process the image and set it as the main icon of the app
root.iconphoto(False, photo)
root.title("ELO calc.")
root.resizable(False, False)

opt = ["10", "13", "16", "20", "23", "24", "30", "32", "40"] #k constant option list
variable = StringVar(root)
variable.set(opt[0])

results = ["1", "0.5", "0"]#result option list
variable_r = StringVar(root)
variable_r.set(results[0])

#Deploy Labels and various content as buttons and option lists
main = LabelFrame(root, text="Chess ELO app - beta 0.2.1.", font=('Arial', 10, "bold"))
txt1 = Label(main, text = "Your ELO: ", font=('Helvetica', 9))
E1 = Entry(main, bd =3)
txt2 = Label(main, text = "Your enemy's ELO: ", font=('Helvetica', 9))
E2 = Entry(main, bd =3)
txt3 = Label(main, text = "K: ", font=('Helvetica', 9))

#K option list
mb = OptionMenu(main, variable, *opt )
mb.config(width=8, font=('Helvetica', 9))

txt4 = Label(main, text = "Result: ", font=('Helvetica', 9))
#Result option list
mb_r = OptionMenu(main, variable_r, *results )
mb_r.config(width=8, font=('Helvetica', 9))

def submit_info(): #first grab all information and prepare the call to the elo.py algorithm
    try: #try method to avoid any issue
        x = elo.calcular(int(variable.get()), int(E1.get()), int(E2.get()), float(variable_r.get()))
    
    except: #message in case of issue during the process
        messagebox.showerror("Warning!", "Invalid entry, take your time and read carefully the instructions")
    
    #conditionals to make the info better for user, they filter between positive and negative variations
    if x > int(E1.get()):
        messagebox.showinfo("ELO variation", E1.get()+" + "+ str(round(x-int(E1.get()), 1)) + " = "+ str(x))
        
    else:
        messagebox.showinfo("ELO variation", E1.get()+" - "+ str(round(int(E1.get())-x, 1)) + " = "+ str(x))

Submit = Button(main, text ="CALC", command = submit_info) #submit button

#pack content & show on screen
main.grid()
txt1.grid(row = 0, column = 0, sticky = W)
E1.grid(row = 0, column = 1, sticky = W)
txt2.grid(row = 1, column = 0, sticky = W)
E2.grid(row = 1, column = 1, sticky = W)
txt3.grid(row = 2, column = 0, sticky = W)
mb.grid(row = 2, column = 1, sticky = N)
txt4.grid(row = 3, column = 0, sticky = W)
mb_r.grid(row = 3, column = 1, sticky = N)

Submit.grid(row = 4, column = 1, sticky = E)
 
root.mainloop() #tkinter main loop