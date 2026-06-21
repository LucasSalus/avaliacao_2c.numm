from interpolacao import interpolacao_lagrange, interpolacao_newton

# Dados do Dataset do Drone (Enunciado do Problema 1)
tempos = [1.0, 2.0, 3.0, 4.0, 5.0]
altitudes = [10.0, 25.0, 45.0, 70.0, 105.0]

# O instante da falha do sensor
tempo_falha = 3.5

# Executa o algoritmo que criamos do zero
res_lagrange = interpolacao_lagrange(tempos, altitudes, tempo_falha)
res_newton = interpolacao_newton(tempos, altitudes, tempo_falha)


print("--- SISTEMA DE TELEMETRIA DO DRONE ---")
print(f"Altitude estimada por Lagrange = {tempo_falha}s: {res_lagrange:.2f} metros")
print(f"Altitude por Newton   (t={tempo_falha}s): {res_newton:.4f} metros\n")
