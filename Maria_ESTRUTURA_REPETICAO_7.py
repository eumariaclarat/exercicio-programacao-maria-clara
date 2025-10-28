#Faça um programa que leia 5 números e informe o maior número.
#desenvolvido por: Maria Clara Marinho Torres
maior=-99
#para
#intervalo
for x in range(1,6):
  numero=int(input("Informe um número:"))

  #se
  if numero>maior:
    maior = numero

print("o número maior é o:",maior)
