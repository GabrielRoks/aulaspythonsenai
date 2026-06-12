import op

def menu():
    opcoes = {
        "1": ("Soma", op.soma),
        "2": ("Subtração", op.sub),
        "3": ("Multiplicação", op.mult),
        "4": ("Divisão", op.div),
        "5": ("Potência", op.potencia),
        "6": ("Raiz Quadrada", op.raiz_quad),
        "7": ("Raiz Cúbica", op.raiz_cub),
        "8": ("Fatorial", op.fatorial),
        "9": ("Número Primo", op.primo),
        "10": ("Verificar Múltiplo", op.ismult),
        "11": ("Verificar Divisor", op.divisor),
        "12": ("MDC", op.mdc),
        "13": ("MMC", op.mmc),
        "14": ("Média", op.media),
        "15": ("Maior Número", op.maior),
        "16": ("Menor Número", op.menor),
        "17": ("Bhaskara", op.bhaskara),
        "18": ("Pitágoras", op.pitagoras)
    }

    while True:
        print("\n" + "=" * 40)
        print("           CALCULADORA")
        print("=" * 40)

        for chave, (nome, _) in opcoes.items():
            print(f"{chave:>2} - {nome}")

        print(" 0 - Sair")
        print("=" * 40)

        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            print("Encerrando programa...")
            break

        if escolha in opcoes:
            print("\n" + "-" * 40)

            try:
                resultado = opcoes[escolha][1]()
                print(f"Resultado: {resultado}")
            except Exception as erro:
                print(f"Erro: {erro}")

            print("-" * 40)
            input("Pressione ENTER para continuar...")
        else:
            print("Opção inválida!")
            input("Pressione ENTER para continuar...")


if __name__ == "__main__":
    menu()