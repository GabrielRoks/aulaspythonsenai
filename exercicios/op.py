from verify import verify_float, convert_float
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
    if num2 == "0":
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
    try:
        num = float(num)
        if num < 0:
            return 'Valor inválido'
        result = f'{math.sqrt(num):.2f}'
        return result
    except (ValueError, TypeError):
        return 'Valor inválido'
    
def raiz_cub():
    num = input("Digite um número: ")
    try:
        num = float(num)
        result = f'{math.cbrt(num):.2f}'
        return result
    except (ValueError, TypeError):
        return 'Valor inválido'

def fatorial():
    num = input("Digite um número: ")
    result = 1
    if num.isdigit():
        num = int(num)
        while num >= 1:
            result = result * num
            num -= 1
        return result
    else:
        return "Valor inválido"
    
def primo():
    num = input("Digite um número: ")
    if num.isdigit():
        num = int(num)
        if num < 2:
            return "Não é primo"
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return "Não é primo"
        return "Número é primo"

def decisao(x, y, num, num2):
    if num.isdigit() and num2.isdigit():
        result = int(num) % int(num2) == 0
        if result:
            return x
        return y
    return "Valor inválido"

def ismult():
    num1 = input("Digite um número: ")
    num2 = input("Digite outro número: ")
    lista = [num1, num2]
    mult = f'{lista[0]} é multiplo de {lista[1]}'
    nao_mult = f'{lista[0]} não é multiplo de {lista[1]}'
    return decisao(mult, nao_mult, lista[0], lista[1])

def divisor():
    num1 = input("Digite um número: ")
    num2 = input("Digite outro número: ")
    lista = [num1, num2]
    divisao = f'{lista[1]} é divisor de {lista[0]}'
    nao_divisor = f'{lista[1]} não é divisor de {lista[0]}'
    return decisao(divisao, nao_divisor, lista[0], lista[1])

def mdc():
    num1 = input("Digite um número: ")
    num2 = input("Digite outro número: ")
    lista = [num1, num2]
    if lista[0].isdigit() and lista[1].isdigit():
        numero_1 = int(lista[0])
        numero_2 = int(lista[1])
        while numero_2 != 0:
            resto = numero_1 % numero_2
            numero_1 = numero_2
            numero_2 = resto
        return f'O mdc é {numero_1}'
    return "Valor inválido"

def mdc_int(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def mmc():
    num1 = input("Digite um número: ")
    num2 = input("Digite outro número: ")

    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        result = (num1 * num2) // mdc_int(num1, num2)
        return f'O resultado do mmc de {num1} e {num2} é: {result}'
    return "Dados inválidos"

def media():
    i = 0
    med = 0
    while True:
        nota = input("Digite uma nota: ")
        if nota == '':
            if i == 0: 
                return 'Média 0.0'
            med = med / i
            return f'A média foi {med:.2f}'
        try:
            nota = float(nota)
            med += nota
            i += 1
        except (ValueError, TypeError):
            return 'Valores inválidos'
        
def valor(x, z, y, msg1, msg2):
    if z == y:
        return f'{z} e {y} possuem o mesmo valor'
    if x == '>':
        return msg1 if z > y else msg2
    if x == '<':
        return msg1 if z < y else msg2
    return msg2

def maior():
    num1 = input("Digite um número: ")
    num2 = input("Digite outro número: ")

    try:
        z, y = convert_float(num1, num2)

        msg1 = f'{z} é maior que {y}'
        msg2 = f'{y} é maior que {z}'
        return valor(">", z, y, msg1, msg2)
    except (ValueError, TypeError):
        return 'Valores inválidos'
def menor():
    num1 = input("Digite um número: ")
    num2 = input("Digite outro número: ")
    try:
        z, y = convert_float(num1, num2)
        msg1 = f'{z} é menor que {y}'
        msg2 = f'{y} é menor que {z}'
        resp = valor("<", z, y, msg1, msg2)
        return resp
    except (ValueError, TypeError):
        return 'Valores inválidos'

def bhaskara():
    a = input("Digite o valor de a: ")
    b = input("Digite o valor de b: ")
    c = input("Digite o valor de c: ")

    try:
        a1, b1, c1 = float(a), float(b), float(c)
        ra = (b1**2) - (4 * a1 * c1)
        if a1 == 0:
            return '"A" não pode ser 0'
        if ra < 0:
            return 'Raiz negativa'
        x1 = (-b1 + math.sqrt(ra)) / (2 * a1)
        x2 = (-b1 - math.sqrt(ra)) / (2 * a1)
        return f'x1 = {x1} e x2 = {x2}'
    except(ValueError, TypeError):
        return 'Valores inválidos'

def pitagoras():
    print("----------Pitágoras-----------\n"
        "1 - Possui o valor dos dois catetos\n"
        "2 - Possui 1 cateto e a hipotenusa\n"
        "3 - Calcular usando o seno\n"
        "4 - Calcular usando o cosseno\n"
        "5 - Calcular usando a tangente\n")
    opcao = input("Digite um das opçoes: ")
    if opcao == '1':
        try:
            ca = float(input('Digite o valor do primeiro cateto: '))
            co = float(input('Digite o valor do segundo cateto: '))
            result = math.sqrt(ca**2 + co**2)
            return f"O valor da hipotenusa é {result:.2f}"
        except (TypeError, ValueError):
            return 'Valores inválidos'
        
    elif opcao == "2":
        try:
            co = float(input("Digite o valor do cateto: "))
            h = float(input("Digite o valor da hipotenusa: "))
            if h <= co:
                return 'A hipotenusa deve ser maior que o cateto'
            resultado = math.sqrt(h**2 - co**2)
            return f"O valor do cateto é {resultado}"  
        except (ValueError, TypeError):
            return "Valores inválidos"
        
    elif opcao == '3':
        try:
            co = float(input('Digite o valor do cateto oposto: '))
            ang = input('Digite o ângulo (30, 45 ou 60): ')
            match ang:
                case '30':
                    x = 1 / 2
                case '45':
                    x = math.sqrt(2) / 2
                case '60':
                    x = math.sqrt(3) / 2
                case _:
                    return "Valor inválido"
            result = co / x
            return f'O valor da hipotenusa é {result:.2f}'
        except(ValueError, TypeError):
            return "Valores inválidos"
        
        
    elif opcao == '4':
        try:
            ca = float(input('Digite o valor do cateto adjacente: '))
            ang = input('Digite o ângulo (30, 45 ou 60): ')
            match ang:
                case '30':
                    x = math.sqrt(3) / 2
                case '45':
                    x = math.sqrt(2) / 2
                case '60':
                    x = 1 / 2
                case _:
                    return "Valor inválido"
            result = ca / x
            return f'O valor da hipotenusa é {result:.2f}'
        except(ValueError, TypeError):
            return "Valores inválidos"
    
    elif opcao == '5':
        try:
            ca = float(input('Digite o valor do cateto adjacente: '))
            ang = input('Digite o ângulo (30, 45 ou 60): ')
            match ang:
                case '30':
                    x = math.sqrt(3) / 3
                case '45':
                    x = 1
                case '60':
                    x = math.sqrt(3)
                case _:
                    return "Valor inválido"
            result = ca * x
            return f'O valor do cateto oposto é {result:.2f}'
        except(ValueError, TypeError):
            return "Valores inválidos"
    