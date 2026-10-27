import matplotlib.pyplot as plt
import numpy as np
# catherine eileen huerta rascon NC = 0072

cant_productos = [100,150,200,300,500]
precio = [4000,7000,9000,12000,18000]

plt.plot(cant_productos,precio)
plt.show()

# perzonalizar grafica
plt.plot(cant_productos,precio, color = "green", marker = "o", linestyle = "dashed", linewidth = 2, markersize = 12)
plt.title("venta de walmart 0072")
plt.xlabel("cant prod")
plt.ylabel("precio")
plt.show()

print("catherine eileen huerta rascon NC = 0072")