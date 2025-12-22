import numpy as np
import matplotlib.pyplot as plt

try:
    from noise import pnoise2
except ImportError:
    raise ImportError("install noise u bum")

seed = np.random.randint(0, 100000)
dim = 4096
noise_map = np.zeros((dim, dim))
for y in range(dim):
    nx = x / 50
    ny = y / 50
    noise_value = pnoise(nx, ny, octaves=6, persistance=0.5, lacunarity=2.0)