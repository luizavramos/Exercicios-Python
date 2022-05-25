minutos = int(input("Informe os minutos que a máquina está marcando: "))

fatorial = 1
for x in range(minutos, 1, -1):
    fatorial *= x


print("A senha é LIBERDADE{}".format(fatorial))

# apenas para não fechar automaticamente no prompt de comando.
input(" ")
