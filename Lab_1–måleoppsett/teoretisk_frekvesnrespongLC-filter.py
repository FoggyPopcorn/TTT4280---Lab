import numpy as np
import matplotlib.pyplot as plt

# Component values (example, can be changed)
L = 100e-3      # 100 mH
C1 = 100e-6     # 100 uF
C2 = 470e-6     # 470 uF
C3 = 100e-9     # 100 nF

# Total equivalent capacitance
C_tot = (C1 * (C2 + C3)) / (C1 + (C2 + C3))

# Frequency range
f = np.logspace(0, 5, 1000)  # 100 Hz to 100 kHz
w = 2 * np.pi * f
s = 1j * w

# System function H(s)
H = 1 / (1 + (s**2) * L * C_tot)

# Magnitude in dB
H_mag_db = 20 * np.log10(np.abs(H))

# Plot
plt.figure()
plt.semilogx(f, H_mag_db)
plt.xlabel("Frekvens [Hz]")
plt.ylabel("Amplitude |H(jω)| [dB]")
plt.title("Teoretisk frekvensresponds av LP-filteret")
plt.grid(True, which="both")
plt.show()
