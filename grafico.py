import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Temperaturas (K) e Intensidades (mv)
T = np.array([1194.7532896432292 ,
1140.864036275123 ,
1071.030411928571 ,
997.0199123003634 ,
907.8142123271108 ,
790.3155082996855 ,
664.0418553615477])
I = np.array([0.0084, 0.0058, 0.0038, 0.0024, 0.0013, 0.0008, 0.0006])

# Cálculo de 1/T e ln(I)
inv_T = 1 / T
ln_I = np.log(I)

# Regressão linear
slope, intercept, r_value, p_value, std_err = linregress(inv_T, ln_I)

# Linha de ajuste
x_fit = np.linspace(inv_T.min(), inv_T.max(), 100)
y_fit = slope * x_fit + intercept

# Plot
plt.figure(figsize=(8, 6))
plt.plot(inv_T, ln_I, 'o', label='Dados experimentais')
plt.plot(x_fit, y_fit, '-', color='green', label=f'Ajuste linear\nInclinação = {slope:.2e}')
plt.xlabel('1 / T (1/K)')
plt.ylabel('ln(Intensidade)')
plt.title('Gráfico ln(Intensidade) vs. 1/Temperatura')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
