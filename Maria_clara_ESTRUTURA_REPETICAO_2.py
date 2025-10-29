#Faça um programa que leia um nome de usuário.
#E a sua senha e não aceite a senha igual ao nome do usuário.
#Mostrando uma mensagem de erro e voltando a pedir as informações.
#desenvolvido por: Maria Clara Marinho Torres

#input:leia
#print:escreva
nome = input("Informe seu nome: ")
senha = input("Informe sua senha: ")
#while:enquanto
while nome == senha:
    print("Sua senha não pode ser seu nome.")
    print("Por favor, informe novamente seu nome e sua senha!")

    nome = input("Informe seu nome: ")
    senha = input("Informe sua senha: ")

print("Oie,", nome, "sua senha está segura ! :)")