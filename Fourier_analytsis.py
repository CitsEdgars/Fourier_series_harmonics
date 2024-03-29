import numpy as np
import matplotlib.pyplot as plt
from math import log10, floor

def round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(abs(x))))-1)

#Define target function
letter = "G"
letter_ASCII = ord(letter)
letter_binary = bin(letter_ASCII).replace('b','')

bit_count = len(letter_binary)

dx = 0.001
L = 8
x = L * np.arange(0+dx, 1+dx, dx)
n = len(x)
noct = int(np.floor(n/bit_count))

y = []
for letter in letter_binary:
    y.append(int(letter))

f = np.zeros_like(x)
for idx,val in enumerate(y):
    f[idx*noct:(idx+1)*noct] = y[val]

fig, ax = plt.subplots(2)
ax[0].plot(x, f, '-', color = 'k', linewidth = 2)

#Compute Fourier Series
A0 = (np.sum(f) * dx * L) * 2/L
fFS = A0/2

harmonics = 10
A = np.zeros(harmonics)
B = np.zeros(harmonics)
for k in range(harmonics):
    #A(n) = 2*integral(g(t)*sin((2*pi*t)/T))
    A[k] = 2*np.sum(f * np.sin(2*np.pi * (k+1) * x/L)) * dx
    B[k] = 2*np.sum(f * np.cos(2*np.pi * (k+1) * x/L)) * dx
    fFS += A[k]*np.sin((k+1)*2*np.pi*x/L) + B[k]*np.cos((k+1)*2*np.pi*x/L)
    # ax[0].plot(x, fFS, '-')
    
ax[0].plot(x, fFS, '-')
harmonics_list = []

for idx, value in enumerate(A):
    harmonics = np.sqrt(np.square(A[idx]) + np.square(B[idx]))
    harmonics_list.append(harmonics)
    # print("Harmonic {}: {}".format(idx+1,round_sig(harmonics, 4)))
    print("A[{}] coeff was: {}".format(idx+1, round_sig(A[idx])))
    print("B[{}] coeff was: {}".format(idx+1, round_sig(B[idx])))

harmonics_x = np.linspace(1, len(harmonics_list), len(harmonics_list))  
ax[1].set_xticks(np.arange(len(harmonics_list)+1))
ax[1].set_yticks(np.arange(0, 1, .1))
ax[1].bar(harmonics_x, harmonics_list, width = 0.4)

plt.show()