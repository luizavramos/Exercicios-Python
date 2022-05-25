aux = 0
dia = 0

dias_da_semana = ['zero', 'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira']

for x in range(0, 5):
    entrada = input("Informe o número de votos de {}: ".format(dias_da_semana[x+1]))
    entrada = int(entrada)
    if entrada > aux:
        aux = entrada
        dia = x

diastr = ""

if dia == 0:
    diastr = "segunda-feira"
elif dia == 1:
    diastr = "terça-feira"
elif dia == 2:
    diastr = "quarta-feira"
elif dia == 3:
    diastr = "quinta-feira"
elif dia == 4:
    diastr = "sexta-feira"

print("O dia mais votado foi {}.".format(diastr))

# apenas para não fechar automaticamente no prompt de comando.
input(" ")
