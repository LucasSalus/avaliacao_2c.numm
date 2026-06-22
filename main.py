from interpolacao import interpolacao_lagrange, interpolacao_newton, interpolacao_gregory_newton, spline_linear, spline_cubica_natural
from integracao import regra_trapezios_pontos, regra_simpson_13_pontos, regra_simpson_38_pontos

# Dados do Dataset do Drone (Enunciado do Problema 1)
tempos = [1.0, 2.0, 3.0, 4.0, 5.0]
altitudes = [1.2, 1.9, 3.2, 5.5, 8.2]

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
temp_servidor = [45.0, 52.0, 60.0, 71.0]
minuto_alvo = 25.0

res_gregory = interpolacao_gregory_newton(minutos_servidor, temp_servidor, minuto_alvo)

print("--- MONITORAMENTO DO DATA CENTER ---")
print(f"Temperatura estimada no minuto {minuto_alvo}: {res_gregory:.4f}°C")

# --- PROBLEMA 3: BRAÇO ROBÓTICO ---

# Dados do movimento do laser do braço robótico
tempos_robo = [0.0, 1.0, 2.0, 3.0]
posicoes_robo = [2.5, 4.5, 3.0, 6.0]
instante_alvo = 1.5

res_spline_lin = spline_linear(tempos_robo, posicoes_robo, instante_alvo)
res_spline_cub = spline_cubica_natural(tempos_robo, posicoes_robo, instante_alvo)

print("--- CONTROLE DO BRAÇO ROBÓTICO ---")
print(f"Posição por Spline Linear (t={instante_alvo}s): {res_spline_lin:.4f} mm")
print(f"Posição por Spline Cúbica (t={instante_alvo}s): {res_spline_cub:.4f} mm")


# --- PROBLEMA 4: MONITOR DE REDE (3/8 Simpson) ---
t = [0, 2, 4, 6], h = 2
banda_servidor = [10.0, 15.0, 12.0, 8.0]
h_servidor = 2.0

res_p4_simpson38 = regra_simpson_38_pontos(banda_servidor, h_servidor)

print("--- MONITOR DE REDE (PROBLEMA 4) ---")
print(f"Total de dados transferidos: {res_p4_simpson38:.2f} MB\n")



# --- PROBLEMA 5: ODÔMETRO DO CARRO ELÉTRICO ---
t = [0.0, 0.5, 1.0, 1.5, 2.0], h = 0.5
velocidades_carro = [0.0, 40.0, 65.0, 80.0, 90.0]
h_carro = 0.5

res_p5_trapezios = regra_trapezios_pontos(velocidades_carro, h_carro)
res_p5_simpson13 = regra_simpson_13_pontos(velocidades_carro, h_carro)

print("--- CONSUMO DO CARRO ELÉTRICO (PROBLEMA 5) ---")
print(f"Distância por Trapézios: {res_p5_trapezios:.2f} km")
print(f"Distância por 1/3 Simpson: {res_p5_simpson13:.2f} km\n")
