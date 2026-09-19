custo = float(input("Qual o custo total da compra?")) #recebe o custo total da compra

desconto = 0.0 #defini a variavel desconto

if custo < 200.0: #se o custo for menor que 200 temos 5% de desconto
    desconto = custo*0.05
elif 200 <= custo < 300: #se o custo for maior ou igual a 200 e menor que 300 temos 10% de desconto
    desconto = custo*0.1
else:
    desconto = custo*0.15 #se o custo for maior ou igual a 300 temos 15% de desconto

print(f"Você recebeu um desconto de {desconto:.2f} e pagará um total de {custo - desconto:.2f} reais") #mostra na tela o resultado final

