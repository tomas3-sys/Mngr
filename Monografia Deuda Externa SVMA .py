import matplotlib.pyplot as plt
import numpy as np
# FIGURA 2 
fig, ax = plt.subplots()
años = ["2000", "2001", "2002", "2003","2004", "2005", "2006", "2007", "2008", "2009","2010", "2011", "2012", 
        "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020","2021", "2022", "2023", "2024"]
Desembolsos = {"Des":[85, 46, 135, 365, 432, 378, 501, 656, 1004, 1797, 1039, 1467, 1051, 
                      1096, 1144, 1493, 470, 692, 740, 1179, 384, 903, 1912, 1831, 684]}
Amortizaciones = {"Amo":[194, 257, 295, 683, 310, 262, 439, 540, 726, 1064, 1017, 926, 
                         824, 911, 873, 936, 748, 793, 844, 633, 548, 633, 1446, 1713, 611]}
Intereses = {"Int":[200, 208, 203, 198, 189, 168, 188, 185, 214, 308, 289, 269, 280, 
                    299, 306, 340, 362, 360, 343, 370, 282, 259, 274, 296, 297]}
Saldo_Vigente = {"SV":[2717, 2507, 2347, 2028, 2151, 2267, 2328, 2444, 2722, 3455, 3477, 4018, 4245,
                       4431, 4701, 5259, 4981, 4880, 4776, 5321, 5156, 5863, 5971, 6044]}

ax.set_title("Deuda Externa Privada")
ax.plot(años, Desembolsos["Des"], marker = "o")
ax.plot(Amortizaciones["Amo"], marker = "^")
ax.plot(Intereses["Int"], marker = "*")
ax.plot(Saldo_Vigente["SV"], marker = "D")
ax.grid()
ax.legend(["Desembolsos", "Amortizaciones", "Intereses", "Saldo Vigente"])
ax.set_xlabel("Año fiscal")
ax.set_ylabel("Millones de Dólares (USD)")

plt.show()