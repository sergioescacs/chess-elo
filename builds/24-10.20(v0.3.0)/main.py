import elo
from tkinter import *
from tkinter import messagebox

root = Tk()

photo = PhotoImage(file = "xadrez.png") #set the future icon photo as a variable

#process the image and set it as the main icon of the app
root.iconphoto(False, photo)
root.title("ELO calc.")
root.resizable(False, False)

opt = ["k10", "k13", "k16", "k20", "k23", "k24", "k30", "k32", "k40"] #k constant option list
variable = StringVar(root)
variable.set(opt[0])

results = ["1", "0.5", "0"]#result option list
variable_r = StringVar(root)
variable_r.set(results[0])

#add Box variables 
all_entries = []
all_txt = []
all_mb = []
counter = 0

reference = {}

def process_dict(d):
    e = 0.0
        
    for x in d:
        e += float((d.get(x)).get())
    
    return e
    
def addEntry(): #addBox function
    global counter #counter variable
    global all_entries #all_entries array variable
    global all_txt
    global all_mb
    global reference
    
    if counter < 9: #first of all, check if we have not created more than 10 boxes
        
        txt_n = Label(main, text = "{}. ".format(str(counter+2)), font=('Helvetica', 9)) #crate txt object
        txt_n.grid(row = 4+counter, column = 0, sticky = W, padx = (5, 0) ) #show in screen txt object
        
        ent = Entry(main, bd = 3, width = 15) #create entry pbject
        ent.grid(row = 4+counter, column = 0, sticky = W, padx = (25, 0)) #show in screen entry object
        
        reference[counter] = StringVar(root) #create a section from dictionary with StringVar caract
        reference[counter].set(results[0]) #set default value
        
        r = OptionMenu(main, reference[counter], *results) #create optionMenu and set all variables
        r.config(width=4, font=('Helvetica', 9)) #Config optionMenu
        
        r.grid(row = 4+counter, column = 1, sticky = W, padx =(20, 20)) #show in screen new optionMenu

        all_entries.append(ent) #save entry into an array
        all_txt.append(txt_n) #save txt name into an array
        all_mb.append(r) #save optionmenu name into array
        
        counter += 1

def deleteEntry():
    global all_entries
    global all_txt
    global all_mb
    global counter
    global reference
    
    try:
        #modify all array 
        all_entries[len(all_entries)-1].destroy()
        del all_entries[len(all_entries)-1]
            
        all_txt[len(all_txt)-1].destroy()
        del all_txt[len(all_txt)-1]
            
        all_mb[len(all_mb)-1].destroy()
        del reference[int(len(all_mb)-1)]
        del all_mb[len(all_mb)-1]
        print(process_dict(reference))
        
        
        counter -= 1
    
    except:
        messagebox.showerror("Warning!", "No entries to delete!")
    
    #print(all_entries)

def submit_info(): #first grab all information and prepare the call to the elo.py algorithm
    
    data_r = process_dict(reference) + float(variable_r.get())
    data_ea = []
    
    for x in all_entries:
        data_ea.append(int(x.get()))
    
    data_ea.append(int(E2.get()))
    
    try: #try method to avoid any issue
        ea = elo.t_result(data_ea, int(E1.get()))
        x = elo.calcular(int((variable.get()).replace("k", "")), int(E1.get()), int(E2.get()), data_r, ea)
        
    except: #message in case of issue during the process
        messagebox.showerror("Warning!", "Invalid entry, take your time and read carefully the instructions")
    
    #conditionals to make the info better for user, they filter between positive and negative variations
    if x > int(E1.get()):
        messagebox.showinfo("ELO variation", "{} +  {}  = {}".format(E1.get(), str(round(x-int(E1.get()), 1)), str(x)))
        
    else:
        messagebox.showinfo("ELO variation", "{} - {} = {}".format(E1.get(), str(round(int(E1.get())-x, 1)), str(x)))

    data_r = 0.0
    
    
#Deploy Labels and various content as buttons and option lists
main = LabelFrame(root, text="Chess ELO app - beta v0.3.0", font=('Arial', 10, "bold"))
txt1 = Label(main, text = "Your ELO: ", font=('Helvetica', 9))
E1 = Entry(main, bd =3, width = 15)
txt2 = Label(main, text = "Your enemy's ELO: ", font=('Helvetica', 9))
E2 = Entry(main, bd =3, width = 15)
txt3 = Label(main, text = "1. ", font=('Helvetica', 9))

#K option list
mb = OptionMenu(main, variable, *opt )
mb.config(width=4, font=('Helvetica', 9))

#Result option list
mb_r = OptionMenu(main, variable_r, *results )
mb_r.config(width=4, font=('Helvetica', 9))

Submit = Button(main, text ="CALC", command = submit_info) #submit button
Add = Button(main, text ="ADD", command = addEntry) #add entry button
Del = Button(main, text = "DELETE", command = deleteEntry) #add Delete entry button

#pack content & show on screen
main.grid()
txt1.grid(row = 0, column = 0, sticky = W, padx = (10, 0))
Submit.grid(row = 0, column = 0, sticky = E)
Del.grid(row = 0, column = 1, sticky = E, padx = (55, 10))
Add.grid(row = 0, column = 1, sticky = W, padx = 15)

E1.grid(row = 1, column = 0, sticky = W, padx = (25, 0))
mb.grid(row = 1, column = 1, sticky = W, padx =(20, 20))
txt2.grid(row = 2, column = 0, sticky = W, padx = (10, 0))
txt3.grid(row = 3, column = 0, sticky = W, padx = (5, 0) )
E2.grid(row = 3, column = 0, sticky = W, padx = (25, 0))
mb_r.grid(row = 3, column = 1, sticky = W, padx =(20, 20))


root.mainloop() #tkinter main loop