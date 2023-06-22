import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define el sistema de ecuaciones diferenciales
def lotka_volterra(t, y, a, b, c, d):
    x, y = y
    dxdt = a*x - b*x*y
    dydt = c*x*y - d*y
    return [dxdt, dydt]

# Define los parámetros del modelo
a = 1.5
b = 1
c = 3
d = 1

# Define los puntos iniciales para la integración
t_span = [0, 20]
y0 = [10, 5]

# Integra el sistema de ecuaciones diferenciales
sol = solve_ivp(lotka_volterra, t_span, y0, args=(a, b, c, d), dense_output=True)




def detectar_ciclo(t, y):
    # Calcular la Transformada Rápida de Fourier
    fft_result = np.fft.fft(y)
    freqs = np.fft.fftfreq(len(y), d=t[1]-t[0])  # ahora tomando en cuenta el espaciado de tiempo
    
    # Ignorar la mitad de los resultados debido a la simetría compleja conjugada
    fft_result = fft_result[:len(fft_result)//2]
    freqs = freqs[:len(freqs)//2]
    
    # Encuentra la frecuencia con la amplitud más alta
    indice_frecuencia_maxima = np.argmax(np.abs(fft_result))
    frecuencia_maxima = freqs[indice_frecuencia_maxima]
    
    # El período es el inverso de la frecuencia
    periodo = 1.0 / frecuencia_maxima if frecuencia_maxima != 0 else None
    return periodo

# Definir la serie de tiempo
t = np.linspace(0, 20, 1000)
y = sol.sol(t)

# Detectar el ciclo
periodo = detectar_ciclo(t, y)
print(f'Periodo detectado: {periodo}')