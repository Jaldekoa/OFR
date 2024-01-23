from OFR.STFM.metadata import params_by_endpoint, all_params
from urllib.parse import urlencode
import pandas as pd
import requests


def __encode_url(endpoint: str, params: dict) -> str:
    # Create valid params dict for the endpoint
    valid_params = {el: all_params.get(el, None) for el in params_by_endpoint.get(endpoint, [])}
    # Get only valid parameters from params
    web_params = {k: v for k, v in params.items() if k in valid_params
                  if valid_params[k] is None or v in valid_params[k]}

    # Special case for series/multifull
    if "mnemonics" in params.keys():
        valid_mnemonics = [mnemonic for mnemonic in params["mnemonics"].split(",") if
                           mnemonic in all_params["mnemonic"]]
        web_params.update({"mnemonics": ",".join(valid_mnemonics)})

    # Encode URL params only if there are valid params
    if web_params:
        base_url = "https://data.financialresearch.gov/v1/"
        return f"{base_url}{endpoint}?{urlencode(web_params)}"
    else:
        return f"https://data.financialresearch.gov/v1/{endpoint}"


def __read_data_from_url(endpoint: str, url: str, **params) -> pd.DataFrame or (pd.DataFrame, pd.DataFrame):
    res = requests.get(url).json()
    return reader_by_endpoint[endpoint](res, **params)


def __read_metadata_mnemonics(raw_json: list or dict, **params) -> pd.DataFrame:
    if params.get("dataset", False):
        return pd.DataFrame(raw_json)

    elif params.get("output", False):
        dfs = [pd.json_normalize(raw_json, k).assign(dataset=k) for k, v in raw_json.items()]
        return pd.concat(dfs, ignore_index=True)
    else:
        return pd.DataFrame(raw_json)


def __read_metadata_query(raw_json: dict, **params) -> pd.DataFrame:
    return pd.json_normalize(raw_json, max_level=1)


def __read_metadata_search(raw_json: list, **params) -> pd.DataFrame:
    return pd.DataFrame(raw_json)


def __read_series_timeseries(raw_json: list, **params) -> pd.DataFrame:
    df_data = pd.DataFrame(raw_json, columns=["date", "value"])
    df_data["date"], df_data["value"] = pd.to_datetime(df_data["date"]), pd.to_numeric(df_data["value"],
                                                                                       errors="coerce")
    return df_data


def __read_calc_spread(raw_json: list, **params) -> pd.DataFrame:
    df_data = pd.DataFrame(raw_json, columns=["date", "value"])
    df_data["date"], df_data["value"] = pd.to_datetime(df_data["date"]), pd.to_numeric(df_data["value"],
                                                                                       errors="coerce")
    return df_data


def __read_series_full(raw_json: dict, **params) -> (pd.DataFrame, pd.DataFrame):
    df_timeseries = __read_series_timeseries(raw_json[params["mnemonic"]]
                                             .get("timeseries", {"aggregation": [[]]})
                                             .get("aggregation", [[]]))
    df_metadata = __read_metadata_query(raw_json[params["mnemonic"]]
                                        .get("metadata", {"mnemonic": params["mnemonic"]}))

    return df_timeseries, df_metadata


def __read_series_multifull(raw_json: dict, **params) -> (pd.DataFrame, pd.DataFrame):
    dfs = [__read_series_full({k: v}, params={"mnemonic": k}) for k, v in raw_json.items()]
    timeseries, metadata = [el_one for el_one, el_two in dfs], [el_two for el_one, el_two in dfs]

    return pd.concat(timeseries, ignore_index=True), pd.concat(metadata, ignore_index=True)


def __read_series_dataset(raw_json: dict, **params) -> (pd.DataFrame, pd.DataFrame):
    if params is None:
        return pd.DataFrame([(key, value.get("long_name"), value.get("short_name")) for key, value in raw_json.items()],
                            columns=["database", "long_name", "short_name"])
    else:
        return __read_series_multifull(raw_json["timeseries"], **params)


reader_by_endpoint = {
    "metadata/mnemonics": __read_metadata_mnemonics,
    "metadata/query": __read_metadata_query,
    "metadata/search": __read_metadata_search,

    "series/timeseries": __read_series_timeseries,
    "calc/spread": __read_calc_spread,

    "series/full": __read_series_full,
    "series/multifull": __read_series_multifull,
    "series/dataset": __read_series_dataset,
}
