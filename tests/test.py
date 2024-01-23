from OFR.STFM.get_series_info import *
from OFR.STFM.get_series_data import *
from OFR.STFM.get_series_info_data import *


def test_metadata_mnemonics():
    assert isinstance(metadata_mnemonics(), pd.DataFrame)
    assert isinstance(metadata_mnemonics(dataset="nypd"), pd.DataFrame)
    assert isinstance(metadata_mnemonics(output="by_dataset"), pd.DataFrame)


def test_metadata_query():
    assert isinstance(metadata_query(mnemonic="REPO-DVP_AR_LE30-P"), pd.DataFrame)
    assert isinstance(metadata_query(mnemonic="REPO-DVP_AR_LE30-P", fields="release/long_name"), pd.DataFrame)


def test_metadata_search():
    assert isinstance(metadata_search(query="Outstanding*"), pd.DataFrame)
    assert isinstance(metadata_search(query="*dvp*"), pd.DataFrame)


def test_series_timeseries():
    assert isinstance(series_timeseries(mnemonic="REPO-DVP_AR_G30-P"), pd.DataFrame)
    assert isinstance(series_timeseries(mnemonic="REPO-DVP_AR_G30-P", label="disclosure_edits"), pd.DataFrame)
    assert isinstance(series_timeseries(mnemonic="REPO-DVP_AR_G30-P", periodicity="W", how="mean"), pd.DataFrame)


def test_calc_spread():
    assert isinstance(calc_spread(x="REPO-GCF_AR_G30-P", y="REPO-TRI_AR_AG-P"), pd.DataFrame)


def test_series_full():
    assert isinstance(series_full(mnemonic="REPO-DVP_AR_LE30-P"), (pd.DataFrame, pd.DataFrame))
    assert isinstance(series_full(mnemonic="REPO-DVP_AR_G30-P", start_date="2020-02-01", end_date="2020-02-26"), (pd.DataFrame, pd.DataFrame))


def test_series_multifull():
    assert isinstance(series_multifull(mnemonics="REPO-DVP_AR_G30-P,REPO-DVP_AR_LE30-P"), (pd.DataFrame, pd.DataFrame))


def test_series_dataset():
    assert isinstance(series_dataset(), (pd.DataFrame, pd.DataFrame))
    assert isinstance(series_dataset(dataset="tyld"), (pd.DataFrame, pd.DataFrame))


if __name__ == "__main__":
    test_metadata_mnemonics()
    test_metadata_query()
    test_metadata_search()
    test_series_timeseries()
    test_series_full()
    test_series_dataset()
