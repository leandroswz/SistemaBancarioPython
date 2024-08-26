menu = """
                    
[d] Depositar       
[s] Sacar           
[e] Extrato         
[q] Sair                                 
=> """

saldo = 0
limite = 500
saque = [] 
deposito = []
numero_saque = 0
LMITE_SAQUE = 3

while True:
    opcao=input(menu)
    
    if opcao == "d":
        print("Deposito")
        ndeposito=float(input("Digite o valor do deposito!"))
        if ndeposito >0:
            saldo+= ndeposito
            deposito.append(ndeposito) 
            extrato= f"Saque de R${saldo:1.2f}"
            print (f"Deposito efetuado com sucesso no valor de R${ndeposito:.2f}")
            
    elif opcao =="s":
        print("Sacar")
        nSaque=float(input("informe o valor do saque:"))
        if (numero_saque < LMITE_SAQUE) and (nSaque <= limite) and(nSaque <= saldo):
            saldo-=nSaque
            saque.append(nSaque)
            numero_saque += 1
            extrato= f"Saque de R${nSaque:1.2f}"
            print(extrato)
        else:
            print("Erro na operação!! Limite de saque diário atingido, ou saldo insuficiente!!")
    elif opcao == "e":
        print("_______Extrato_______\n")
        for i in saque:
            print(f"Saque de R${i:1.2f}")
        for i in deposito:
            print(f"Deposito de R${i:.2f}")
        print (f"Saldo R${saldo:.2f}")
    elif opcao == "q":
         break
    else:
        print("Operação invalida, por favor selecione uma opção valida!!")