import matplotlib
import pandas as pd

matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime, timedelta


def timeline_chart(icds, title="Timeline de los ICD"):
    # In case the above fails, e.g. because of missing internet connection
    # use the following lists as fallback.
    names = icds
    base = datetime.today()
    dates = [base - timedelta(days=x) for x in range(len(names))]
    # dates = ['2019-02-26', '2019-02-26', '2018-11-10', '2018-11-10',
    #          '2018-09-18', '2018-08-10', '2018-03-17', '2018-03-16',
    #          '2018-03-06', '2018-01-18', '2017-12-10', '2017-10-07',
    #          '2017-05-10', '2017-05-02', '2017-01-17', '2016-09-09',
    #          '2016-07-03', '2016-01-10', '2015-10-29', '2015-02-16',
    #          '2014-10-26', '2014-10-18', '2014-08-26']

    # Convert date strings (e.g. 2014-10-18) to datetime
    #dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]

    # Choose some nice levels
    levels = np.tile([-5, 5, -3, 3, -1, 1],
                     int(np.ceil(len(dates) / 6)))[:len(dates)]

    # Create figure and plot a stem plot with the date
    fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
    ax.set(title=title)

    ax.vlines(dates, 0, levels, color="tab:red")  # The vertical stems.
    ax.plot(dates, np.zeros_like(dates), "-o",
            color="k", markerfacecolor="w")  # Baseline and markers on it.

    # annotate lines
    for d, l, r in zip(dates, levels, names):
        ax.annotate(r, xy=(d, l),
                    xytext=(-3, np.sign(l) * 3), textcoords="offset points",
                    horizontalalignment="right",
                    verticalalignment="bottom" if l > 0 else "top")

    # format xaxis with 4 month intervals
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

    # remove y axis and spines
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.spines[["left", "top", "right"]].set_visible(False)

    ax.margins(y=0.1)
    plt.savefig("prueba.png")
    #plt.show()
    return fig

icds=["R50","K56"]
timeline_chart(icds)

