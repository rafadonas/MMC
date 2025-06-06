import numpy as np
import matplotlib.pyplot as plt

# --- Implementação das Funções Matemáticas ---

def T(t):
    """
    Calcula a temperatura T(t) para a onda de calor.
    t: tempo em meses
    """
    return 35 + (1 - np.exp(-t / 27)) + t * np.exp(-34.33 * t)
  
def e(x):
    """
    Calcula a escala Richter e(x) para os movimentos da terra.
    x: velocidade em m/s
    """
    # Adicionado um pequeno epsilon a x para evitar log de zero em np.sqrt(8*x) quando x=0
    epsilon = 1e-9
    # Nota: O termo cos(sqrt(8x) - 19.47) causa oscilações.
    return 5.47 + 1.85 * np.exp(-x) * np.cos(np.sqrt(8 * (x + epsilon)) - 19.47) + (x - 1.365) * np.exp(-34.33 * x)

# --- Domínios de Análise ---
t_domain = np.linspace(0, 36, 1000)  # Tempo de 0 a 36 meses
x_domain = np.linspace(0, 5, 1000)   # Velocidade de 0 a 5 m/s

# --- Cálculo dos Valores das Funções ---
T_values = T(t_domain)
e_values = e(x_domain)

# --- Identificação dos Pontos Máximos e Mínimos (Memória de Cálculo) ---

# Para T(t)
min_T_index = np.argmin(T_values)
max_T_index = np.argmax(T_values)
t_min = t_domain[min_T_index]
T_min = T_values[min_T_index]
t_max = t_domain[max_T_index]
T_max = T_values[max_T_index]

# Para e(x)
min_e_index = np.argmin(e_values)
max_e_index = np.argmax(e_values)
x_min = x_domain[min_e_index]
e_min = e_values[min_e_index]
x_max = x_domain[max_e_index]
e_max = e_values[max_e_index]

# --- Plotagem dos Gráficos ---

# Gráfico para T(t) - Onda de Calor
plt.figure(figsize=(12, 7))
plt.plot(t_domain, T_values, label='T(t)', color='red')
plt.scatter([t_min, t_max], [T_min, T_max], color='blue', zorder=5) # zorder para sobrepor os pontos
plt.title('Modelo de Onda de Calor: T(t)', fontsize=16)
plt.xlabel('Tempo (meses)', fontsize=12)
plt.ylabel('Temperatura T(t)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Anotações dos pontos
plt.annotate(f'Mínimo\n({t_min:.2f}, {T_min:.2f})', xy=(t_min, T_min), xytext=(t_min + 2, T_min - 0.2))
plt.annotate(f'Máximo\n({t_max:.2f}, {T_max:.2f})', xy=(t_max, T_max), xytext=(t_max - 10, T_max - 0.1))
plt.show()

# Gráfico para e(x) - Movimentos da Terra
plt.figure(figsize=(12, 7))
plt.plot(x_domain, e_values, label='e(x)', color='green')
plt.scatter([x_min, x_max], [e_min, e_max], color='purple', zorder=5)
plt.title('Modelo de Movimentos Anômalos da Terra: e(x)', fontsize=16)
plt.xlabel('Velocidade (m/s)', fontsize=12)
plt.ylabel('Escala Richter e(x)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Anotações dos pontos
plt.annotate(f'Mínimo\n({x_min:.2f}, {e_min:.2f})',
             xy=(x_min, e_min),
             xytext=(x_min + 0.5, e_min + 0.5)), # Move o texto para cima e para a direita
plt.annotate(f'Máximo\n({x_max:.2f}, {e_max:.2f})',
             xy=(x_max, e_max),
             xytext=(x_max + 0.5, e_max - 0.5)), # Move o texto para baixo e para a direita
             
plt.show()