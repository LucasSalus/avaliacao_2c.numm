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


    