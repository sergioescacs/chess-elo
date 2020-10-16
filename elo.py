k = 40 #k constant 

print("Elo1: ") 
elo1 = input() #player 1 input

print("Elo2: ")
elo2 = input() #player 2 input

print("Result: ")
r = input() #result input, just will work with [1, 0, 0.5]

def calcular(k, elo1, elo2, result): #main function   
    ea = 1/(1+10**((int(elo2)-int(elo1))/400)) #theorically result, using probability and other mathmatics methods.
    
    new_elo = round(int(elo1)+(k*(int(result)-ea))) #final variation calculation the theorically result, the real result and the k constant.
    
    return new_elo #final ELO points

print(calcular(k, elo1, elo2, r)) #call function and print it