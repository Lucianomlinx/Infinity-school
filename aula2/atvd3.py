#Atividade 03:
#Verificação de Maioridade e Habilitação:
#Crie um programa que peça a idade do usuário e se ele possui habilitação
#(sim ou não). Use operadores lógicos para verificar se ele é maior de idade
#(>= 18) e possui habilitação.

idade = int(input("Forneça sua idade."))
hab = str(input("digite S para se  for habilitado e N para não:"))

print(idade>=18 and hab=="S")