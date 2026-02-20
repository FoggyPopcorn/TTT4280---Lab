import numpy as np
import matplotlib.pyplot as plt

# Komponentverdier (lav resonansfrekvens)
L = 1.0            # 1 H
C_tot = 3.9e-6     # 3.9 uF

# Resonansfrekvens
f0 = 1 / (2*np.pi*np.sqrt(L * C_tot))

# Frekvensakse (mye rom til høyre)
omega = np.logspace(-1, 3, 3000)  # rad/s
s = 1j * omega

# Dempingsfaktorer
zeta_values = [0.05, 0.2, 0.5, 1.0]

plt.figure()

for zeta in zeta_values:
    H = 1 / (1 + 2*zeta*np.sqrt(L*C_tot)*s + L*C_tot*s**2)
    plt.semilogx(omega / (2*np.pi), np.abs(H), label=f"$\\zeta = {zeta}$")

plt.axvline(f0, linestyle="--", linewidth=1.2,
            label=f"$f_0 \\approx {f0:.1f}\\,\\mathrm{{Hz}}$")

plt.xlabel("Frekvens [Hz]")
plt.ylabel("$|H(j\\omega)|$")
plt.title("Frekvensrespons for LC-filter med ulike dempingsfaktorer")
plt.grid(True, which="both")
plt.legend()
plt.show()