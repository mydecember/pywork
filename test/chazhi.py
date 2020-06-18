import numpy as np
import matplotlib.pyplot as plt
import math
# refer
# https://blog.csdn.net/u010592995/article/details/73555425/
def showSinc():
    N = 15
    f = 1.0
    Fs = 10
    Ts = 0.1

    T = N*Ts
    n = np.arange(0, N)
    n = n.astype(np.float)
    NP = math.floor((1/f)/Ts)

    nTs = n*Ts
    ts = np.arange(0, Ts * (N), Ts)
    x = np.sin(2*math.pi*f*ts)

# samples first
    plt.subplot(311)
    plt.stem(ts, x)
    plt.title('sample signal')

    Ts1 = 0.001;
    t1 = np.arange(0, T/Ts1-1)*Ts1
    f1 = np.sin(2*np.pi*t1);
    plt.hold
    plt.plot(t1, f1, 'r-')


    # x(n)=f
    # T=Ts
    #
    t1 = 0
    t2 = 1/f
    interpfac = 3
    fs_sinc = interpfac*Fs

    Dt = Ts/interpfac
    t=np.arange(t1, t2, Dt)

    delay = Dt * .0
    ta = np.arange(t1, Ts*N, Dt)
    fa = np.zeros(np.shape(ta))

    for t in range(0, len(ta)):
        for m in range(0, len(nTs)):
            fa[t] = fa[t] + x[m]*np.sinc((t*Dt - delay - m*Ts)/Ts)

    plt.subplot(312);
    plt.stem(ta,fa)
    plt.title('insert')
    plt.show()

def show1():
    N = 15
    f = 1.0
    Fs = 10
    Ts = 0.1

    T = N * Ts
    n = np.arange(0, N)
    n = n.astype(np.float)

    nTs = n * Ts
    ts = np.arange(0, Ts * (N + 1), Ts)
    x = np.sin(2 * math.pi * f * ts)

    plt.subplot(311)
    plt.stem(ts, x)
    plt.title('sample signal')

    Ts1 = 0.001;
    NP1 = math.floor((1 / f) / (Ts1))
    t1 = np.arange(0, T / Ts1 - 1) * Ts1
    f1 = np.sin(2 * np.pi * t1);
    plt.hold
    plt.plot(t1, f1, 'r-')

    # x(n)=f
    # T=Ts
    #
    t1 = 0
    t2 = 1 / f
    interpfac = 3
    fs_sinc = interpfac * Fs

    Dt = Ts / interpfac
    t = np.arange(t1, t2, Dt)

    delay = Dt * .0
    ta = np.arange(t1, Ts * N, Dt)
    fa = np.zeros(np.shape(ta))

    for t in range(0, len(ta)):
        for m in range(0, len(nTs)):
            # fa[t] = fa[t] + x[m] * np.sinc((t * Dt - delay - m * Ts) / Ts)
            fa[t] = fa[t] + x[m] * np.sinc((t - delay - m / 2))

    plt.subplot(312);
    plt.stem(ta, fa)
    plt.title('insert')
    plt.show()

show1()