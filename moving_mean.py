import progressbar
import pdb
import numpy as np
import matplotlib.pyplot as plt

means = np.arange(-200, 200, 0.01)

mean1 = 0
std1 = 0.5
variance1 = np.square(std1)

std2 = 0.5
variance2 = np.square(std2)

f1 = np.exp(-np.square(means-mean1)/2*variance1)/(np.sqrt(2*np.pi*variance1)) # Ideal distribution

mean_orig = []
mean_bhatt = []
std_bhatt = []
max_bhatt = []

bar = progressbar.ProgressBar(
        maxval = len(means),
        widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]
        )

bar.start()
i = 0
for mean in means:
    i += 1
    if mean < -100 or mean > 100:
        continue
    mean_orig.append(mean)

    f2 = np.exp(-np.square(means-mean)/2*variance2)/(np.sqrt(2*np.pi*variance2))

    bhatt_dist = (np.multiply(f1, f2))**0.5

    this_mean = np.sum(np.multiply(means, bhatt_dist))/np.sum(bhatt_dist)
    this_std = (np.sum((bhatt_dist - this_mean)**2)/len(bhatt_dist))**0.5

    mean_bhatt.append(this_mean)
    std_bhatt.append(this_std)
    max_bhatt.append(np.max(bhatt_dist))

    bar.update(i)

bar.finish()

fig, ax = plt.subplots(2, 2)

ax[0, 0].plot(mean_orig, mean_bhatt)
ax[0, 0].set_title("Moving dist mean vs Bhatt dist mean")

ax[0, 1].plot(mean_orig, std_bhatt)
ax[0, 1].set_title("Moving dist mean vs Bhatt dist std")

ax[1, 0].plot(mean_orig, max_bhatt)
ax[1, 0].set_title("Moving dist mean vs Bhatt dist max (height)")

#ax[1, 1].plot(mean_orig, mean_orig)
ax[1, 1].set_title("Blank")

plt.show()
