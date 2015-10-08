""":mod:`iceplotlib.animation`

Draw animations.
"""

from matplotlib.animation import FFMpegFileWriter, FuncAnimation
from iceplotlib.plot import gca

### Customized MovieWriter class ###

class IceWriter(FFMpegFileWriter):

  def __init__(self, temp_prefix='_tmp', clear_temp=True, *args, **kwargs):

    FFMpegFileWriter.__init__(self, *args, **kwargs)
    self.temp_prefix=temp_prefix
    self.clear_temp=clear_temp

  def setup(self, fig, outfile, dpi):

    return FFMpegFileWriter.setup(self, fig, outfile, dpi,
      frame_prefix=self.temp_prefix,
      clear_temp=self.clear_temp)

### Animations ###

def _animate_mapaxes_method(name):
    """Transform a plotting method into an animation function"""
    def func(nc, *args, **kwargs):
        ax = gca()
        frames = kwargs.pop('frames', range(len(nc.dimensions['time'])))
        def update(t):
            ax.cla()
            getattr(ax, name)(nc, *args, t=t, **kwargs)
        update(frames[0])
        return FuncAnimation(ax.figure, update, frames)
    return func

iceanim = _animate_mapaxes_method('icemap')
