# solicitando o valor de bpm e idade
bpm = int(input("Informe o número de bpm:"))

idade = int(input("Informe a sua idade:"))

# desvios condicionais para até 2 anos:

if idade <= 2 and 120 <= bpm <= 140:
    print("Os batimentos estão dentro da faixa adequada")

elif idade <= 2 and bpm < 120:
    print("Os batimentos estão abaixo da faixa adequada")

elif idade <= 2 and bpm > 140:
    print("Os batimentos estão acima da faixa adequada")

# desvios condicionais para crianças de 8 a 17 anos:

elif 8 <= idade <= 17 and 80 <= bpm <= 100:
    print("Os batimentos estão dentro da faixa adequada")

elif 8 <= idade <= 17 and bpm < 80:
    print("Os batimentos estão abaixo da faixa adequada")

elif 8 <= idade <= 17 and bpm > 100:
    print("Os batimentos estão acima da faixa adequada")

# desvios condicionais para adultos

elif 18 <= idade <= 60 and 70 <= bpm <= 80:
    print("Os batimentos estão dentro da faixa adequada")

elif 18 <= idade <= 60 and bpm < 70:
    print("Os batimentos estão abaixo da faixa adequada")

elif 18 <= idade <= 60 and bpm > 80:
    print("Os batimentos estão acima da faixa adequada")

# desvios condicionais para idosos

elif 60 < idade and 50 <= bpm <= 60:
    print("Os batimentos estão dentro da faixa adequada")

elif 60 < idade and bpm < 50:
    print("Os batimentos estão abaixo da faixa adequada")

elif 60 < idade and bpm > 60:
    print("Os batimentos estão acima da faixa adequada")
# para crianças entre 3 e 7 anos

else:
    print("Não temos informações sobre a faixa de bpm para essa idade")
