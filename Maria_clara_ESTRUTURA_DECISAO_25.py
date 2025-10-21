#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
#Caso contrário, ele será classificado como "Inocente".
#desenvolvido por: Maria Clara Marinho Torres
crime = 0
respostas= input("Telefonou para a vítima?")
#se
if respostas == "sim":
  crime = crime + 1
  
respostas = input("Esteve no local do crime?")
if respostas == "sim":
  crime = crime + 1

respostas = input("Mora perto da vítima?")
if respostas == "sim":
  crime = crime + 1

respostas = input("Devia para a vítima?")
if respostas == "sim":
  crime = crime + 1

respostas = input("Já trabalhou com a vítima?")
if respostas == "sim":
  crime = crime + 1



#se
if crime<=2:
  print("Suspeita")
#senao se
elif crime<=3:
  print("Cúmplice")
#senao se
elif crime>=5:
  print("Assassino")
#senao
else:
  print("Inocente")