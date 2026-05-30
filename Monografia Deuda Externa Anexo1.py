import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()


# x axis (years)
años = np.array([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024])
## SECTOR PRIVADO ##
# CORTO PLAZO
crpl_saldo1 = np.array([2315, 2802, 3063, 3095, 4332, 4956, 4321, 4449, 5064, 3605, 7108, 9590, 9835, 11649, 14235, 15485, 14179, 15999, 19693, 22069, 21396, 23704, 28711, 30198, 31235])
# LARGO PLAZO
desembolsos1 = np.array([2493, 2187, 1855, 1916, 2380, 2872, 3697, 4604, 3450, 5277, 9332, 9156, 7762, 9798, 6675, 9292, 10407, 11298, 12063, 11283, 12162, 11264, 20176, 12236, 15669])
Amortizaciones1 = np.array([3601, 2567, 3202, 3011, 3434, 2842, 3876, 2802, 2874, 4140, 4329, 4193, 8577, 4422, 6974, 6924, 5763, 9931, 9459, 8036, 11527, 9211, 14917, 9649, 11444])
lrpl_saldo1 = np.array([13207, 12827, 11480, 10385, 9331, 9361, 9483, 11285, 11861, 12985, 18084, 23544, 22833, 28207, 27907, 30275, 35141, 36927, 39531, 42778, 43152, 45205, 50464, 53051, 57275])
total_saldo1 = np.array([15522, 15629, 14543, 13480, 13662, 14317, 13803, 15734, 16925, 16590, 25192, 33135, 32669, 39856, 42142, 45760, 49319, 52926, 59223, 64848, 64548, 68909, 79176, 83249, 88511])
# SECTOR PUBLICO ##
crpl_saldo2 = np.array([199, 320, 429, 224, 391, 399, 254, 695, 552, 339, 995, 825, 665, 515, 703, 702, 673, 591, 766, 863, 687, 976, 1125, 1287, 1352])
# LARGO PLAZO
desembolsos2 = np.array([3282, 5763, 2518, 4934, 2905, 4323, 5903, 4487, 3425, 9173, 3700, 4486, 6906, 8564, 11419, 10507, 7000, 6599, 8030, 6048, 18604, 19603, 8562, 12818, 11953])
Amortizaciones2 = np.array([2128, 2824, 3821, 3670, 2122, 5546, 4083, 2898, 2313, 1729, 2192, 2069, 3546, 1851, 2618, 2670, 1809, 6284, 6252, 5195, 3074, 5906, 4381, 6434, 10101])
lrpl_saldo2 = np.array([20498, 23214, 22409, 24360, 25444, 23790, 26045, 28124, 28962, 36850, 38605, 41662, 45450, 51701, 59064, 65456, 70405, 71279, 72234, 72972, 89272, 101418, 103518, 111683, 111843])
total_saldo2 = np.array([20697, 23535, 22838, 24584, 25835, 24189, 26299, 28819, 29514, 37190, 39600, 42487, 46116, 52216, 59767, 66158, 71078, 71870, 72999, 73835, 89959, 102395, 104643, 112970, 113195])
# Deuda Externa Total
total_saldo = np.array([36219, 39163, 37382, 38065, 39497, 38507, 40103, 44553, 46440, 53779, 64792, 75622, 78784, 92073, 101909, 111918, 120397, 124796, 132223, 138683, 154507, 171303, 183818, 196219, 201705])


# Plots: use (x, y) ordering and remove unsupported kwargs
ax.step(años, total_saldo1, label="Deuda Externa Total", color='purple', linewidth=1.5, where='mid')
ax.step(años, total_saldo2, label="Deuda Externa Pública", color='red', linewidth=1.5, where='mid')
ax.stackplot(años, total_saldo, labels=['Deuda Externa Total'], colors=['purple'], alpha=0.3)
ax.stem(años, crpl_saldo1, linefmt='purple', markerfmt='D', basefmt=" ", label="Deuda Externa Total")
ax.stem(años, crpl_saldo2, linefmt='brown', markerfmt='X', basefmt=" ", label="Deuda Externa Total")
ax.plot(años, Amortizaciones1, label="Amortizaciones Largo Plazo Privado", color='cyan', linestyle='--', marker='v')
ax.plot(años, Amortizaciones2, label="Amortizaciones Largo Plazo Público", color='gray', linestyle='--', marker='x')
ax.bar(años - 0.2, desembolsos1, width=0.4, color='lightblue', label="Desembolsos Largo Plazo Privado", alpha=0.5)
ax.bar(años + 0.2, desembolsos2, width=0.4, color='lightgray', label="Desembolsos Largo Plazo Público", alpha=0.5)
ax.bar(años - 0.2, lrpl_saldo1, width=0.4, color='blue', label="Saldo Largo Plazo Privado", alpha=0.7)
ax.bar(años + 0.2, lrpl_saldo2, width=0.4, color='red', label="Saldo Largo Plazo Público", alpha=0.7)


ax.set_title("Colombia: Deuda Externa; Pública y Privada")
ax.grid()
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

