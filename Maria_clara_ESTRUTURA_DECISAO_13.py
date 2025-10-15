#Faça um programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
#desenvolvido por: Maria Clara Marinho Torres 

semana = input("Qual número da semana?(1 a 7).")
#se
if semana=="1":
  print("Domingo")
#senao se
elif semana=="2":
  print("Segunda-Feira")
#senao se
elif semana=="3":
  print("Terça-feira")
#senao se
elif semana=="4":
  print("Quarta-Feira")
#senao se
elif semana=="5":
  print("Quinta-Feira")
#senao se
elif semana=="6":
  print("Sexta-Feira")
#senao se
elif semana=="7":
  print("Sabádo")
#senao
else:
  print("Valor Inválido!")