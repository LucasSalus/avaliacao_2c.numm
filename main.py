from interpolacao import interpolacao_lagrange, interpolacao_newton, interpolacao_gregory_newton, spline_linear, spline_cubica_natural

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

# --- PROBLEMA 2: SERVIDOR DATA CENTER ---
minutos_servidor = [10.0, 20.0, 30.0, 40.0]
temp_servidor = [55.0, 62.0, 68.0, 75.0] 
minuto_alvo = 25.0

res_gregory = interpolacao_gregory_newton(minutos_servidor, temp_servidor, minuto_alvo)

print("--- MONITORAMENTO DO DATA CENTER ---")
print(f"Temperatura estimada no minuto {minuto_alvo}: {res_gregory:.4f}°C")

# --- PROBLEMA 3: BRAÇO ROBÓTICO ---

# Dados do movimento do laser do braço robótico
tempos_robo = [0.0, 1.0, 2.0, 3.0]
posicoes_robo = [0.0, 0.5, 2.0, 1.5]
instante_alvo = 1.5

res_spline_lin = spline_linear(tempos_robo, posicoes_robo, instante_alvo)
res_spline_cub = spline_cubica_natural(tempos_robo, posicoes_robo, instante_alvo)

print("--- CONTROLE DO BRAÇO ROBÓTICO ---")
print(f"Posição por Spline Linear (t={instante_alvo}s): {res_spline_lin:.4f} mm")
print(f"Posição por Spline Cúbica (t={instante_alvo}s): {res_spline_cub:.4f} mm")
