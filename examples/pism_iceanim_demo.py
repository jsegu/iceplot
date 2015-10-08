"""
Animation demo.
"""

import iceplotlib.plot as iplt
import iceplotlib.animation as iani

# load data
nc = iplt.load('pism_anim_sample.nc')

# animate
iplt.axes(projection='mapaxes')
ani = iani.iceanim(nc, thkth=1.0)

# show
iplt.show()

# to save the animation:
#ani.save('iceanim.mp4')
