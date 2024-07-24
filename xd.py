import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats



#Parámetros

df = 48  # Grados de libertad (n - 1)
alpha = 0.05
t_critical = stats.t.ppf(1 - alpha/2, df=df)  # Valor crítico t para un nivel de significancia de 0.05 (bilateral)

#Valores para la gráfica

t_values = np.linspace(-4, 4, 1000)  # Valores de t para la gráfica
pdf_values = stats.t.pdf(t_values, df=df)  # Densidad de probabilidad de la distribución t

#Crear gráfica

plt.figure(figsize=(8, 6))
plt.plot(t_values, pdf_values, label=f'Distribución t con {df} grados de libertad')
plt.fill_between(t_values, 0, pdf_values, where=(t_values <= -t_critical) | (t_values >= t_critical), color='red', alpha=0.3, label=f'Región de rechazo (α={alpha})')
plt.axvline(x=9.36, color='black', linestyle='--', linewidth=1.5, label='Valor de t calculado (9.36)')
plt.axvline(x=-t_critical, color='blue', linestyle='--', linewidth=1, label='Valor crítico t1 = -1.96, t2 = 1.96')
plt.axvline(x=t_critical, color='blue', linestyle='--', linewidth=1)
plt.xlabel('t')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución t de Student y prueba de hipótesis')
plt.legend()
plt.grid(True)
plt.xlim(-4, 4)
plt.ylim(0, 0.4)
plt.show()