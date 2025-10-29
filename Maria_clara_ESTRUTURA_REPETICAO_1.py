#Faça um programa que peça uma nota, entre zero e dez. 
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
#desenvolvido por: Maria Clara Marinho Torres

#int:numero inteiro/sem virgula
#input:leia
#print:escreva
valor = int(input("Informe uma nota entre 0 e 10: "))
#enquanto
while valor <0 or valor >10:
    print("valor inválido")
    valor = int(input("Informe uma nota entre 0 e 10: "))
print("Valor válido")
