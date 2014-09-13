"""
Plot surface velocity streamlines.
"""

from netCDF4 import Dataset
from matplotlib import pyplot as plt
from iceplot import plot as iplt
from iceplot import autoplot as aplt

# load data
nc = Dataset('pism_plot_sample.nc')

# plot
im = aplt.streamplot(nc, 'velsurf')
iplt.icemargin(nc)

# show
nc.close()
plt.show()
