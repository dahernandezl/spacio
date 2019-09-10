import random as rd

numeroSecreto = rd.randint(1,10)

print('hola mundo' + str(numeroSecreto))

numeroUsuario = input ('adivina el número ')

print('tu número es:' + str(numeroUsuario))

if int(numeroUsuario) == int(numeroSecreto):
    print('Ganaste :)')
else:
    print('Perdedor :(')
