from unittest import result

from verify import verify_float, convert_float, verify_int, convert_int
import math

def soma():
    numero1 = input("Digite um número: ")
    numero2 = input('Digite outro número: ')
    if verify_float(numero1, numero2):
        num = convert_float(numero1, numero2)
        resultado = num[0] + num[1]
        return resultado
    else:
        return None

def sub():
    num1 = input("Digite um número: ")
    num2 = input("Digite outro número: ")
    if verify_float(num1, num2):
        number = convert_float(num1, num2)
        result = number[0] - number[1]
        return result
    else:
        return None

def mult():
    num1 = input("Digite um número: ")
    num2 = input("Digite outro número: ")
    if verify_float(num1, num2):
        number = convert_float(num1, num2)
        result = number[0] * number[1]
        return result
    else:
        return None
    
def div():
    num1 = input("Digite um número: ")
    num2 = input("Digite outro número: ")
    if num2 == 0:
        result = 'Não é possível dividir um número por 0'
        return result
    elif verify_float(num1, num2):
        number = convert_float(num1, num2)
        result = number[0] // number[1]
        return result
    else:
        return None
    
def potencia():
    num1 = input("Digite um número: ")
    num2 = input("Digite outro número: ")
    if num1 == '0':
        return 0
    elif num2 == '0':
        return 1
    elif verify_float(num1, num2):
        number = convert_float(num1, num2)
        result = number[0] ** number[1]
        return result
    else:
        return None
    
def raiz_quad():
    num = input("Digite um número: ")
    if verify_float(num):
        number = convert_float(num)
        result = math.sqrt(number)
        return result
    else:
        return None
    
def raiz_cub():
    num = input("Digite um número: ")
    if verify_float(num):
        number = convert_float(num)
        result = math.cbrt(number)
        return result
    else:
        return None
    
# def fatorial():
#     num = input("Digite um número: ")
#     if verify_float(num):
#         number = convert_float(num)
#         i = 0
#         ant = convert_float(num)
#         for i in number:
#             ant -= 1
#             if ant:
#                 result = number * ant
#             else:
#                 break
#             i += 1
#             return result
#     else:
#         return None
    
def primo():
    num = input("Digite um número: ")
    if verify_float(num):
        number = convert_float(num)
        # if number % :
        #     ...
        return result
    else:
        return None