menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
#caracterizar função depositar
    if opcao == "d":
        valor = float(input("Informe a quantia que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
#caracterizar função sacar
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        passou_saldo = valor > saldo

        passou_limite = valor > limite

        passou_saques = numero_saques >= LIMITE_SAQUES

        if passou_saldo:
            print("Operação falhou! saldo insuficiente.")

        elif passou_limite:
            print("Operação falhou! Seu limite é menor que o saque.")

        elif passou_saques:
            print("Operação falhou! Passou do limite diário.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! Valor inválido.")
#caracterizar função extrato
    elif opcao == "e":
        print("\n ________EXTRATO________")
        print("Nenhuma ação realizada." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
#caracterizar função sair
    elif opcao == "q":
        break

    else:
        print("Operação inválida, tente novamente.")