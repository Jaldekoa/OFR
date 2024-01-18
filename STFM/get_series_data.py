from OFR.STFM.base import __encode_url, __read_data_from_url
import pandas as pd


# Single Series Data
# https://www.financialresearch.gov/short-term-funding-monitor/api-specs/api-data-single/
def series_timeseries(mnemonic: str, **kwargs) -> pd.DataFrame:
    url = __encode_url("series/timeseries", {"mnemonic": mnemonic, **kwargs})
    return __read_data_from_url("series/timeseries", url, **kwargs)


# Series Spread
# https://www.financialresearch.gov/short-term-funding-monitor/api-specs/api-data-spread/
def calc_spread(x: str, y: str, **kwargs) -> pd.DataFrame:
    url = __encode_url("calc/spread", {"x": x, "y": y, **kwargs})
    return __read_data_from_url("calc/spread", url, **kwargs)
