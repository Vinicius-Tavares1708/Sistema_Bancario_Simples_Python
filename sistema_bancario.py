menu = '''
---MENU---
[d] Depositar
[s] Sacar
[e] Ver Extrato
[nu] Novo Usuário
[lc] Listar Contas
[nc] Nova Conta
[q] Sair
O que gostaria de fazer?
'''

saldo = 0

saques_diario = 0
LIMITE_SAQUE_DIARIO = 3
LIMITE_VALOR_SAQUE = 500

extrato = []

usuarios = []
contas = []
AGENCIA = "0001"

def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
            saldo += deposito
            print("Valor depositado com sucesso")
            novo_extrato = f"Deposito: R${deposito:.2f}"
            extrato.append(novo_extrato)

    else:
        print("Valor do deposito precisa ser maior que R$0.00")

    return saldo

def sacar(*, saldo, saque, extrato, limite_valor, saque_dia):
    if saque > limite_valor:
                print("O limite de saque é R$500.00")

    else:
        if saque <= saldo:
            saldo -= saque
            print("Saque realizado com sucesso")
            saque_dia += 1
            novo_extrato = f"Saque: R${saque:.2f}"
            extrato.append(novo_extrato)
    
        else:
            print("Saldo insuficiente")

    return saldo, saque_dia

def ver_extrato(saldo, /, *, extrato):
    if not extrato:
           print("Ainda não foi feita nenhuma movimentação")

    else:
        print("---Seu Extrato---")
        for i, movimentacao in enumerate(extrato, 1):
            print(f"{i}. {movimentacao}\n")
        print(f"Seu saldo: R${saldo:.2f}")
        print("---------------------")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)
     
    if usuario:
        print("Já existe usuário com esse CPF")
        return
          
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({'nome':nome, 'cpf':cpf, 'data_nascimento':data_nascimento, 'endereco': endereco})
    print("Usuário criado com sucesso")

def filtrar_usuarios(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios
        if usuario['cpf'] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {'agencia':agencia, 'numero_conta':numero_conta, 'usuario':usuario}
    
    print("USUÁRIO NÃO ENCONTRADO")

def mostar_contas(contas):
    if not contas:
          print("Nenhuma conta cadastrada")

    else:
        for conta in contas:
           print(f'''
Agência: {conta['agencia']}
Conta: {conta['numero_conta']}
Titular: {conta['usuario']['nome']}
                ''')

while True:

    opcao = str(input(menu)).lower()

    if opcao == "d":
        deposito = float(input("Digite o valor que deseja depositar: R$"))
        saldo = depositar(saldo, deposito, extrato)
        
    elif opcao == "s":
        if saques_diario < LIMITE_SAQUE_DIARIO:
            saque = float(input("Digite o valor deseja sacar? R$"))
            saldo, saques_diario = sacar(
                 saldo = saldo,
                 saque = saque,
                 extrato = extrato,
                 saque_dia = saques_diario,
                 limite_valor = LIMITE_VALOR_SAQUE,
            )
        else:
            print("Você já excedeu a quantidade de saques diários que pode fazer")
            
    elif opcao == "e":
        ver_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        criar_usuario(usuarios)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)
        print("---------------------")

    elif opcao == "lc":
         mostar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("Opção inválida. Digite alguma opção do menu.")