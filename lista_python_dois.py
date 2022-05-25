def exercicio_um():
    numero_um = int(input("Informe um número inteiro: "))
    numero_dois = int(input("Informe um número inteiro: "))

    if numero_um > numero_dois:
        print("O primeiro número é maior que o segundo")
    else:
        print("O segundo número é maior que o primeiro")


def exercicio_dois():
    numero_um = float(input("Informe um número: "))
    if numero_um > 0:
        print("Este é um número positivo")
    else:
        print("Este é um número negativo")


def exercicio_tres():
    sexo = input("Informe o seu sexo, F ou M: ")
    sexo = sexo.upper()
    fem_str = "F"
    masc_str = "M"
    if sexo == fem_str:
        print("Feminino")
    elif sexo == masc_str:
        print("Masculino")
    else:
        print("Sexo não encontrado")


def exercicio_quatro():
    char = input("Digite um caractere: ")
    char = char.upper()
    if char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        print("É uma vogal")
    else:
        print("É uma consoante")


def exercicio_cinco():
    nota_total = 0.0

    for x in range(1, 3):
        nota = float(input("Informe a {} nota".format(x)))
        nota_total = nota_total + nota
    media = nota_total / 2

    print("A média do aluno é {}".format(media))
    if 10 > media >= 7:
        print("Aprovado")
    elif media < 7:
        print("Reprovado")
    elif media == 10:
        print("Aprovado com distinção")


def exercicio_seis():
    qtd = 3
    valores = []

    for i in range(qtd):
        v = float(input("Digite o {}º número: ".format(i)))
        valores.append(v)

        maior = valores[0]

    for i in range(qtd):
        if valores[i] > maior:
            maior = valores[i]

    print("O maior número é {}. ".format(maior))


def exercicio_sete():
    qtd = 5
    valores_maior = []
    valores_menor = []

    for i in range(qtd):
        v = float(input("Digite o {}º número: ".format(i + 1)))
        valores_maior.append(v)
        valores_menor.append(v)

        maior = valores_maior[0]
        menor = valores_menor[0]

    for i in range(qtd):
        if valores_maior[i] > maior:
            maior = valores_maior[i]

    print("O maior número é {}. ".format(maior))
    for i in range(qtd):
        if valores_menor[i] < menor:
            menor = valores_menor[i]

    print("O menor número é {}. ".format(menor))


def exercicio_sete_lucas():
    qtd = 5
    valores = []

    for i in range(qtd):
        v = float(input("Digite o {}º número: ".format(i + 1)))
        valores.append(v)

    val = valores[0]

    for i in range(1, qtd):
        if valores[i] > val:
            val = valores[i]

    print("O maior número é {}. ".format(val))

    val = valores[0]

    for i in range(1, qtd):
        if valores[i] < val:
            val = valores[i]

    print("O menor número é {}. ".format(val))


def exercicio_oito():
    qtde = 3
    valores = []

    for x in range(qtde):
        aux = float(input("Favor informar o preço do {}º produto.".format(x + 1)))
        valores.append(aux)

    menor = valores[0]

    for x in range(qtde):
        if valores[x] < menor:
            menor = valores[x]
    print("O menor preço é {} reais. ".format(menor))


def exercicio_nove():
    numeros = []

    for x in range(0, 3):
        aux = int(input("Informe o {}º numero:".format(x + 1)))
        numeros.append(aux)

    numeros.sort(reverse=True)
    print(numeros)


def exercicio_dez():
    print("Em qual turno você estuda?")
    turno = input("digitar as letras M-matutino ou V-Vespertino ou N- Noturno ")
    turno = turno.upper()
    if turno == 'M':
        print("Bom dia!")
    elif turno == 'V':
        print("Boa Tarde!")
    elif turno == 'N':
        print("Boa Noite!")
    else:
        print("Valor Inválido")


def exercicio_onze():
    salario = float(input("Informe o seu salário: "))

    if salario <= 280.00:

        salario_final = salario * 1.2
        aumento = salario * 0.2
        print("Salário anterior = R${}, A porcentagem de aumento é 20%. O Salário final é R${}, o aumento foi de R${}"\
              .format(salario, salario_final, aumento))
    elif 700 >= salario > 280:
        salario_final = salario * 1.15
        aumento = salario * 0.15
        print("Salário anterior = R${}, A porcentagem de aumento é 15%. O Salário final é R${}, o aumento foi de R${}" \
              .format(salario, salario_final, aumento))
    elif 1500 >= salario > 700:
        salario_final = salario * 1.1
        aumento = salario * 0.1
        print("Salário anterior = R${}, A porcentagem de aumento é 10%. O Salário final é R${}, o aumento foi de R${}" \
              .format(salario, salario_final, aumento))
    elif salario > 1500:
        salario_final = salario * 1.05
        aumento = salario * 0.05
        print("Salário anterior = R${}, A porcentagem de aumento é 5%. O Salário final é R${}, o aumento foi de R${}" \
              .format(salario, salario_final, aumento))


def exercicio_doze():
    hora = float(input("Informe a qtde de horas trabalhadas no mês: "))
    valor_hora = float(input("informe o valor da sua hora: "))

    salario = hora * valor_hora
    desc_inss = salario * 0.1
    desc_fgts = salario * 0.11
    salario_liq = salario - desc_inss

    if salario <= 900:
        print("Salário Bruto R${}\n IR isento\n INSS R${}\n FGTS R${}\n Total de descontos R${}\n Salário liquido R${}"\
              .format(salario, desc_inss, desc_fgts, desc_inss, salario_liq))

    elif 1500 >= salario > 900:

        desc_ir = salario * 0.05
        salario_liq = salario_liq - desc_ir
        total_desc = desc_ir + desc_inss

        print("Salário Bruto R${}\n IR R${}\n INSS R${}\n FGTS R${}\n Total de descontos R${}\n Salário liquido R${}" \
              .format(salario, desc_ir, desc_inss, desc_fgts, total_desc, salario_liq))
    elif 1500 < salario <= 2500:

        desc_ir = salario * 0.1
        salario_liq = salario_liq - desc_ir
        total_desc = desc_ir + desc_inss

        print("Salário Bruto R${}\n IR R${}\n INSS R${}\n FGTS R${}\n Total de descontos R${}\n Salário liquido R${}" \
              .format(salario, desc_ir, desc_inss, desc_fgts, total_desc, salario_liq))
    elif 2500 < salario:
        desc_ir = salario * 0.2
        salario_liq = salario_liq - desc_ir
        total_desc = desc_ir + desc_inss

        print("Salário Bruto R${}\n IR R${}\n INSS R${}\n FGTS R${}\n Total de descontos R${}\n Salário liquido R${}" \
              .format(salario, desc_ir, desc_inss, desc_fgts, total_desc, salario_liq))


def exercicio_treze():
    print("Qual o dia da semana?")
    dia = int(input("digitar o número 1 para segunda-feira,digitar o número 2 para terça-feira e assim por diante. "))

    if dia == 1:
        print("Segunda-feira")
    elif dia == 2:
        print("Terça-feira")
    elif dia == 3:
        print("Quarta-feira")
    elif dia == 4:
        print("Quinta-feira")
    elif dia == 5:
        print("Sexta-feira")
    elif dia == 6:
        print("Sábado")
    elif dia == 7:
        print("Domingo")
    else:
        print("dia não encontrado")
def exercicio_quatorze():
    nota_um = float(input("informe a 1º nota: "))
    nota_dois = float(input("informe 2º nota: "))
    media = (nota_um + nota_dois)/2
    if 10 >= media >= 9:
        print("Você está aprovado! Conceito A")
    elif 9 > media >= 7.5:
        print("Você está aprovado! Conceito B")
    elif 7.5 > media >= 6.0:
        print("Você está aprovado! Conceito C")
    elif 6 > media >= 4:
        print("Você está reprovado! Conceito D")
    elif 4 > media >= 0:
        print("Você está reprovado! Conceito E")
    else:
        print("ERRO")


def exercicio_quinze():
    lado_um = float(input("informe o tamanho do 1º lado do triangulo: "))
    lado_dois = float(input("informe o tamanho do 2º lado do triangulo: "))
    lado_tres = float(input("informe o tamanho do 3º lado do triangulo: "))

    tam_1 = lado_um + lado_dois
    tam_2 = lado_um + lado_tres
    tam_3 = lado_dois + lado_tres

    if tam_1 > lado_tres or tam_2 > lado_dois or tam_3 > lado_um:
        print("É um triângulo!")
        if lado_um == lado_dois or lado_um == lado_tres or lado_dois == lado_tres:
            print("É um triângulo Isósceles")
        elif lado_tres == lado_dois == lado_um:
            print("É um triângulo Equilatero")
        else:
            print("É um triângulo escaleno")
    else:
        print("Não é um triângulo")


def exercicio_dezesseis():
    a = float(input("Informe o valor de a: "))
    if a == 0:
        print("O programa acaba aqui.")
    else:
        b = float(input("Informe o valor de b: "))
        c = float(input("Informe o valor de c: "))

        delta = b ** 2 - 4 * a * c
        print(delta)

        if delta < 0:
            print("A equação não tem raízes reais.")
        elif delta == 0:
            bas = (-b)/(2*a)
            print("A equação tem apenas uma raíz real no valor de {}.".format(bas))
        elif delta > 0:
            bas = (-b + delta) / (2 * a)
            bas2 = (- b - delta) / (2 * a)
            print("A equação tem duas raízes reais, sendo elas no valor de {} e {}".format(bas, bas2))

def exercicio_dezessete():

    ano = int(input("Informe o ano:"))

    if ano % 4 == 0:
        print("O ano é bissexto!")
    else:
        print("O ano não é bissexto.")


def exercicio_dezoito():

    data = input('Digite uma data no formato dd/mm/aaaa: ')
    dia = int(data[:2])
    mes = int(data[3:5])
    ano = int(data[6:])

    if 12 >= mes >= 1:
        print(" ")
    else:
        print("mês inexistente")
    #ano bissexto

    if ano % 4 == 0:
        print("O ano é bissexto!")
        if 1 <= dia <= 31 and mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            print("data correta")
        elif 1 <= dia <= 29 and mes == 2:
            print("data correta")
        elif 1 <= dia <= 30 and mes == 4 or mes == 6 or mes == 9 or mes == 11:
            print("data correta")
        else:
            print("data incorreta")

    else:
        print("O ano não é bissexto.")
        if 1 <= dia <= 31 and mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            print("data correta")
        elif 1 <= dia <= 28 and mes == 2:
            print("data correta")
        elif 1 <= dia <= 30 and mes == 4 or mes == 6 or mes == 9 or mes == 11:
            print("data correta")
        else:
            print("data incorreta")


def exercicio_dezenove():
    numero = int(input("Informe um valor de 0 até 1000."))

    centena = numero // 100
    aux = (numero - (centena * 100))
    dezena = aux // 10
    unidade = aux % 10
    print(centena, dezena, unidade)

    if numero > 1000:
        print("número inválido, maior que 1000.")

    if centena == 1:
        cent = "centena"
    elif centena > 1:
        cent = "centenas"

    if dezena == 1:
        dez = "dezena"
    elif dezena > 1:
        dez = "dezenas"

    if unidade == 1:
        uni = "unidade"
    elif unidade > 1:
        uni = "unidades"

    if unidade == 0 and dezena == 0:
        print("O número tem {} {}.".format(centena, cent))
    elif centena == 0 and dezena == 0:
        print("O número tem {} {}.".format(unidade, uni))
    elif centena == 0 and unidade == 0:
        print("O número tem {} {}.".format(dezena, dez))
    elif centena > 0 and dezena > 0 and unidade > 0:
        print("O número tem {} {}, {} {}, {} {}.".format(centena, cent, dezena, dez, unidade, uni))
    elif centena > 0 and dezena > 0 and unidade == 0:
        print("O número tem {} {} e {} {}.".format(centena, cent, dezena, dez))
    elif centena > 0 and dezena == 0 and unidade >0:
        print("O número tem {} {} e {} {}.".format(centena, cent, unidade, uni))


def exercicio_vinte():
    media = []

    for x in range (3):
        notas = float(input("Insira a {} nota ".format(x + 1)))
        media.append(notas)

    print(media)
    media_final = (media[0]+media[1]+media[2])/3

    if 7 <= media_final < 10:
        print("Aprovado, sua média final é {}".format(media_final))
    elif media_final == 10:
        print("Aprovado com distinção, sua média final é {}".format(media_final))
    else:
        print("Reprovado, sua média final é {}".format(media_final))

def exercicio_vinteeum():
    valor_saque = int(input("informe um valor para saque de 1 a 600"))

    if valor_saque > 600 or valor_saque < 1:
        print("valor inválido")

    centena = valor_saque // 100
    aux = (valor_saque - (centena * 100))
    dezena = aux // 10
    notas_cinq = dezena // 5
    notas_dez = dezena % 5
    unidade = aux % 10
    notas_cinco = unidade // 5
    notas_um = unidade % 5

    print("Serão {} nota(s) de cem,{} nota(s) de 50, {} nota(s) de 10, {} nota(s) de 5 e {} nota(s) de um". format(centena, notas_cinq, notas_dez, notas_cinco, notas_um))
    

def exercicio_vintedois(numero):
    #numero = int(input("Informe um número:"))
    if numero % 2 == 0:
        print("Este número é par.")
    else:
        print("Este número é impar")


def exercicio_vintetres(numero):
    import math
    #numero = float(input("Informe um número."))
    aux = math.ceil(numero) #arredonda o número p cima

    if numero == aux:
        print("este número é inteiro")
    else:
        print("Este é um número decimal")


def aux_exercicio_vintequatro(numero):
    if numero >= 0:
        print("Este número é positivo")
    else:
        print("Este número é negativo")


def exercicio_vintequatro():
    numero_um = float(input("informe o 1º número: "))
    numero_dois = float(input("informe o 2º número: "))

    print("Para realizar soma, tecle 1")
    print("Para realizar subtração, tecle 2")
    print("Para realizar multiplicação, tecle 3")
    print("Para realizar divisão, tecle 4")

    operacao = int (input("Informe qual operação você gostaria de realizar"))

    soma = numero_um + numero_dois
    sub = numero_um - numero_dois
    mult = numero_um * numero_dois
    div = numero_um / numero_dois

    if operacao == 1:
        print("O resultado da soma é {}".format(soma))
        exercicio_vintetres(soma)
        exercicio_vintedois(soma)
        aux_exercicio_vintequatro(soma)
    elif operacao == 2:
        print("O resultado da subtração é {}".format(sub))
        exercicio_vintetres(sub)
        exercicio_vintedois(sub)
        aux_exercicio_vintequatro(sub)
    elif operacao == 3:
        print("O resultado da multiplicação é {}".format(mult))
        exercicio_vintetres(mult)
        exercicio_vintedois(mult)
        aux_exercicio_vintequatro(mult)
    elif operacao == 4:
        print("O resultado da divisão é {}".format(div))
        exercicio_vintetres(div)
        exercicio_vintedois(div)
        aux_exercicio_vintequatro(div)


def exercicio_vintecinco():
    pontuacao = 0

    pergunta_um = input("Telefonou para a vítima? ").upper()

    if pergunta_um == "SIM":
        pontuacao += 1

    pergunta_dois = input("Esteve no local do crime? ").upper()

    if pergunta_dois == "SIM":
        pontuacao += 1

    pergunta_tres = input("Mora perto da vítima? ").upper()

    if pergunta_tres == "SIM":
        pontuacao += 1

    pergunta_quatro = input("Devia para a vítima? ").upper()

    if pergunta_quatro == "SIM":
        pontuacao += 1

    pergunta_cinco = input("Já trabalhou com a vítima? ").upper()
    if pergunta_cinco == "SIM":
        pontuacao += 1

    print(pontuacao)

    if pontuacao == 2:
        print("Suspeita")
    elif pontuacao == 3 or pontuacao == 4:
        print("Cúmplice")
    elif pontuacao == 5:
        print("Assasino")
    else:
        print("Inocente")


def exercicio_vinteseis():
    litros = float(input("informe a quantidade de litros: "))
    alcool_gasolina = input("Informe A se for alcool ou G se for Gasolina").upper()

    if alcool_gasolina == "A" and litros <= 20:
        preco = (litros * 1.90) - (litros * 1.90 * 0.03)
        print(f"Valor total é R${preco}")
    elif alcool_gasolina == "A" and litros > 20:
        preco = (litros * 1.90) - (litros * 1.90 * 0.05)
        print(f"Valor total é R${preco}")
    elif alcool_gasolina == "G" and litros <= 20:
        preco = (litros * 2.5) - (litros * 2.5 * 0.04)
        print(f"Valor total é R${preco}")
    elif alcool_gasolina == "G" and litros > 20:
        preco = (litros * 2.5) - (litros * 2.5 * 0.06)
        print(f"Valor total é R${preco}")


def exercicio_vinteesete():
    quantidade_mor = float(input("Informe a quantidade em kg de morango comprado"))
    quantidade_maca = float(input("Informe a quantidade em kg de maça comprada"))

    if quantidade_mor > 5:
        preco_mor = 2.2 * quantidade_mor
    else:
        preco_mor = 2.5 * quantidade_mor


    if quantidade_maca > 5:
        preco_maca = 1.5 * quantidade_maca
    else:
        preco_maca = 1.8 * quantidade_maca

    preco_final = preco_maca + preco_mor

    if (quantidade_maca + quantidade_mor) > 8:
        preco_final = preco_final * 0.9

    print(f"Preço total da compra é R${preco_final}")


def exercicio_vinteoito():
    print("Você deve escolher apenas 2 tipos de carne.")
    tipo_carne = input("Informe o tipo de carne").upper()
    tipo_carne_dois = input("Informe o segundo tipo de carne").upper()

    if tipo_carne == "ALCATRA" or tipo_carne_dois == "ALCATRA":
        qtde_alcatra = float(input("Informe qtos kg de alcatra foram comprados"))

        if qtde_alcatra > 5:
            preco_alcatra = qtde_alcatra * 6.80
        else:
            preco_alcatra = qtde_alcatra * 5.90

    if tipo_carne == "PICANHA" or tipo_carne_dois == "PICANHA":
        qtde_picanha = float(input("Informe qtos kg de picanha foram comprados"))
        if qtde_picanha > 5:
            preco_picanha = qtde_picanha * 7.80
        else:
            preco_picanha = qtde_picanha * 6.90

    if tipo_carne == "FILE DUPLO" or tipo_carne_dois == "FILE DUPLO":
        qtde_file = float(input("Informe qtos kg de file foram comprados"))
        if qtde_file > 5:
            preco_file = qtde_file * 5.80
        else:
            preco_file = qtde_file * 4.90

    preco_final = preco_file + preco_picanha + preco_alcatra

    tipo_pagamento = input("Informe o tipo de pagamento.").upper()

    if tipo_pagamento == "CARTÃO TABAJARA":
        desconto = preco_final * 0.05
        preco_final = preco_final - desconto





if __name__ == "__main__":
    # exercicio_dez()
    # exercicio_um()
    # exercicio_dois()
    # exercicio_tres()
    # exercicio_quatro()
    # exercicio_cinco()
    # exercicio_seis()
    # exercicio_sete()
    # exercicio_oito()
    # exercicio_nove()
    #exercicio_sete_lucas()
    #exercicio_onze()
    #exercicio_doze()
    #exercicio_treze()
    #exercicio_quatorze()
    #exercicio_quinze()
    #exercicio_dezesseis()
    #exercicio_dezessete()
    #exercicio_dezoito()
    #exercicio_dezenove()
    #exercicio_vinte()
    #exercicio_vinteeum(
    #exercicio_vintedois()
    #exercicio_vintetres()
    #exercicio_vintequatro()
    #exercicio_vintecinco()
    #exercicio_vinteseis()
    exercicio_vinteesete()