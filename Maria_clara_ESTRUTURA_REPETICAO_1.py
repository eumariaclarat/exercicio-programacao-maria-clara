#Faça um programa que peça uma nota, entre zero e dez. 
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
#desenvolvido por: Maria Clara Marinho Torres


valor = int(input("Informe uma nota entre 0 e 10: "))
while valor <0 or valor >10:
    print("valor inválido")
    valor = int(input("Informe uma nota entre 0 e 10: "))
print("Valor válido")