
def fibo(parada,valor_parada):
    lista_fibo = []
    n0 = 1
    n1 = 1
    lista_fibo.append(n0)
    lista_fibo.append(n1)
    if parada == 'pos' and valor_parada.isdigit():
        for i in range(int(valor_parada) - 2):
            if i == 0:
                lista_fibo.append(lista_fibo[0] + lista_fibo[1])
            else:
                lista_fibo.append(lista_fibo[i] + lista_fibo[i+1])

        return lista_fibo
    
    elif parada == 'exa' and valor_parada.isdigit():
        i = 0
        while True:
            if i == 0:
                lista_fibo.append(lista_fibo[0] + lista_fibo[1])
                i+=1
            else:
                lista_fibo.append(lista_fibo[i] + lista_fibo[i+1])
                i+=1
                if lista_fibo[-1] == int(valor_parada):
                    break
                elif lista_fibo[-1] >= int(valor_parada):
                    lista_fibo.pop()
                    break
        return lista_fibo
    
    else:
        return 'Burro!'

    
parada = input("Digite 'pos' para parar na posição do número ou digite 'exa' para parar naquele número: ")
valor_parada = input("Digite o número da parada: ")
x = fibo(parada, valor_parada)

if type(x) == list:
    for i in x:
        print(i)
else:
    print(x)


