def step(nums):
    num = str(nums)
    if len(num) % 2 != 0:
        return False
 
    for i in range(0, len(num)-1, 2):
        digito1 = int(num[i])
        digito2 = int(num[i+1])
        if abs(digito1 - digito2) != 1:
            return False
    
    return True
 
 
numero = input('Ingresa un numero:\n>>> ')

if step(numero):
    print ("Es un número STEP")
else:
    print ("No es un número STEP")
