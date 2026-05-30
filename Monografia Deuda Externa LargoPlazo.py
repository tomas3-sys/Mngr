import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()

# SECTOR PUBLICO"
años = ([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013, 2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024])
amo_pu = ([2.128, 2.824, 3.821, 3.670, 2.122, 5.546, 4.083, 2.898, 2.313, 1.729, 2.192, 2.069, 3.546, 1.851, 2.618, 2.670, 1.809, 6.284, 6.252, 5.195, 3.074, 5.906, 4.381, 6.434, 10.101])
int_pu = ([1.517, 1.639, 1.671, 1.701, 1.740, 2.064, 1.821, 1.981, 2.194, 2.101, 2.259, 2.199, 2.266, 2.291, 2.573, 3.054, 3.062, 3.311, 3.493, 3.707, 3.421, 3.798, 3.921, 5.199, 6.333])
#SECTOR PRIVADO"
amo_pr = ([3.601, 2.567, 3.202, 3.011, 3.434, 2.842, 3.876, 2.802, 2.874, 4.140, 4.329, 4.193, 8.577, 4.422, 6.974, 6.924, 5.763, 9.931, 9.459, 8.036, 11.527, 9.211, 14.917, 9.649, 11.444])
int_pr = ([0.973, 0.755, 0.717, 0.602, 0.595, 0.613, 0.695, 0.749, 0.750, 0.748, 0.674, 0.913, 1.005,1.270, 1.392, 1.480, 1.659, 1.933, 2.186, 2.467, 2.225, 2.202, 2.629, 3.338, 3.734])
#TOTAL#
subtotal_pub = ([3.645, 4.464, 5.492, 5.371, 3.863, 7.610, 5.904, 4.879, 4.507, 3.830, 4.451, 4.267, 5.812, 4.142, 5.190, 5.724, 4.870, 9.594, 9.745, 8.901, 9.644, 6.495, 8.302, 11.632, 16.433])
subtotal_pri = ([4.573, 3.322, 3.919, 3.613, 4.029, 3.455, 4.571, 3.551, 3.625, 4.888, 5.002, 5.106, 9.582, 5.6912, 8.366, 8.403, 7.423, 11.864, 11.644, 10.503, 13.752, 11.413, 17.546, 12.987, 15.178])
totaldeu = ([8.218, 7.786, 9.411, 8.983, 7.892, 11.064, 10.475, 8.430, 8.132, 8.718, 9.453, 9.373, 15.394, 9.834, 13.557, 14.127, 12.293, 21.458, 21.390, 19.404, 20.247, 21.058, 25.848, 24.619, 31.611])
# Convertir las listas en numpy arrays para resolver aritmética más rápida.
amo_pu = np.array(amo_pu)
int_pu = np.array(int_pu)
amo_pr = np.array(amo_pr)
int_pr = np.array(int_pr)
subtotal_pri = np.array(subtotal_pri)
subtotal_pub = np.array(subtotal_pub)
totaldeu = np.array(totaldeu)
# Barras apiladas de los Diagramas en orden cronológico (las líneas conectan al bar más cercano).
ax.plot(años, subtotal_pri, label="Subtotal Sec.Privado", color='purple', linestyle = "dotted", marker='o')
ax.plot(años, subtotal_pub, label="Subtotal Sec.Publico", color='brown', linestyle = "dotted", marker='s')
ax.plot(años, totaldeu, label="Total Endeudamiento ", color= 'black',linestyle = "dashed", marker = '^')
ax.bar(años, amo_pr, color='green', label = "Amortizaciones SPu")
ax.bar(años, amo_pu, color='blue', bottom=amo_pr, label = "Amortizaciones SPr")
ax.bar(años, int_pu, color='red', bottom=amo_pr + amo_pu, label = "Intereses SPr")
ax.bar(años, int_pr, color='orange', bottom=amo_pr + amo_pu + int_pu, label = "Intereses SPu")
# Etiquetas, legenda y crudricula
ax.set_title("Servicio de la Deuda Externa a Largo Pazo")
ax.set_xlabel("Año Fiscal")
ax.set_ylabel("Millones de Dólares (USD)")
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()