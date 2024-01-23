from OFR.STFM.base import __encode_url, __read_data_from_url
import pandas as pd


# Mnemonics
# https://www.financialresearch.gov/short-term-funding-monitor/api-specs/api-info-mnemonics/
def metadata_mnemonics(**kwargs) -> pd.DataFrame or list:
    url = __encode_url("metadata/mnemonics", kwargs)
    return __read_data_from_url("metadata/mnemonics", url, **kwargs)


# Single Series Query
# https://www.financialresearch.gov/short-term-funding-monitor/api-specs/api-info-query/
def metadata_query(mnemonic: str, **kwargs) -> pd.DataFrame:
    url = __encode_url("metadata/query", {"mnemonic": mnemonic, **kwargs})
    return __read_data_from_url("metadata/query", url, **kwargs)


# Series Search
# https://www.financialresearch.gov/short-term-funding-monitor/api-specs/api-info-search/
def metadata_search(query: str) -> pd.DataFrame:
    url = __encode_url("metadata/search", {"query": query})
    return __read_data_from_url("metadata/search", url)
