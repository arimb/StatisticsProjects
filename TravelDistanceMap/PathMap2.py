import matplotlib.pyplot as plt
import datashader as ds
import datashader.transfer_functions as tf
import pandas as pd
from colorcet import fire
import numpy as np

import holoviews as hv
import holoviews.plotting.mpl
from holoviews.operation.datashader import datashade

df = pd.read_csv('C:/Users/arimb/Desktop/StLouis.csv')

agg = ds.Canvas().points(df, 'Lng', 'Lat', ds.mean('Density'))

a = tf.shade(agg, cmap=fire, how='log')

hv.extension('bokeh')

hv.RGB(np.dstack([a.r.values, a.g.values, a.b.values])).options(width=450, invert_yaxis=True)

# renderer = hv.Store.renderers['matplotlib'].instance(fig='svg', holomap='gif')
# renderer.save(img, 'test')

# hv.renderer('bokeh').save(img, 'test', fmt='png')