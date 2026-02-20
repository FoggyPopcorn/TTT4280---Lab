import numpy as np
import matplotlib.pyplot as plt

# Component values
L = 100e-3      # 100 mH
C1 = 100e-6     # 100 uF
C2 = 470e-6     # 470 uF
C3 = 100e-9     # 100 nF

# Equivalent capacitance (pi-filter approximation)
C_tot = (C1 * (C2 + C3)) / (C1 + (C2 + C3))

# Damping resistor from characteristic impedance
R_s = np.sqrt(L / C_tot)

# Frequency range
f = np.logspace(0, 5, 1000)  # 1 Hz to 100 kHz
w = 2 * np.pi * f
s = 1j * w

# Damped system function
H = 1 / (1 + s * R_s * C_tot + (s**2) * L * C_tot)

# Magnitude in dB
H_mag_db = 20 * np.log10(np.abs(H))

# Plot
plt.figure()
plt.semilogx(f, H_mag_db)
plt.xlabel("Frekvens [Hz]")
plt.ylabel("Amplitude |H(jω)| [dB]")
plt.title("Frekvensrespons av LP-filter med seriedemping")
plt.grid(True, which="both")
plt.show()
