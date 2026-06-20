from interpolacao import interpolacao_lagrange

# Dados do Dataset do Drone (Enunciado do Problema 1)
tempos = [1.0, 2.0, 3.0, 4.0, 5.0]
altitudes = [10.0, 25.0, 45.0, 70.0, 105.0]

# O instante da falha do sensor
tempo_falha = 3.5

# Executa o algoritmo que criamos do zero
altitude_estimada = interpolacao_lagrange(tempos, altitudes, tempo_falha)

print("--- SISTEMA DE TELEMETRIA DO DRONE ---")
print(f"Altitude estimada no instante t = {tempo_falha}s: {altitude_estimada:.2f} metros")