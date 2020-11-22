import elo
from tkinter import *
from tkinter import messagebox

class Constructor: #Main builder class where extra-buttons and labels will be created
    def __init__(self, master, main, k_list, results, counter):
        #Various variables from the App class
        self.reference = {}
        self.master = master
        self.main = main
        self.k_list = k_list
        self.results = results
        self.counter = counter
        
        self.reference[self.counter] = StringVar(self.master) #create a section from dictionary with StringVar caract
        self.reference[self.counter].set(self.results[0]) #set default value
        
        self.txt_n = Label(self.main, text = "{}. ".format(str(self.counter+2)), font=('Helvetica', 9)) #crate txt object
        self.txt_n.grid(row = 4+counter, column = 0, sticky = W, padx = (5, 0) ) #show in screen txt object
        
        self.ent = Entry(self.main, bd = 3, width = 15) #create entry pbject
        self.ent.grid(row = 4+self.counter, column = 0, sticky = W, padx = (25, 0)) #show in screen entry object
        
        self.r = OptionMenu(self.main, self.reference[self.counter], *self.results) #create optionMenu and set all variables
        self.r.config(width=4, font=('Helvetica', 9)) #Config optionMenu
        self.r.grid(row = 4+self.counter, column = 1, sticky = W, padx =(20, 20)) #show in screen new optionMenu    
        
    def get_info(self): #Function where all data will be processed
        e = 0.0
                
        for x in self.reference:
            e += float((self.reference.get(x)).get())
            
        return self.ent.get(), e
    
    def __del__(self):
        self.txt_n.destroy() #Destroy number[x] label
        self.ent.destroy() #Destroy entry[x] 
        self.r.destroy() #Destroy k-box[x]

    
class App: #Main class where the functions will be implemented.      
    def __init__(self, master):
        #Main variables
        global counter
        global pre_fab
        pre_fab, counter = [], 0
        
        k_list = ["k10", "k13", "k16", "k20", "k23", "k24", "k30", "k32", "k40"] #k constant option list
        variable = StringVar(master)
        variable.set(k_list[0])

        results = ["1", "0.5", "0"]#result option list
        variable_r = StringVar(master)
        variable_r.set(results[0])
        
        # Generate Main Frame
        main = LabelFrame(master, text="Chess ELO app - beta v0.3.1", font=('Arial', 10, "bold"))
        
        #Main sub-functions
        def submit_info(): #submit button on-Click
            punct = 0
            data_ea = []
            
            for x in pre_fab:
                punct += x.get_info()[1]
                data_ea.append(int(x.get_info()[0]))

            data_r = float(punct) + float(variable_r.get())
            data_ea.append(int(E2.get()))

            try: #try method to avoid any issue
                ea = elo.t_result(data_ea, int(E1.get()))
                y = elo.calcular(int((variable.get()).replace("k", "")), int(E1.get()), data_r, ea)
                
            except Exception as e: #message in case of issue during the process
                print(e)
                messagebox.showerror("Warning!", "Invalid entry, take your time and read carefully the instructions")
            
            #conditionals to make the info better for user, they filter between positive and negative variations
            if y > int(E1.get()):
                messagebox.showinfo("ELO variation", "{} +  {}  = {}".format(E1.get(), str(round(y-int(E1.get()), 1)), str(y)))
                
            else:
                messagebox.showinfo("ELO variation", "{} - {} = {}".format(E1.get(), str(round(int(E1.get())-y, 1)), str(y)))

            data_r = 0.0
                    
        def addEntry(): #on-Click function, add Entry button. 
            global counter
            global pre_fab
            
            if counter < 9:
                pre_fab.append(Constructor(master, main, k_list, results, counter))
                counter += 1
             
            else:
                messagebox.showerror("Warning!", "You can not add more Labels.")
        
        def deleteEntry(): #on-Click function, delete Entry button. 
            global counter
            global pre_fab
            
            try:
                del pre_fab[counter-1] 
                counter -= 1
            
            except:
                messagebox.showerror("Warning!", "No entries to delete!")
            
        #Start building widgets
        txt1 = Label(main, text = "Your ELO: ", font=('Helvetica', 9))
        E1 = Entry(main, bd =3, width = 15)
        txt2 = Label(main, text = "Your enemy's ELO: ", font=('Helvetica', 9))
        E2 = Entry(main, bd =3, width = 15)
        txt3 = Label(main, text = "1. ", font=('Helvetica', 9))

            #K option list
        mb = OptionMenu(main, variable, *k_list )
        mb.config(width=4, font=('Helvetica', 9))

            #Result option list
        mb_r = OptionMenu(main, variable_r, *results )
        mb_r.config(width=4, font=('Helvetica', 9))

        Submit = Button(main, text ="CALC", command = submit_info) #submit button
        Add = Button(main, text ="ADD", command = addEntry) #add entry button
        Del = Button(main, text = "DELETE", command = deleteEntry) #add Delete entry button
        
        #Final screen deploy
        main.grid()
        txt1.grid(row = 0, column = 0, sticky = W, padx = (10, 0))
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

#Main function where all actions are coordinated 
def main():
    root = Tk() #Init of the main loop

    photo = PhotoImage(file = "xadrez.png") #set ico as a variable

    root.iconphoto(False, photo)
    root.title("ELO calc.") #Set window title
    root.resizable(False, False) #window none resizable

    Window_Base = App(root) #Deploying of the main items

    root.mainloop()

#Where the software starts
if __name__ == '__main__':
    main()