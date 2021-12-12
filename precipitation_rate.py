"""
Caclulates the precipitation rate measured at the LAPUP weather station

Athanassios Argiriou, LAPUP, 2021-12-11
"""

import pandas as pd

years = ["2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]

precipitation = pd.DataFrame()

for i in years:
    my_file = "Meteo_1min_" + i + "_qc.csv"
    df = pd.read_csv(my_file, sep=",", usecols=["Time", "precip"], index_col=[0], parse_dates=True)
    df.dropna(inplace=True)
    precipitation = precipitation.append(df)

rate_1min = precipitation.sort_values('precip', ascending=False)
rate_1min.to_csv("1_min_precipitation_rate_sorted.csv", float_format="%.1f")

rate_1h = precipitation.resample('H').sum()
rate_1h.sort_values('precip', ascending=False, inplace=True)
rate_1h.to_csv("hourly_precipitation_rate_sorted.csv", float_format = "%.1f")

rate_daily = precipitation.resample('D').sum()
rate_daily.sort_values('precip', ascending=False, inplace=True)
rate_daily.to_csv("daily_precipitation_rate_sorted.csv", float_format = "%.1f")
