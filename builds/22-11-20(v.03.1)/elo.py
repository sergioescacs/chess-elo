def calcular(k, elo1, elo2, result_a, ea): #main function that will process all information and return the final ELO rating
    return round(elo1+(k*(result_a-ea)), 1) #final variation calculation the theorically result, the real result and the k constant.

def t_result(array_r, elo1):
    ea = 0
    
    for x in array_r:
        ea_r = 1/(1+10**((x-elo1)/400)) #theorically result, using probability and other mathmatics methods.

        ea += ea_r
        
    return ea