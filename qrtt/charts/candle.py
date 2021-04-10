import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as md
from matplotlib import gridspec



def candle(ohlcv, show_ticks=True, show_grid=False):
    dates = [str(date) for date in ohlcv.index.date]
    
    _o, _h, _l, _c, _v = ohlcv['open'], ohlcv['high'], ohlcv['low'], ohlcv['close'], ohlcv['volume']

    colors_bool = _c >= _o
    colors = np.where(colors_bool, 'green', 'red')

    plt.rcParams["figure.figsize"] = (7,7)
    plt.style.use('fast')
#     

    # gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1])
    gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1], hspace=0.1)

    fig, ax = plt.subplots(2,1,sharex=True)

    ax[0] =  plt.subplot(gs[0,:])
    ax[1] =  plt.subplot(gs[1,:])

    ax[0].bar(dates, (_c - _o), 0.8, bottom=_o, color=colors, edgecolor=None, zorder=3) #edgecolor=colors, 
    ax[0].vlines(dates, _l, _h, color=colors, linewidths=1.5)
    ax[1].bar(dates, _v,color=colors)
    

    
    if show_ticks:
        ax[1].set_xticks(dates[::round(len(dates)/5)])
    else:
        ax[0].tick_params(axis='both', left=False, top=False, right=False, bottom=False, labelleft=False, labeltop=False, labelright=False, labelbottom=False)
        ax[1].tick_params(axis='both', left=False, top=False, right=False, bottom=False, labelleft=False, labeltop=False, labelright=False, labelbottom=False)

        
    if show_grid:
        ax[0].grid(color='r', linestyle='-', linewidth=2)

        
    # plt.legend()
    plt.gcf().autofmt_xdate()
    plt.show()

