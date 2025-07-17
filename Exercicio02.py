"""
Faça um programa que leia 5 números e informe o maior número.

"""

def maximoValor():
    valores=[]
    for i in range(0,5):
        valor =int(input("Informe o valor: "))
        valores.append(valor)
    valores.sort(reverse=True)
    print(f"O maior valor digitado foi: {valores[0]}")

maximoValor()

    