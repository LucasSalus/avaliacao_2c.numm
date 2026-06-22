def regra_trapezios_pontos(y_pontos, h):
    
    n = len(y_pontos) - 1
    soma = 0.5 * (y_pontos[0] + y_pontos[-1])
    
    for i in range(1, n):
        soma += y_pontos[i]
        
    return soma * h


def regra_simpson_13_pontos(y_pontos, h):
 
    n = len(y_pontos) - 1
    if n % 2 != 0:
        raise ValueError("Para a Regra de 1/3 de Simpson, o número de intervalos deve ser par.")
        
    soma = y_pontos[0] + y_pontos[-1]
    
    for i in range(1, n):
        if i % 2 == 0:
            soma += 2 * y_pontos[i]  
        else:
            soma += 4 * y_pontos[i]  
            
    return soma * (h / 3)


    
def mmq_ajuste_linear(x_pontos, y_pontos):

    n = len(x_pontos)
    
    sum_x = sum(x_pontos)
    sum_y = sum(y_pontos)
    sum_x2 = sum(x ** 2 for x in x_pontos)
    sum_xy = sum(x * y for x, y in zip(x_pontos, y_pontos))
   
    denominador = (n * sum_x2) - (sum_x ** 2)
    
    a = ((n * sum_xy) - (sum_x * sum_y)) / denominador
    b = ((sum_x2 * sum_y) - (sum_x * sum_xy)) / denominador
    
    return a, b


def quadratura_gauss_2pontos(funcao, a, b):
    
    raiz3 = 3.0 ** 0.5
    
    t = [-1.0 / raiz3, 1.0 / raiz3]
    pesos = [1.0, 1.0]
    
    
    soma = 0.0
    for i in range(2):
        x = ((b - a) * t[i] + (b + a)) / 2.0
        soma += pesos[i] * funcao(x)
        
    return ((b - a) / 2.0) * soma
