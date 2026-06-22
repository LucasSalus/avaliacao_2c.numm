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

def interpolacao_newton(x_pontos, y_pontos, x_alvo):

    n = len(x_pontos)
    
    # Cria a tabela triangular preenchida com zeros usando listas puras
    tabela = [[0.0] * n for _ in range(n)]
    
    # Preenche a primeira coluna com os valores de Y
    for i in range(n):
        tabela[i][0] = y_pontos[i]
        
    # Constrói a tabela de diferenças divididas
    for j in range(1, n):
        for i in range(n - j):
            num = tabela[i + 1][j - 1] - tabela[i][j - 1]
            den = x_pontos[i + j] - x_pontos[i]
            tabela[i][j] = num / den

    # Calcula o valor interpolado final
    resultado = tabela[0][0]
    termo_multiplicador = 1.0
    
    for i in range(1, n):
        termo_multiplicador *= (x_alvo - x_pontos[i - 1])
        resultado += tabela[0][i] * termo_multiplicador
        
    return resultado

def interpolacao_gregory_newton(x_pontos, y_pontos, x_alvo):
    
    n = len(x_pontos)
    h = x_pontos[1] - x_pontos[0]  
    
    tabela = [[0.0] * n for _ in range(n)]
    
    for i in range(n):
        tabela[i][0] = y_pontos[i]
        
    for j in range(1, n):
        for i in range(n - j):
            tabela[i][j] = tabela[i + 1][j - 1] - tabela[i][j - 1]
            
    u = (x_alvo - x_pontos[0]) / h
    
    resultado = tabela[0][0]
    termo_multiplicador = 1.0
    
    for i in range(1, n):
        fatorial = 1
        for k in range(1, i + 1):
            fatorial *= k
            
        termo_multiplicador *= (u - (i - 1))
        resultado += (termo_multiplicador * tabela[0][i]) / fatorial
        
    return resultado
