# OFR-Wrapper
Este repositorio contiene un Wrapper de Python para interactuar con la API oficial de la Office of Financial Research (OFR).

## Get Series Information (get_series_info)

### metadata_mnemonics
Returns all series available through the API. If no parameters are specified, then this route returns a list of all mnemonics. Using a parameter returns a list of hashes that contain the mnemonic along with the series name.

```python
OFR.get_series_info.metadata_mnemonics(**kwargs)
```

| Parameter | Type  | Description                                                                                                                                                   |
|-----------|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `dataset` | `str` | The dataset for which you want to retrieve mnemonics. Available data sets can be queried by the following keys: {"mmf": OFR U.S. Money Market Fund Data Release, "repo": OFR U.S. Repo Markets Data Release, "fnyr": Federal Reserve Bank of New York Reference Rates, "nypd": Federal Reserve Bank of New York Primary Dealer Statistics, "tyld": Treasury Constant Maturity Rates}      |
| `output`  | `str` | The only allowable output value is "by_dataset" which will return a hash with the top-level keys being the datasets and their value being a list of mnemonic. |

#### Returns:
- `pd.DataFrame`: A DataFrame containing the dataset.
