# OFR Wrapper Documentation
This repository contains a Python wrapper to interact with the official Office of Financial Research (OFR) API.
OFR's API does not require tokens or registration, so feel free to use it immediately.

# Short Term Funding Monitor
Short-term funding markets are the core of liquidity and maturity transformation in financial markets. They provide financing for financial institutions, serve as alternatives to deposits for cash investors, and can be used to obtain securities. However, as unavoidable consequences of their functions, these critical markets are vulnerable to disruptions. Problems faced by financial institutions or other parts of the financial system often appear as stresses in short-term funding markets. As part of the Office of Financial Research’s mission to promote and monitor financial stability, the OFR collects a variety of data on these markets. The Short-term Funding Monitor presents these data and places them in context with other data sources.

## Get Series Information (get_series_info)

### metadata_mnemonics
Returns all series available through the API. If no parameters are specified, then this route returns a list of all mnemonics. Using a parameter returns a list of hashes that contain the mnemonic along with the series name.

```python
OFR.get_series_info.metadata_mnemonics(**kwargs)
```

#### Parameters
| Parameter | Type  | Description                                                                                                                                                   |
|-----------|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `dataset` | `str` | The dataset for which you want to retrieve mnemonics. Available data sets can be queried by the following keys: ["mmf", "repo", "fnyr", "nypd", "tyld"]       |
| `output`  | `str` | The only allowable output value is "by_dataset" which will return a hash with the top-level keys being the datasets and their value being a list of mnemonic. |

#### Returns
- `pd.DataFrame`: A DataFrame containing the metadata mnemonics data.


### metadata_query
Returns specific metadata for the given mnemonic. Series metadata is organized into fields; some fields have subfields. If you do not specify the fields parameter, all the metadata for that mnemonic is returned. The metadata is returned as a single hash with the field names and their value.

```python
OFR.get_series_info.metadata_query(mnemonic, **kwargs)
```

#### Parameters
| Parameter  | Type  | Description                                                                                                                                                      |
|------------|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `mnemonic` | `str` | The mnemonic for which you want to retrieve metadata. **This parameter is required**.                                                                            |
| `fields`   | `str` | The fields you want to retrieve. You can retrieve multiple fields by separating them with commas. To access a subfield of a field use a / eg: release/long_name. |

#### Returns
- `pd.DataFrame`: A DataFrame containing the metadata query data.


### metadata_search
Returns a list of data sets and series that contain field values that match the given search query. The results are returned with the following fields:
- mnemonic: unique identifier for the series
- dataset: identifier for the data set that the series is a part of
- field: the metadata field that satisfies the search query
- value: the value of the field that satisfies the search query
- type: format of the data within the field

If the metadata is at the data set level, then "mnemonic" will be "none".

```python
OFR.get_series_info.metadata_search(query)
```

#### Parameters
| Parameter | Type  | Description                                                                                    |
|-----------|-------|------------------------------------------------------------------------------------------------|
| `query`   | `str` | The value for which you want to search. * and ? are supported. **This parameter is required**. |

#### Returns
- `pd.DataFrame`: A DataFrame containing the metadata search by query data.


## Get Series Data (get_series_data)

### series_timeseries
Returns the series for the given mnemonic as a list of date/value pairs. Each mnemonic is required to have an aggregation series and that is the default subseries returned. You can specify a different subseries to return.

```python
OFR.STFM.get_series_data.series_timeseries(query, **kwargs)
```

#### Parameters
| Parameter      | Type  | Description                                                                                                                                                               |
|----------------|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `mnemonic`     | `str` | The unique identifier for the series for which you want to retrieve data. ****This parameter is required****.                                                             |
| `label`        | `str` | The specific subseries to return. Possible labels are: "aggregation" and "disclosure_edits". By default the "aggregation" subseries is returned.                          |
| `start_date`   | `str` | First date in "YYYY-MM-DD" format for which you want to receive data. If no start_date is given, "1901-01-01" is used.                                                    |
| `end_date`     | `str` | Last date in "YYYY-MM-DD" format for which you want to receive data. If no start_date is given, "1901-01-01" is used.                                                     |
| `periodicity`  | `str` | Converts the series to the given periodicity. Available values are: ["A", "AS", "D", "M", "MS", "W", "B", "BM", "BMS", "Q", "BQ", "QS", "BQS", "BA", "BAS"]               |
| `how`          | `str` | How to calculate the value for the given periodicity. By default the last value in that period is given. Available values are: ["first", "last", "mean", "median", "sum"] |
| `remove_nulls` | `str` | If this parameter is set to "true" all nulls in the series will be removed.                                                                                               |
| `time_format`  | `str` | The format for the dates in the series. By default they are returned as strings in the format: YYYY-MM-DD. Available values are: ["date", "ms"]                           |

#### Returns
- `pd.DataFrame`: A DataFrame containing the timeseries data.


### calc_spread
Returns the difference between the data points of two specified series. It will compute the spread of the aggregation subseries by calculating the difference between the first mnemonic (x) and the second mnemonic (y).

```python
OFR.STFM.get_series_data.calc_spread(x, y, **kwargs)
```
#### Parameters
| Parameter      | Type  | Description                                                                                                                                                               |
|----------------|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `x`            | `str` | The mnemonic (unique identifier) for the first series that you want to use as the base of the calculation. **This parameter is required**.                                |
| `y`            | `str` | The mnemonic (unique identifier) for the second series that will be subtracted from x. **This parameter is required**.                                                    |
| `start_date`   | `str` | First date in "YYYY-MM-DD" format for which you want to receive data. If no start_date is given, "1901-01-01" is used.                                                    |
| `end_date`     | `str` | Last date in "YYYY-MM-DD" format for which you want to receive data. If no start_date is given, "1901-01-01" is used.                                                     |
| `periodicity`  | `str` | Converts the series to the given periodicity. Available values are: ["A", "AS", "D", "M", "MS", "W", "B", "BM", "BMS", "Q", "BQ", "QS", "BQS", "BA", "BAS"]               |
| `how`          | `str` | How to calculate the value for the given periodicity. By default the last value in that period is given. Available values are: ["first", "last", "mean", "median", "sum"] |
| `remove_nulls` | `str` | If this parameter is set to "true" all nulls in the series will be removed.                                                                                               |
| `time_format`  | `str` | The format for the dates in the series. By default they are returned as strings in the format: YYYY-MM-DD. Available values are: ["date", "ms"]                           |

#### Returns
- `pd.DataFrame`: A DataFrame containing the spread between two timeseries data.


## Get Series Information & Data (get_series_info_data)

### series_full
Returns all the data and metadata for the given series. A hashed object is returned with a top-level key of the mnemonic.

| Dataframe      | Description                                                                                                           |
|----------------|-----------------------------------------------------------------------------------------------------------------------|
| `timeseries`   | Contains each of the series of data points associated with this mnemonic. Each series is keyed by its subseries name. |
| `metadata`     | Contains a full hash of all series information associated with this mnemonic.                                         |

```python
OFR.STFM.get_series_data.series_full(mnemonic, **kwargs)
```

#### Parameters
| Parameter      | Type  | Description                                                                                                                                                               |
|----------------|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `mnemonic`     | `str` | The unique identifier for the series for which you want to retrieve data. ****This parameter is required****.                                                             |
| `start_date`   | `str` | First date in "YYYY-MM-DD" format for which you want to receive data. If no start_date is given, "1901-01-01" is used.                                                    |
| `end_date`     | `str` | Last date in "YYYY-MM-DD" format for which you want to receive data. If no start_date is given, "1901-01-01" is used.                                                     |
| `periodicity`  | `str` | Converts the series to the given periodicity. Available values are: ["A", "AS", "D", "M", "MS", "W", "B", "BM", "BMS", "Q", "BQ", "QS", "BQS", "BA", "BAS"]               |
| `how`          | `str` | How to calculate the value for the given periodicity. By default the last value in that period is given. Available values are: ["first", "last", "mean", "median", "sum"] |
| `remove_nulls` | `str` | If this parameter is set to "true" all nulls in the series will be removed.                                                                                               |
| `time_format`  | `str` | The format for the dates in the series. By default they are returned as strings in the format: YYYY-MM-DD. Available values are: ["date", "ms"]                           |

#### Returns
- `(pd.DataFrame, pd.DataFrame)`: A tuple of two DataFrames containing the data and metadata for the given series.


### series_multifull
Returns all the data and metadata for all given series. A hashed object is returned with a top-level key of the mnemonic. Below that are two keys:

| Dataframe      | Description                                                                                                           |
|----------------|-----------------------------------------------------------------------------------------------------------------------|
| `timeseries`   | Contains each of the series of data points associated with this mnemonic. Each series is keyed by its subseries name. |
| `metadata`     | Contains a full hash of all series information associated with this mnemonic.                                         |

```python
OFR.STFM.get_series_data.series_full(mnemonics, **kwargs)
```

#### Parameters
| Parameter      | Type  | Description                                                                                                                                                               |
|----------------|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `mnemonics`    | `str` | Comma separated list of mnemonics (unique identifiers) for all series for which you want to retrieve data. ****This parameter is required****.                            |
| `start_date`   | `str` | First date in "YYYY-MM-DD" format for which you want to receive data. If no start_date is given, "1901-01-01" is used.                                                    |
| `end_date`     | `str` | Last date in "YYYY-MM-DD" format for which you want to receive data. If no start_date is given, "1901-01-01" is used.                                                     |
| `periodicity`  | `str` | Converts the series to the given periodicity. Available values are: ["A", "AS", "D", "M", "MS", "W", "B", "BM", "BMS", "Q", "BQ", "QS", "BQS", "BA", "BAS"]               |
| `how`          | `str` | How to calculate the value for the given periodicity. By default the last value in that period is given. Available values are: ["first", "last", "mean", "median", "sum"] |
| `remove_nulls` | `str` | If this parameter is set to "true" all nulls in the series will be removed.                                                                                               |
| `time_format`  | `str` | The format for the dates in the series. By default they are returned as strings in the format: YYYY-MM-DD. Available values are: ["date", "ms"]                           |

#### Returns
- `(pd.DataFrame, pd.DataFrame)`: A tuple of two DataFrames containing the data and metadata for the given series.


### series_dataset
Returns all the data for a specific dataset. If no specific dataset is given, then a hash containing only basic information about each data set is returned.

```python
OFR.STFM.get_series_data.series_dataset(datset, **kwargs)
```

#### Parameters
| Parameter      | Type  | Description                                                                                                                                                                             |
|----------------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `dataset`      | `str` | The specific data set for which to return the underlying series information and data. Available data sets can be queried by the following keys: ["mmf", "repo", "fnyr", "nypd", "tyld"] |
| `vintage`      | `str` | If the vintage isn’t specified then the whole datasets (preliminary, final, and "as of") will be returned. The valid values for this parameter are: ["p", "f", "a"]                     |
| `start_date`   | `str` | First date in "YYYY-MM-DD" format for which you want to receive data. If no start_date is given, "1901-01-01" is used.                                                                  |
| `end_date`     | `str` | Last date in "YYYY-MM-DD" format for which you want to receive data. If no start_date is given, "1901-01-01" is used.                                                                   |
| `periodicity`  | `str` | Converts the series to the given periodicity. Available values are: ["A", "AS", "D", "M", "MS", "W", "B", "BM", "BMS", "Q", "BQ", "QS", "BQS", "BA", "BAS"]                             |
| `how`          | `str` | How to calculate the value for the given periodicity. By default the last value in that period is given. Available values are: ["first", "last", "mean", "median", "sum"]               |
| `remove_nulls` | `str` | If this parameter is set to "true" all nulls in the series will be removed.                                                                                                             |
| `time_format`  | `str` | The format for the dates in the series. By default they are returned as strings in the format: YYYY-MM-DD. Available values are: ["date", "ms"]                                         |

#### Returns
- `(pd.DataFrame, pd.DataFrame)`: A tuple of two DataFrames containing the data and metadata for the dataset.

# U.S. Money Market Fund Monitor

- [ ] TODO (Work in progress): Add the capability to download any data from the OFR's U.S. Money Market Fund Monitor.
