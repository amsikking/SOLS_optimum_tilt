import numpy as np

NA1 = 1.35 # Nikon 100x1.35 Sil
n1 = 1.4 # Silicone refractive index
lambda_ex = 488 # typical laser
lambda_em = 510 # GFP like

theta1 = np.arcsin(NA1/n1)

a = lambda_ex/(np.pi * lambda_em) + np.sin(2 * theta1)
b = 2 * (1 - 2 * (np.sin(theta1) ** 2))
c = - np.sin(2 * theta1)

tan_theta_eff = (- b + (b**2 - 4 * a * c)**0.5)/ (2 * a)
theta_eff = np.arctan(tan_theta_eff)
theta_tilt = np.pi/2 + theta1 - 2 * theta_eff

print("Optimum tilt = ", round(np.rad2deg(theta_tilt), 2), "deg")
