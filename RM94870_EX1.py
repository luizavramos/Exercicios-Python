
tipo_de_assinatura = input("informe o tipo de assinatura: ")

tipo_de_assinatura = tipo_de_assinatura.upper()

s1 = "BASIC"
s2 = "SILVER"
s3 = "GOLD"
s4 = "PLATINUM"

faturamento_anual = float(input("informe o faturamento anual: "))

if tipo_de_assinatura == s1:
    bonus = faturamento_anual * 0.3
    print("O valor do bônus é {}".format(bonus))
elif tipo_de_assinatura == s2:
    bonus = faturamento_anual * 0.2
    print("O valor do bônus é {}".format(bonus))
elif tipo_de_assinatura == s3:
    bonus = faturamento_anual * 0.1
    print("O valor do bônus é {}".format(bonus))
elif tipo_de_assinatura == s4:
    bonus = faturamento_anual * 0.05
    print("O valor do bônus é {}".format(bonus))
else:
    print("Não foi encontrado este tipo de assinatura.")

# apenas para não fechar automaticamente no prompt de comando.
input(" ")