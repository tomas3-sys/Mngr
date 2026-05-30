import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
# FIGURA 2 
fig, ax = plt.subplots(2, 4, figsize=(12, 64))
año1970 = (0.1074, 0.2367, 0.2160, 0.3194, 0.2475)
año1975 = (0.1080, 0.2461, 0.2237, 0.3014, 0.2676)
año1980 = (0.1096, 0.3387, 0.2584, 0.3803, 0.2873)
año1985 = (0.1064, 0.3381, 0.2915, 0.3790, 0.3442)
año1990 = (0.1418, 0.3534, 0.3147, 0.3301, 0.3831)
año1995 = (0.1477, 0.3847, 0.3669, 0.3616, 0.4689)
año2000 = (0.1871, 0.3921, 0.4605, 0.3895, 0.5698)

# Convert values to percentage labels
año1970_labels = [f"{x*100:.2f}%" for x in año1970]
año1975_labels = [f"{x*100:.2f}%" for x in año1975]
año1980_labels = [f"{x*100:.2f}%" for x in año1980]
año1985_labels = [f"{x*100:.2f}%" for x in año1985]
año1990_labels = [f"{x*100:.2f}%" for x in año1990]
año1995_labels = [f"{x*100:.2f}%" for x in año1995]
año2000_labels = [f"{x*100:.2f}%" for x in año2000]

ax[0,0].pie(año1970, colors=["Red", "Blue", "Green", "Orange", "Purple"], center =(0, 0), radius=1.3, pctdistance=0.7,
            labels=año1970_labels)
ax[0,1].pie(año1975, colors=["Red", "Blue", "Green", "Orange", "Purple"], center =(0, 0), radius=1.3, pctdistance=0.7,
            labels=año1975_labels)
ax[0,2].pie(año1980, colors=["Red", "Blue", "Green", "Orange", "Purple"], center =(0, 0), radius=1.3, pctdistance=0.7,
            labels=año1980_labels)
ax[0,3].pie(año1985, colors=["Red", "Blue", "Green", "Orange", "Purple"], center =(0, 0), radius=1.3, pctdistance=0.7,
            labels=año1985_labels)
ax[1,0].pie(año1990, colors=["Red", "Blue", "Green", "Orange", "Purple"], center =(0, 0), radius=1.3, pctdistance=0.7,
            labels=año1990_labels)
ax[1,1].pie(año1995, colors=["Red" ,"Blue" ,"Green" ,"Orange" ,"Purple"], center =(0, 0), radius=1.3, pctdistance=0.7,
            labels=año1995_labels)
ax[1,2].pie(año2000, colors=["Red", "Blue", "Green", "Orange", "Purple"], center =(0, 0), radius=1.3, pctdistance=0.7,
            labels=año2000_labels)
ax.flat[0].set_title("1970"), ax.flat[1].set_title("1975"), ax.flat[2].set_title("1980"), ax.flat[3].set_title("1985")
ax.flat[4].set_title("1990"), ax.flat[5].set_title("1995"), ax.flat[6].set_title("2000"), ax.flat[7].set_visible(False)

# Create legend
legend_labels = ["Colombia", "América Latina", "OECD", "Ingresos Medianos-Bajos", "Asia Oriente-Pacífico"]
legend_colors = ["Red", "Blue", "Green", "Orange", "Purple"]
legend_patches = [mpatches.Patch(color=color, label=label) for color, label in zip(legend_colors, legend_labels)]
fig.legend(handles=legend_patches, loc='upper center', bbox_to_anchor=(0.5, -0.02), ncol=5, frameon=True, fontsize=10)
fig.suptitle("Distribución porcentual del ingreso nacional bruto per cápita de Colombia en comparación con otros grupos de países, 1970-2000", fontsize=16)

plt.tight_layout()
plt.show()