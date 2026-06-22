def regra_trapezios(f, a, b, n):
    h = (b - a) / n
    soma = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        soma += f(a + i * h)
        
    return soma * h


def regra_simpson_13(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("O número de intervalos (n) para a Regra de 1/3 de Simpson deve ser par.")
        
    h = (b - a) / n
    soma = f(a) + f(b)
    
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            soma += 2 * f(x)  
        else:
            soma += 4 * f(x)  
            
    return soma * (h / 3)


def regra_simpson_38(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("O número de intervalos (n) para a Regra de 3/8 de Simpson deve ser múltiplo de 3.")
        
    h = (b - a) / n
    soma = f(a) + f(b)
    
    for i in range(1, n):
        x = a + i * h
        if i % 3 == 0:
            soma += 2 * f(x)  
        else:
            soma += 3 * f(x)  
            
    return soma * (3 * h / 8)
