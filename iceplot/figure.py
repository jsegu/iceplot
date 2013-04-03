"""ice.figure

Provide GridFigure class and derivatives, where the figure size is computed from a given map size and an axes grid.
"""

from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from mpl_toolkits.axes_grid1.axes_grid import ImageGrid

mm = 1/25.4
pad  = 5.

### GridFigure class ###

class GridFigure(Figure):
	"""Gridded figure with arbitrary cols and rows and optional colorbars"""

	def __init__(self, mapsize, nrows_ncols, cbar_mode=None, cbar_location='right', sideplot=False, **kwargs):
		"""Compute figure size and initialize axes grid"""

		# compute axes grid size
		(mapw, maph) = mapsize
		(rows, cols) = nrows_ncols
		gridw = cols*(mapw+pad)-pad
		gridh = rows*(maph+pad)-pad
		if cbar_mode is 'each' and cbar_location is 'right':
			gridw += 3*cols*pad
		if cbar_mode is 'each' and cbar_location is 'top':
			gridh += 3*cols*pad
		if cbar_mode is 'single' and cbar_location is 'right':
			gridw += 3*pad
		if cbar_mode is 'single' and cbar_location is 'top':
			gridh += 3*pad
		#gridsize=(gridw*mm,gridh*mm)

		# compute figure size
		figw = gridw + 3*pad
		figh = gridh + 2*pad
		if sideplot:
			figw = figw + figh - 2*pad

		# initialize figure
		Figure.__init__(self, **kwargs)
		self.set_size_inches(figw*mm,figh*mm)
		rect = (pad/figw, pad/figh, gridw/figw, gridh/figh)

		# create axes grid
		self.grid = ImageGrid(self, rect,
			nrows_ncols=nrows_ncols, axes_pad=pad*mm,
			cbar_mode=cbar_mode, cbar_location=cbar_location,
			cbar_pad=pad*mm, cbar_size=pad*mm)

		# initialize map labels [left, right, top, bottom]
		for ax in self.grid:
			ax.maplabels=[False, False, False, False]

		# add right labels in the last column
		for ax in self.grid.axes_column[-1]:
			ax.maplabels[1]=True

		# add bottom labels in the last row
		for ax in self.grid.axes_row[-1]:
			ax.maplabels[3]=True

		# add more axes
		if sideplot:
			self.add_axes([(gridw+4*pad)/figw, 2*pad/figh, (maph-2*pad)/figw, (maph-2*pad)/figh])

### Derivative classes ###

class SimpleFigure(GridFigure):
	"""Simple figure with optional colorbar"""

	def __init__(self, mapsize, **kwargs):
		GridFigure.__init__(self, mapsize, (1,1), **kwargs)

class DoubleInlineFigure(GridFigure):
	"""Double inline figure with optional colorbar"""

	def __init__(self, mapsize, **kwargs):
		GridFigure.__init__(self, mapsize, (1,2), **kwargs)

