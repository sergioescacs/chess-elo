def calcular(k, elo1, elo2, result): #main function   
    ea = 1/(1+10**((int(elo2)-int(elo1))/400)) #theorically result, using probability and other mathmatics methods. 
    new_elo = round(int(elo1)+(k*(int(result)-ea))) #final variation calculation the theorically result, the real result and the k constant.
    
    return new_elo #final ELO points
