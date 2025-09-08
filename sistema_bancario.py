menu = '''
---MENU---
[d] Depositar
[s] Sacar
[e] Ver extrato
[q] Sair
O que gostaria de fazer?
'''

saldo = 0
saques_diario = 0
LIMITE_SAQUE = 500
extrato = []

while True:

    opcao = str(input(menu)).lower()

    if opcao == "d":
        deposito = float(input("Digite o valor que deseja depositar: R$"))
        if deposito > 0:
            saldo += deposito
            print("Valor depositado com sucesso")
            novo_extrato = f"Deposito: R${deposito:.2f}"
            extrato.append(novo_extrato)

        else:
            print("Deposito precisa ser maior que R$0.00")

    elif opcao == "s":
        if saques_diario < 3:
            saque = float(input("Digite o valor deseja sacar? R$"))
            if saque > 500:
                print("O limite de saque é R$500.00")

            else:
                if saque <= saldo:
                    saldo -= saque
                    print("Saque realizado com sucesso")
                    saques_diario += 1
                    novo_extrato = f"Saque: R${saque:.2f}"
                    extrato.append(novo_extrato)
                else:
                    print("Saldo insuficiente")

        else:
            print("Você já excedeu a quantidade de saques diários que pode fazer")

    elif opcao == "e":
       
        if not extrato:
           print("Ainda não foi feita nenhuma movimentação")

        else:
            print("---Seu Extrato---")
            for i, movimentacao in enumerate(extrato, 1):
                print(f"{i}. {movimentacao}\n")
            print(f"Seu saldo: R${saldo:.2f}")
            print("---------------------")

    elif opcao == "q":
        break

    else:
        print("Opção inválida. Digite alguma opção do menu.")