def verificar_float_valido(valor: str) -> bool | float:
        # tenta converter a entrada para float
         
        try:
            valor_convertido = float(valor)
        except:
            print("Digite um número válido")
            return False

        # verifica se o valor digitado tem no máximo duas casas decimais
        # caso tenha mais não é uma representação válida de dinheiro
        casas = len(str(valor_convertido).split('.')[1])

        if casas > 2:
            print("Valores monetários devem ter até duas casas decimais. Tente novamente.")
            return  False

        return valor_convertido    

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[sd] Saldo
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao.lower() == "d":
        valor = input("Informe o valor do depósito: ")
        valor = verificar_float_valido(valor)

        if valor is False:
            continue
        else: 
            saldo += valor
            extrato += f"Operação: depósito. Valor: R$ {valor:.2f}\n"



    elif opcao.lower() == "s":

        if numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques excedido.")
            continue
        
        valor = input("Informe o valor do saque: ")

        # valida a entrada como valor mometário válido
        valor = verificar_float_valido(valor)

        if valor is False:
            continue


        if valor > saldo:
            print("Saldo insuficiente.")

        elif valor > limite:
            print("Valor do saque excede o limite.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Operação: saque. Valor: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Erro, o valor informado deve ser positivo.")

    elif opcao.lower() == "e":
        print("Extrato:")
        if extrato == "":
            print("Nao foram realizadas movimentações")
        else:
            print(extrato)

    elif opcao.lower() == "sd":
        print(f"Saldo: {saldo:.2f}")

    elif opcao.lower() == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")