def interpolacao_lagrange(x_pontos, y_pontos, x_alvo):
    """
    Realiza a interpolação polinomial de Lagrange.
    
    x_pontos: Lista com os valores de X conhecidos (ex: tempos)
    y_pontos: Lista com os valores de Y conhecidos (ex: altitudes)
    x_alvo: O ponto onde queremos estimar o valor (ex: t = 3.5)
    """
    n = len(x_pontos)
    resultado = 0.0

    # Somatório principal da fórmula de Lagrange
    for i in range(n):
        # Inicializa o produtório L_i(x) como 1
        termo_lagrange = 1.0
        
        # Calcula o produtório para o ponto atual i
        for j in range(n):
            if i != j:
                num = x_alvo - x_pontos[j]
                den = x_pontos[i] - x_pontos[j]
                termo_lagrange *= (num / den)
        
        # Adiciona ao resultado final: y_i * L_i(x)
        resultado += y_pontos[i] * termo_lagrange

    return resultado