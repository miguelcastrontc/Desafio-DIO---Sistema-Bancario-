menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = str(input(menu))

    if opcao == "d":
        valor = float(input("Por favor, informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

            print(f"Deposito de R$ {valor:.2f} realizado com suceso! ")

        else:
            print("Valor invalido ")

    elif opcao == "s":
         valor = float(input("Por favor, informe o valor do saque: ")) 

         if valor > saldo:
            print("Saldo inuficiente ")

         elif valor > limite:
            print("Limite inuficiente ")
        
         elif numero_saques >= LIMITE_SAQUES:
            print("Saques maximos diaros atingido! ")

         elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso! ")

         else:
            print("Valor invalido ")

    elif opcao == "e":
        print("\n=================EXTRATO=================")
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("===========================================")

    elif opcao == "q":

        print("========Obrigado por usar nosso banco!========")

        break
        
    else:
            print("Operação falhou! O valor informado é inválido.")