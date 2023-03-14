def bisiesto(year):
    if((year % 4 == 0)):
        if((year % 100 == 0)):
            return 'No es bisiesto'
        else:
            return 'Es bisiesto'
        
    elif((year % 400 == 0)):
            return 'Es bisiesto'
    else:
        return 'No es bisiesto'
    
year_user = input('Ingresa:\n>>> ')
year_user = int(year_user)


print(bisiesto(year_user))