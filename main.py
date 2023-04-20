numero = int(input('digite um numero: '))
if numero <= 0:
    print('Número inválido')

else:
    i = 1
    primo = False
    for i in range(2,numero+1):
        primo = True
        if numero%i == 0 and numero != i : 
            primo = False
            break
    if primo:
        print('Primo')
    else:
        print('Não primo')