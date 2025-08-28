import datetime


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("""
          =============================
          BEM VINDO AO SISTEMA BANCARIO

          [1] DEPOSITAR
          [2] SACAR
          [3] EXTRATO
          [4] SAIR
          =============================
          """)
    opcao = int(input('Digite a operação que deseja realizar [1 a 4]: '))

    if opcao == 1:
        valor_deposito = float(input('Valor do deposito: R$ '))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"\nDeposito de R${valor_deposito:.2f} realizado em: {datetime.datetime.now().replace(microsecond=0)}"
            print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso!")

        else:
            print("Valor invalido, digite um numero positivo")

    elif opcao == 2:
        valor_saque = float(input("Digite o valor do seu saque R$ "))
        excedeu_limite = valor_saque > limite
        excedeu_numero_saques = numero_saques >= LIMITE_SAQUES
        excedeu_saldo = valor_saque > saldo
        
        if excedeu_limite:
            print(f"\nOperação invalida, excedeu o valor limite de R${limite:.2f}.")

        elif excedeu_numero_saques:
            print(f"\nOperação invalida, excedeu o numero de saques diarios de {LIMITE_SAQUES}.")

        elif excedeu_saldo:
            print(f"\nVocê não tem saldo para essa operação.")

        elif valor_saque > 0:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"\nSaque de R${valor_saque:.2f} realizado em: {datetime.datetime.now().replace(microsecond=0)}"
            print(f"Operação realizada com sucesso, você sacou R${valor_saque:.2f}")

    elif opcao == 3:
        extrato += f"\nSaldo final de R${saldo:.2f} em: {datetime.datetime.now().replace(microsecond=0)}"
        print("\n#######EXTRATO#######")
        print(extrato)
        print("\n#####################")

    elif opcao == 4:
        print("Obrigado por usar o nosso sistema, até a próxima!")
        break
    
    else:
        print("Operação Invalida! Digite uma opção valida entre 1 e 4")




    




