import matplotlib.pyplot as plt
import matplotlib.cm     as cm
from matplotlib.collections import LineCollection as lc
import numpy as np

def myplot(ax,xs,ys,zs, cmap):
    plot = lc([zip(x,y) for (x,y) in zip(xs,ys)], cmap = cmap)
    plot.set_array(np.array(zs))
    x0,x1 = np.amin(xs),np.amax(xs)
    y0,y1 = np.amin(ys),np.amax(ys)
    ax.add_collection(plot)
    ax.set_xlim(x0,x1)
    ax.set_ylim(y0,y1)
    cbar = ax.figure.colorbar(plot, ax=ax)
    cbar.ax.set_ylabel('Fertilizer efficiency', rotation=-90, va="bottom")
    return plot


fig, ax = plt.subplots(figsize=(3.5,3))

X = np.linspace(0.1,6)

efficiencies = np.linspace(5,50,10)

Xs = [X]*len(efficiencies)
Ys = [yi/X for yi in efficiencies]
cmap = cm.viridis

myplot(ax, Xs, Ys, efficiencies, cmap)

ax.plot([min(X), max(X)],[5,5], '-k')
ax.plot([min(X), max(X)],[2,2], '--k')

ax.set_ylim([0,20])

ax.set_xlabel('Ratio of fertilizer price to crop price')
ax.set_ylabel('Value-Cost Ratio (VCR)')

fig.tight_layout()

fig.savefig('VCR.pdf')

plt.show()
