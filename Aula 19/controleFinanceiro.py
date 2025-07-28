from transacao import Transacao

""" movimentacao1 =  Transacao("Sálario de 07/2025", 2000.0, "Receita")
movimentacao2 =  Transacao("Conta de Luz de 07/2025", 200.0,"Despesa")

print(movimentacao1)
print(movimentacao2) """

descricao = input("Forneça uma descricricao da nova transação:")
valor = input("Informe o valor da transação:")
tipo = input ("Tipo da transação:")

movimentacao3 = Transacao (descrição,valor,tipo)

print(movimentacao3)
