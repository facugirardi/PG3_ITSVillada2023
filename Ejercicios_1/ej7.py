def step(nums):
    num = str(nums)
    if len(num) % 2 != 0:
        return False
 
    for i in range(0,len(num),2):
        if not (int(num[i:i+2][0])+1==int(num[i:i+2][1]) or int(num[i:i+2][0])-1==int(num[i:i+2][1])):
            return False
 
    return True
 
 
numero = input('Ingresa un numero:\n>>> ')

if step(numero):
    print ("Es un número STEP")
else:
    print ("No es un número STEP")
