
import numpy as np

def detectar_ciclo(t, y, tolerancia=1e-10):
    # Calcular la Transformada Rápida de Fourier
    fft_result = np.fft.fft(y)
    freqs = np.fft.fftfreq(len(y), d=t[1]-t[0])
    
    # Ignorar la mitad de los resultados debido a la simetría compleja conjugada
    fft_result = fft_result[:len(fft_result)//2]
    freqs = freqs[:len(freqs)//2]
    
    # Encuentra la frecuencia con la amplitud más alta
    amplitudes = np.abs(fft_result)
    indice_frecuencia_maxima = np.argmax(amplitudes)
    frecuencia_maxima = freqs[indice_frecuencia_maxima]
    
    # El período es el inverso de la frecuencia
    if np.abs(frecuencia_maxima) > tolerancia: 
        periodo = 1.0 / frecuencia_maxima
    else:
        print("No se puede determinar el período, la frecuencia máxima es demasiado pequeña.")
        periodo = None
    return periodo

# Definir la serie de tiempo
t = np.linspace(0, 4 * np.pi, 5000) # 5000 puntos entre 0 y 4*pi
y = np.sin(t)

# Detectar el ciclo
periodo = detectar_ciclo(t, y)
print(f'Periodo detectado: {periodo}')
print(2* np.pi)