from OFR.STFM.base import __encode_url, __read_data_from_url
import pandas as pd


# Single Series
# https://www.financialresearch.gov/short-term-funding-monitor/api-specs/api-full-single/
def series_full(mnemonic: str, **kwargs) -> (pd.DataFrame, pd.DataFrame):
    url = __encode_url("series/full", {"mnemonic": mnemonic, **kwargs})
    return __read_data_from_url("series/full", url, **kwargs)


# Multiple Series
# https://www.financialresearch.gov/short-term-funding-monitor/api-specs/api-full-multi/
def series_multifull(mnemonics: str, **kwargs) -> (pd.DataFrame, pd.DataFrame):
    url = __encode_url("series/multifull", {"mnemonics": mnemonics, **kwargs})
    return __read_data_from_url("series/multifull", url, **kwargs)


# All Series in Data Set
# https://www.financialresearch.gov/short-term-funding-monitor/api-specs/api-full-dataset/
def series_dataset(**kwargs) -> (pd.DataFrame, pd.DataFrame):
    url = __encode_url("series/dataset", kwargs)
    return __read_data_from_url("series/dataset", url, **kwargs)
