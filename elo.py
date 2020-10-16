k = 40

print("Elo1: ")
elo1 = input()

print("Elo2: ")
elo2 = input()

print("Result: ")
r = input()

def calcular(k, elo1, elo2, result):   
    ea = 1/(1+10**((int(elo2)-int(elo1))/400))
    
    new_elo = round(int(elo1)+(k*(int(result)-ea)))
    
    return new_elo

print(calcular(k, elo1, elo2, r))