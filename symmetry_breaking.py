
import numpy as np
import matplotlib.pyplot as plt

# Return probability function
def return_probability(N, t, E=1.0, hbar=1.0):
    k = np.arange(N)
    Ek = E * (1 - np.cos(2*np.pi*k/N))
    amp = np.mean(np.exp(-1j * Ek * t / hbar))
    return np.abs(amp)**2


# Time values
t_values = np.linspace(0, 50, 2000)

# Create subplot figure
fig, axes = plt.subplots(2, 2, figsize=(10,8))

Ns = [2,3,4,5]

for ax, N in zip(axes.flatten(), Ns):
    
    prob = [return_probability(N, t) for t in t_values]
    
    ax.plot(t_values, prob)
    ax.set_title(f"N = {N}")
    ax.set_xlabel("t")
    ax.set_ylabel(r"$|\psi(0,t)|^2$")
    ax.set_ylim(0,1.05)
    ax.grid(True)

plt.tight_layout()
plt.show()
