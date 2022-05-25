print("Para lives na segunda-feira tecle 1")
print("Para lives na terça-feira tecle 2.")
print("Para lives na quarta-feira tecle 3.")
print("Para lives na quinta-feira tecle 4.")
print("Para lives na sexta-feira tecle 5.")
segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0

dia_live = 0
for dia_live in range (1,11) :
    dia_live = int(input("Informe o dia da semana que você gostaria de ver a live: "))
    print("data escolhido é", dia_live)
    if dia_live == 1:
        segunda += 1
    elif dia_live == 2:
        terca += 1
    elif dia_live == 3:
        quarta += 1
    elif dia_live == 4:
        quinta += 1
    elif dia_live == 5:
        sexta += 1
    else:
        print("voto não computado")
print("Foram computados {} votos para segunda, {} votos para terça, {} votos para quarta, {} votos para quinta, {} votos para sexta".format(segunda,terca,quarta,quinta,sexta))



