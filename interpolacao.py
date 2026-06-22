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

def spline_linear(x_pontos, y_pontos, x_alvo):
    n = len(x_pontos)
    
    idx = -1
    for i in range(n - 1):
        if x_pontos[i] <= x_alvo <= x_pontos[i + 1]:
            idx = i
            break
            
    if idx == -1:
        if x_alvo < x_pontos[0]: idx = 0
        else: idx = n - 2

    
    x0, x1 = x_pontos[idx], x_pontos[idx + 1]
    y0, y1 = y_pontos[idx], y_pontos[idx + 1]
    
    resultado = y0 + ((y1 - y0) / (x1 - x0)) * (x_alvo - x0)
    return resultado


def spline_cubica_natural(x_pontos, y_pontos, x_alvo):
 
    n = len(x_pontos)
    num_intervalos = n - 1
    
    h = [x_pontos[i+1] - x_pontos[i] for i in range(num_intervalos)]
   
    a = [0.0] * n
    b = [1.0] * n
    c = [0.0] * n
    d = [0.0] * n
    
    for i in range(1, num_intervalos):
        a[i] = h[i - 1]
        b[i] = 2.0 * (h[i - 1] + h[i])
        c[i] = h[i]
        
        termo1 = (y_pontos[i + 1] - y_pontos[i]) / h[i]
        termo2 = (y_pontos[i] - y_pontos[i - 1]) / h[i - 1]
        d[i] = 6.0 * (termo1 - termo2)
        
    c_linha = [0.0] * n
    d_linha = [0.0] * n
    g = [0.0] * n 
    
    c_linha[0] = c[0] / b[0]
    d_linha[0] = d[0] / b[0]
    
    for i in range(1, n):
        den = b[i] - a[i] * c_linha[i - 1]
        if i < n - 1:
            c_linha[i] = c[i] / den
        d_linha[i] = (d[i] - a[i] * d_linha[i - 1]) / den
        
    g[n - 1] = d_linha[n - 1]
    for i in range(n - 2, -1, -1):
        g[i] = d_linha[i] - c_linha[i] * g[i + 1]
        
    idx = -1
    for i in range(num_intervalos):
        if x_pontos[i] <= x_alvo <= x_pontos[i + 1]:
            idx = i
            break
    if idx == -1:
        if x_alvo < x_pontos[0]: idx = 0
        else: idx = num_intervalos - 1
        
  
    hi = h[idx]
    xi = x_pontos[idx]
    x_prox = x_pontos[idx + 1]
    
    termo_cub_prox = (g[idx + 1] / (6.0 * hi)) * ((x_alvo - xi) ** 3)
    termo_cub_atual = (g[idx] / (6.0 * hi)) * ((x_prox - x_alvo) ** 3)
    termo_lin_prox = ((y_pontos[idx + 1] / hi) - (g[idx + 1] * hi / 6.0)) * (x_alvo - xi)
    termo_lin_atual = ((y_pontos[idx] / hi) - (g[idx] * hi / 6.0)) * (x_prox - x_alvo)
    
    resultado = termo_cub_prox + termo_cub_atual + termo_lin_prox + termo_lin_atual
    return resultado

