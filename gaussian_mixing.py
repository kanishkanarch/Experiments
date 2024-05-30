import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

x = np.arange(-200,200,.01)

input_means = []
bhatt_means = []

def update(val):
    mean1 = s1.val
    std1 = s2.val
    mean2 = s3.val
    std2 = s4.val

    variance1 = np.square(std1)
    f1 = np.exp(-np.square(x-mean1)/2*variance1)/(np.sqrt(2*np.pi*variance1))
    f1 *= 1/(0.1*np.sum(f1))

    variance2 = np.square(std2)
    f2 = np.exp(-np.square(x-mean2)/2*variance2)/(np.sqrt(2*np.pi*variance2))
    f2 *= 1/(0.1*np.sum(f2))

#    f3_1 = np.minimum(f1, f2)
#    f3_2 = np.multiply(f1, f2)**0.5
#    f3 = np.multiply(f3_1, f3_2)
#    f3 *= 1/(0.1*np.sum(f3))
    f3 = (np.multiply(f1, f2))**0.5

    ax1.clear()
    ax1.fill_between(x, 0, f1, facecolor="grey", alpha=0.5)
    ax1.fill_between(x, 0, f2, facecolor="blue", alpha=0.5)
    ax1.set_ylim([0, 0.0042])

    ax2.clear()
    ax2.fill_between(x, 0, f3, facecolor="red", alpha=0.5)
    ax2.set_ylim([0, 0.00300])
#    ax2.plot(x, x)
#    ax2.plot(x, np.mean(f3))
    ax2.set_ylabel('Bhattacharya distribution')

    plt.draw()

fig = plt.figure(figsize=(10, 8))
gs = fig.add_gridspec(4, 4, height_ratios=[3, 3, 1, 1], width_ratios=[10, 1, 1, 1], wspace=0.72, hspace=0.2)

ax1 = fig.add_subplot(gs[0:2, 0])
ax1.set_ylim([0, 0.00300])
ax2 = fig.add_subplot(gs[2:, 0])
ax_slider1 = fig.add_subplot(gs[0, 1])
ax_slider2 = fig.add_subplot(gs[0, 2])
ax_slider3 = fig.add_subplot(gs[1, 1])
ax_slider4 = fig.add_subplot(gs[1, 2])

s1 = Slider(ax=ax_slider1, label='Mean 1', valmin=-100, valmax=100, valinit=0)
s2 = Slider(ax=ax_slider2, label='Std 1', valmin=0, valmax=0.5, valinit=0.05)
s3 = Slider(ax=ax_slider3, label='Mean 2', valmin=-100, valmax=100, valinit=-2)
s4 = Slider(ax=ax_slider4, label='Std 2', valmin=0, valmax=0.5, valinit=0.05)

s1.on_changed(update)
s2.on_changed(update)
s3.on_changed(update)
s4.on_changed(update)

update(0)
plt.show()
