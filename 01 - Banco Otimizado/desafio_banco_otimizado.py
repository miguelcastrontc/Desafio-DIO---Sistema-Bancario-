from datetime import datetime
import textwrap

#Tratamento data e hora
data_e_hora = datetime.now()
data_e_hora_formatada = data_e_hora.strftime("%d/%m/%Y %H:%M:%S")

def menu():
    menu = """
=====Bem vindo=====
[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar Usuário
[a] Criar Conta
[u] Listar Contas
[q] Sair
===================
>
"""
    return input(textwrap.dedent(menu))

def operacao_deposito(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"{data_e_hora_formatada} - Depósito: R$ {valor:.2f}\n"
        print(f"{data_e_hora_formatada} - Depósito de R$ {valor:.2f} realizado com sucesso! ")

    else:
        print("Valor invalido ")
    
    return saldo, extrato

def operacao_saque(*, saldo, valor, limite, extrato, numero_transacoes, LIMITE_SAQUES):

    if numero_transacoes >= LIMITE_SAQUES:
        print("Limite de saques diários atingido! ")

    elif valor > saldo:
        print("Saldo insuficiente! ")

    elif valor > limite:
        print("Limite de saque insuficiente! ")

    elif valor > 0:
        saldo -= valor
        extrato += f"{data_e_hora_formatada} - Saque: R$ {valor:.2f}\n"
        numero_transacoes += 1
        print(f"{data_e_hora_formatada} - Saque de R$ {valor:.2f} realizado com sucesso! ")

    else:
        print("Valor invalido ")

    return saldo, extrato, numero_transacoes

def consultar_extrato(saldo, /, *, extrato):
    print("\n=================EXTRATO=================")
    print(extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("===========================================")

def verificar_usuario(lista_usuarios, cpf):
    for usuario in lista_usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def cadastrar_usuario(lista_usuarios):
    cpf = int(input("Informe o CPF do usuário: "))

    if verificar_usuario(lista_usuarios, cpf):
        print("\n=====Usuário já cadastrado!=====")
        return

    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento do usuário (DD/MM/AAAA): ")
    endereco = input("Informe o endereço do usuário: ")
    lista_usuarios.append({"nome": nome, "data de nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print(f"\n=====Usuário {nome} cadastrado com sucesso!=====")


def criar_conta(agencia, numero_conta, lista_usuarios):
    cpf = int(input("Informe o CPF do usuário: "))
    usuario = verificar_usuario(lista_usuarios, cpf)

    if not usuario:
        print("\n=====Usuário não encontrado!=====")
        return

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    print(f"\n=====Conta criada com sucesso!=====")
    return conta

def listar_contas(lista_contas):
    if not lista_contas:
        print("\n=====Nenhuma conta cadastrada!=====")
        return

    print("\n=====Contas Cadastradas=====")
    for conta in lista_contas:
        print(f"\nAgência: {conta['agencia']} \nNúmero da Conta: {conta['numero_conta']} \nUsuário: {conta['usuario']['nome']}")
    print("===============================")

def main():
    
    AGENCIA = "0061"
    LIMITE_SAQUES = 10
    saldo = 0
    limite = 500
    extrato = ""
    numero_transacoes = 0
    lista_usuarios = []
    lista_contas = []

    while True:
        opcao = menu()

        if opcao == "d":

            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = operacao_deposito(saldo, valor, extrato)

        elif opcao == "s":

            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_transacoes = operacao_saque(
                saldo=saldo,
                valor=valor,
                limite=limite,
                extrato=extrato,
                numero_transacoes=numero_transacoes,
                LIMITE_SAQUES=LIMITE_SAQUES
            )

        elif opcao == "e":
            consultar_extrato(saldo, extrato=extrato)

        elif opcao == "c":
            cadastrar_usuario(lista_usuarios)

        elif opcao == "a":
            numero_conta = len(lista_contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, lista_usuarios)

            if conta:
                lista_contas.append(conta)

        elif opcao == "u":
            listar_contas(lista_contas)

        elif opcao == "q":
            break
        
        else:
            print("Operação falhou! O valor informado é inválido.")

main()