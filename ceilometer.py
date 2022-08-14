import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


months_seasons = {
    1: "DJF",
    2: "DJF",
    3: "MAM",
    4: "MAM",
    5: "MAM",
    6: "JJA",
    7: "JJA",
    8: "JJA",
    9: "SON",
    10: "SON",
    11: "SON",
    12: "DJF",
}


if __name__ == "__main__":
    pd.options.plotting.backend = "holoviews"

    df = pd.read_csv(
        "/home/timh/Data/AucklandCeilometer/valid_ceilometer_hourly_average_BLD_estimates.csv"
    ).rename({"hourly_mean_bld_magl": "BLD MAGL"}, axis="columns")

    df["datetime"] = df.apply(
        lambda r: datetime.datetime.strptime(
            r["date"] + " " + r["time_nzdt"], "%Y-%m-%d %H:%M:%S"
        ),
        axis="columns",
    )

    df["season"] = df["datetime"].apply(lambda d: d.month).map(months_seasons)
    df["hour"] = df["datetime"].apply(lambda dt: dt.hour)

    plt.figure(figsize=(10, 8))
    p = sns.lineplot(
        x="hour",
        y="BLD MAGL",
        hue="season",
        data=df,
        palette=sns.color_palette("Set2")[:4],
    )
    p.set_ylabel("Depth (m above ground)")
    p.set_title("Auckland Boundary Layer Depth")
    plt.savefig("auckland_boundary_layer_depth.pdf")

    # p = df[["datetime", "BLD MAGL"]].set_index("datetime").plot()
    # hvplot.show(p)

    # df_hours_seasons = (
    #     df[["hour", "season", "BLD MAGL"]].groupby(["hour", "season"]).agg(np.nanmean)
    # )
    # p2 = df_hours_seasons.plot(col="BLD MAGL")
    # hvplot.show(p2)
