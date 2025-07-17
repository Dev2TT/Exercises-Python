"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

valores=[]
for c in range(0,5):
    valor = int(input("Digite um valor: "))
    valores.append(valor)
print("$"*35)

def somaValores(lista):
   print(f"A soma dos valores é: {sum(lista)}")

def mediaValores(lista):
    print(f"A media dos valores dessa lista é: {sum(lista)/len(lista)}")


somaValores(valores)
mediaValores(valores)
