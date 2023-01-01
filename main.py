
m = float(input('Seu peso em KG:'))
a = float(input('Sua altura em M(FAVOR USAR . EM VEZ DE ,):'))
nm = input('Valeu! Mas qual seu nome?')
imc = float((m / (a ** 2)))
limited_imc = round(imc, 2)
print("Ok, {} de acordo com meus calculo seu imc é {}.".format(nm, limited_imc))

if (limited_imc >= 18.5 and limited_imc < 25):
    print("{}, você está com seu peso normal!".format(nm))

elif (limited_imc < 18.5):
    print("Você está abaixo do peso.")

elif (limited_imc > 24.9 and limited_imc < 30):
    print("Você está com sobrepeso.")

elif (limited_imc > 29.9 and limited_imc < 35):
    print("{}. Você sofre de obesidade grau 1.".format(nm))

elif (limited_imc > 34.9 and limited_imc < 40):
    print("{}. Você sofre de obesidade grau 2.".format(nm))

elif (limited_imc > 40):
    print("{}. Você sofre de obesidade morbida.".format(nm))
