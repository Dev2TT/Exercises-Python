"""
Faça um programa que 
imprima na tela os números de 1 a 20, um abaixo do outro.
 Depois modifique o programa para que ele mostre os números um ao lado do outro.
"""

def mostrarValor():
    lista=[]
    print("Um abaixo do Outro")
    for i in range(0,21):
        print(i)
        lista.append(i)
    print("-="*35)
    print("Um ao lado do outro")
    print(lista)

mostrarValor()
