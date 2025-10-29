#Faça um programa que pergunte em que turno você estuda. Peça para digitar:
#M - Matutino
#V - Vespertino
#N - Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
#desenvolvido por: Maria Clara Marinho Torres 

#input:leia
#print:escreva
turno = input("Digite o turno: M,V ou N.")
#se
if turno=="M":
  print("Bom Dia!")
#senao se
elif turno=="V":
  print("Boa Tarde!")
#senao se
elif turno=="N":
  print("Boa noite!")
#senao
else:
  print("Valor Inválido!")