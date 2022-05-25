soma_impar = 0.0
soma_par = 0.0

for y in range(1, 50, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.")
    nota_impar = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}. ".format(y)))
    soma_impar = soma_impar + nota_impar

media_impar = soma_impar / 25

for x in range(2, 51, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.")
    nota_par = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}. ".format(x)))
    soma_par = soma_par + nota_par

media_par = soma_par / 25

print("A média da turma par é {} e a média da turma ímpar é {}.".format(media_par, media_impar))

if media_par > media_impar:
    print("A média da turma par é maior.")
else:
    print("A média da turma ímpar é maior.")

# apenas para não fechar automaticamente no prompt de comando.
input(" ")
