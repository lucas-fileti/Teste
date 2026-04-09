git --version
saldo = 0
registro = []

while True:
    print("\n ---Menu---")
    print("\n1 - Entradas")
    print("2 - Saidas")
    print("3 - Saldo")
    print("4 - Registro")
    print("5 - Sair")
    opcao = input("\nEscolha").strip()

    if opcao == "1":
        valor = float(input("Quanto que adicionar? "))
        saldo += valor 
        print("Valor adicionado !!!")
        registro.append(f"+{valor}")

    elif opcao == "2":
        valor  = float(input("Quanto gastou ?"))
        saldo -= valor
        print("Gasto registrado !!!")
        registro.append(f"-{valor}")

    elif opcao == "3":
        print(f"Saldo R${saldo}")

    elif opcao == "4":
        print("registro:")

        total = 0

        for item in registro:   
            print(item)
            total += float(item)

        print(f"\nTotal Movimentado: R${total}")
    elif opcao == "5":
        print("Saindo...")
        break
    
    else: 
        print("escolha invalida")

