print('Calculadora Basica')

num1 = float(input('Ingrese el primer numero: '))
num2 = float(input('Ingrese el segundo numero: '))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
try:
    division = num1 / num2
except ZeroDivisionError:
    print('No se puede dividir por cero')

print(f'El resultado de la suma es: {suma}')
print(f'El resultado de la resta es: {resta}')
print(f'El resultado de la multiplicacion es: {multiplicacion}')
print(f'El resultado de la division es: {division}')