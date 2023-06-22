import numpy as np
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
t = np.linspace(0, 4 * np.pi, 500) # 500 puntos entre 0 y 4*pi
y = np.sin(t)

# Detectar el ciclo
periodo = detectar_ciclo(t, y)
print(f'Periodo detectado: {periodo}')