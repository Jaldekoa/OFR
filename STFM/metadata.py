from OFR.STFM.base import __read_metadata_mnemonics, __read_metadata_query, __read_metadata_search
from OFR.STFM.base import __read_series_timeseries, __read_calc_spread
from OFR.STFM.base import __read_series_full, __read_series_multifull, __read_series_dataset

mnemonic = ["MMF-MMF_AG_TOT-M", "MMF-MMF_BRA_TOT-M", "MMF-MMF_OA_TOT-M", "MMF-MMF_RP_AG_G30-M",
            "MMF-MMF_RP_AG_LE30-M", "MMF-MMF_RP_AG_OO-M", "MMF-MMF_RP_AG_TOT-M", "MMF-MMF_RP_G30-M",
            "MMF-MMF_RP_LE30-M", "MMF-MMF_RP_OA_G30-M", "MMF-MMF_RP_OA_LE30-M", "MMF-MMF_RP_OA_OO-M",
            "MMF-MMF_RP_OA_TOT-M", "MMF-MMF_RP_OO-M", "MMF-MMF_RP_TOT-M", "MMF-MMF_RP_T_G30-M",
            "MMF-MMF_RP_T_LE30-M", "MMF-MMF_RP_T_OO-M", "MMF-MMF_RP_T_TOT-M", "MMF-MMF_RP_wDFI-M",
            "MMF-MMF_RP_wFFI-M", "MMF-MMF_RP_wFICC-M", "MMF-MMF_RP_wFR-M", "MMF-MMF_RP_wOCP-M", "MMF-MMF_TOT-M",
            "MMF-MMF_T_TOT-M", "MMF-MY_MMF_RP_AG_G30-M", "MMF-MY_MMF_RP_AG_LE30-M", "MMF-MY_MMF_RP_AG_OO-M",
            "MMF-MY_MMF_RP_AG_TOT-M", "MMF-MY_MMF_RP_G30-M", "MMF-MY_MMF_RP_LE30-M", "MMF-MY_MMF_RP_OA_G30-M",
            "MMF-MY_MMF_RP_OA_LE30-M", "MMF-MY_MMF_RP_OA_OO-M", "MMF-MY_MMF_RP_OA_TOT-M", "MMF-MY_MMF_RP_OO-M",
            "MMF-MY_MMF_RP_TOT-M", "MMF-MY_MMF_RP_T_G30-M", "MMF-MY_MMF_RP_T_LE30-M", "MMF-MY_MMF_RP_T_OO-M",
            "MMF-MY_MMF_RP_T_TOT-M", "REPO-DVP_AR_G30-P", "REPO-DVP_AR_G30-F", "REPO-DVP_AR_LE30-P",
            "REPO-DVP_AR_LE30-F", "REPO-DVP_AR_OO-P", "REPO-DVP_AR_OO-F", "REPO-DVP_AR_TOT-P", "REPO-DVP_AR_TOT-F",
            "REPO-DVP_OV_G30-P", "REPO-DVP_OV_G30-F", "REPO-DVP_OV_LE30-P", "REPO-DVP_OV_LE30-F",
            "REPO-DVP_OV_OO-P", "REPO-DVP_OV_OO-F", "REPO-DVP_OV_TOT-P", "REPO-DVP_OV_TOT-F", "REPO-DVP_TV_G30-P",
            "REPO-DVP_TV_G30-F", "REPO-DVP_TV_LE30-P", "REPO-DVP_TV_LE30-F", "REPO-DVP_TV_OO-P",
            "REPO-DVP_TV_OO-F", "REPO-DVP_TV_TOT-P", "REPO-DVP_TV_TOT-F", "REPO-GCF_AR_AG-P", "REPO-GCF_AR_AG-F",
            "REPO-GCF_AR_G30-P", "REPO-GCF_AR_G30-F", "REPO-GCF_AR_LE30-P", "REPO-GCF_AR_LE30-F",
            "REPO-GCF_AR_OO-P", "REPO-GCF_AR_OO-F", "REPO-GCF_AR_T-P", "REPO-GCF_AR_T-F", "REPO-GCF_AR_TOT-P",
            "REPO-GCF_AR_TOT-F", "REPO-GCF_OV_AG-P", "REPO-GCF_OV_AG-F", "REPO-GCF_OV_G30-P", "REPO-GCF_OV_G30-F",
            "REPO-GCF_OV_LE30-P", "REPO-GCF_OV_LE30-F", "REPO-GCF_OV_OO-P", "REPO-GCF_OV_OO-F", "REPO-GCF_OV_T-P",
            "REPO-GCF_OV_T-F", "REPO-GCF_OV_TOT-P", "REPO-GCF_OV_TOT-F", "REPO-GCF_TV_AG-P", "REPO-GCF_TV_AG-F",
            "REPO-GCF_TV_G30-P", "REPO-GCF_TV_G30-F", "REPO-GCF_TV_LE30-P", "REPO-GCF_TV_LE30-F",
            "REPO-GCF_TV_OO-P", "REPO-GCF_TV_OO-F", "REPO-GCF_TV_T-P", "REPO-GCF_TV_T-F", "REPO-GCF_TV_TOT-P",
            "REPO-GCF_TV_TOT-F", "REPO-TRI_AR_AG-P", "REPO-TRI_AR_AG-F", "REPO-TRI_AR_CORD-P",
            "REPO-TRI_AR_CORD-F", "REPO-TRI_AR_G30-P", "REPO-TRI_AR_G30-F", "REPO-TRI_AR_LE30-P",
            "REPO-TRI_AR_LE30-F", "REPO-TRI_AR_O-P", "REPO-TRI_AR_O-F", "REPO-TRI_AR_OO-P", "REPO-TRI_AR_OO-F",
            "REPO-TRI_AR_T-P", "REPO-TRI_AR_T-F", "REPO-TRI_AR_TOT-P", "REPO-TRI_AR_TOT-F", "REPO-TRI_TV_AG-P",
            "REPO-TRI_TV_AG-F", "REPO-TRI_TV_CORD-P", "REPO-TRI_TV_CORD-F", "REPO-TRI_TV_G30-P",
            "REPO-TRI_TV_G30-F", "REPO-TRI_TV_LE30-P", "REPO-TRI_TV_LE30-F", "REPO-TRI_TV_O-P", "REPO-TRI_TV_O-F",
            "REPO-TRI_TV_OO-P", "REPO-TRI_TV_OO-F", "REPO-TRI_TV_T-P", "REPO-TRI_TV_T-F", "REPO-TRI_TV_TOT-P",
            "REPO-TRI_TV_TOT-F", "FNYR-BGCR-A", "FNYR-BGCR_1Pctl-A", "FNYR-BGCR_25Pctl-A", "FNYR-BGCR_75Pctl-A",
            "FNYR-BGCR_99Pctl-A", "FNYR-BGCR_UV-A", "FNYR-EFFR-A", "FNYR-EFFR_1Pctl-A", "FNYR-EFFR_25Pctl-A",
            "FNYR-EFFR_75Pctl-A", "FNYR-EFFR_99Pctl-A", "FNYR-EFFR_UV-A", "FNYR-OBFR-A", "FNYR-OBFR_1Pctl-A",
            "FNYR-OBFR_25Pctl-A", "FNYR-OBFR_75Pctl-A", "FNYR-OBFR_99Pctl-A", "FNYR-OBFR_UV-A", "FNYR-SOFR-A",
            "FNYR-SOFR_1Pctl-A", "FNYR-SOFR_25Pctl-A", "FNYR-SOFR_75Pctl-A", "FNYR-SOFR_99Pctl-A",
            "FNYR-SOFR_UV-A", "FNYR-TGCR-A", "FNYR-TGCR_1Pctl-A", "FNYR-TGCR_25Pctl-A", "FNYR-TGCR_75Pctl-A",
            "FNYR-TGCR_99Pctl-A", "FNYR-TGCR_UV-A", "NYPD-PD_AFtD_AG-A", "NYPD-PD_AFtD_AG_MBS-A",
            "NYPD-PD_AFtD_AG_eMBS-A", "NYPD-PD_AFtD_CORS-A", "NYPD-PD_AFtD_OMBS-A", "NYPD-PD_AFtD_T-A",
            "NYPD-PD_AFtD_TIPS-A", "NYPD-PD_AFtD_TOT-A", "NYPD-PD_AFtD_T_eTIPS-A", "NYPD-PD_AFtR_AG-A",
            "NYPD-PD_AFtR_AG_MBS-A", "NYPD-PD_AFtR_AG_eMBS-A", "NYPD-PD_AFtR_CORS-A", "NYPD-PD_AFtR_OMBS-A",
            "NYPD-PD_AFtR_T-A", "NYPD-PD_AFtR_TIPS-A", "NYPD-PD_AFtR_TOT-A", "NYPD-PD_AFtR_T_eTIPS-A",
            "NYPD-PD_RP_ABS_GE30-A", "NYPD-PD_RP_ABS_L30-A", "NYPD-PD_RP_ABS_OO-A", "NYPD-PD_RP_ABS_TOT-A",
            "NYPD-PD_RP_AG_GE30-A", "NYPD-PD_RP_AG_L30-A", "NYPD-PD_RP_AG_MBS_GE30-A", "NYPD-PD_RP_AG_MBS_L30-A",
            "NYPD-PD_RP_AG_MBS_OO-A", "NYPD-PD_RP_AG_MBS_TOT-A", "NYPD-PD_RP_AG_OO-A", "NYPD-PD_RP_AG_TOT-A",
            "NYPD-PD_RP_AG_eMBS_GE30-A", "NYPD-PD_RP_AG_eMBS_L30-A", "NYPD-PD_RP_AG_eMBS_OO-A",
            "NYPD-PD_RP_AG_eMBS_TOT-A", "NYPD-PD_RP_CORD_GE30-A", "NYPD-PD_RP_CORD_L30-A", "NYPD-PD_RP_CORD_OO-A",
            "NYPD-PD_RP_CORD_TOT-A", "NYPD-PD_RP_EQT_GE30-A", "NYPD-PD_RP_EQT_L30-A", "NYPD-PD_RP_EQT_OO-A",
            "NYPD-PD_RP_EQT_TOT-A", "NYPD-PD_RP_GE30-A", "NYPD-PD_RP_L30-A", "NYPD-PD_RP_OO-A",
            "NYPD-PD_RP_OS_GE30-A", "NYPD-PD_RP_OS_L30-A", "NYPD-PD_RP_OS_OO-A", "NYPD-PD_RP_OS_TOT-A",
            "NYPD-PD_RP_TIPS_GE30-A", "NYPD-PD_RP_TIPS_L30-A", "NYPD-PD_RP_TIPS_OO-A", "NYPD-PD_RP_TIPS_TOT-A",
            "NYPD-PD_RP_TOT-A", "NYPD-PD_RP_T_GE30-A", "NYPD-PD_RP_T_L30-A", "NYPD-PD_RP_T_OO-A",
            "NYPD-PD_RP_T_TOT-A", "NYPD-PD_RP_T_eTIPS_GE30-A", "NYPD-PD_RP_T_eTIPS_L30-A",
            "NYPD-PD_RP_T_eTIPS_OO-A", "NYPD-PD_RP_T_eTIPS_TOT-A", "NYPD-PD_RRP_ABS_GE30-A",
            "NYPD-PD_RRP_ABS_L30-A", "NYPD-PD_RRP_ABS_OO-A", "NYPD-PD_RRP_ABS_TOT-A", "NYPD-PD_RRP_AG_GE30-A",
            "NYPD-PD_RRP_AG_L30-A", "NYPD-PD_RRP_AG_MBS_GE30-A", "NYPD-PD_RRP_AG_MBS_L30-A",
            "NYPD-PD_RRP_AG_MBS_OO-A", "NYPD-PD_RRP_AG_MBS_TOT-A", "NYPD-PD_RRP_AG_OO-A", "NYPD-PD_RRP_AG_TOT-A",
            "NYPD-PD_RRP_AG_eMBS_GE30-A", "NYPD-PD_RRP_AG_eMBS_L30-A", "NYPD-PD_RRP_AG_eMBS_OO-A",
            "NYPD-PD_RRP_AG_eMBS_TOT-A", "NYPD-PD_RRP_CORD_GE30-A", "NYPD-PD_RRP_CORD_L30-A",
            "NYPD-PD_RRP_CORD_OO-A", "NYPD-PD_RRP_CORD_TOT-A", "NYPD-PD_RRP_EQT_GE30-A", "NYPD-PD_RRP_EQT_L30-A",
            "NYPD-PD_RRP_EQT_OO-A", "NYPD-PD_RRP_EQT_TOT-A", "NYPD-PD_RRP_GE30-A", "NYPD-PD_RRP_L30-A",
            "NYPD-PD_RRP_OO-A", "NYPD-PD_RRP_OS_GE30-A", "NYPD-PD_RRP_OS_L30-A", "NYPD-PD_RRP_OS_OO-A",
            "NYPD-PD_RRP_OS_TOT-A", "NYPD-PD_RRP_TIPS_GE30-A", "NYPD-PD_RRP_TIPS_L30-A", "NYPD-PD_RRP_TIPS_OO-A",
            "NYPD-PD_RRP_TIPS_TOT-A", "NYPD-PD_RRP_TOT-A", "NYPD-PD_RRP_T_GE30-A", "NYPD-PD_RRP_T_L30-A",
            "NYPD-PD_RRP_T_OO-A", "NYPD-PD_RRP_T_TOT-A", "NYPD-PD_RRP_T_eTIPS_GE30-A", "NYPD-PD_RRP_T_eTIPS_L30-A",
            "NYPD-PD_RRP_T_eTIPS_OO-A", "NYPD-PD_RRP_T_eTIPS_TOT-A", "NYPD-PD_SB_ABS_GE30-A",
            "NYPD-PD_SB_ABS_L30-A", "NYPD-PD_SB_ABS_OO-A", "NYPD-PD_SB_ABS_TOT-A", "NYPD-PD_SB_AG_GE30-A",
            "NYPD-PD_SB_AG_L30-A", "NYPD-PD_SB_AG_MBS_GE30-A", "NYPD-PD_SB_AG_MBS_L30-A", "NYPD-PD_SB_AG_MBS_OO-A",
            "NYPD-PD_SB_AG_MBS_TOT-A", "NYPD-PD_SB_AG_OO-A", "NYPD-PD_SB_AG_TOT-A", "NYPD-PD_SB_AG_eMBS_GE30-A",
            "NYPD-PD_SB_AG_eMBS_L30-A", "NYPD-PD_SB_AG_eMBS_OO-A", "NYPD-PD_SB_AG_eMBS_TOT-A",
            "NYPD-PD_SB_CORD_GE30-A", "NYPD-PD_SB_CORD_L30-A", "NYPD-PD_SB_CORD_OO-A", "NYPD-PD_SB_CORD_TOT-A",
            "NYPD-PD_SB_EQT_GE30-A", "NYPD-PD_SB_EQT_L30-A", "NYPD-PD_SB_EQT_OO-A", "NYPD-PD_SB_EQT_TOT-A",
            "NYPD-PD_SB_GE30-A", "NYPD-PD_SB_L30-A", "NYPD-PD_SB_OO-A", "NYPD-PD_SB_OS_GE30-A",
            "NYPD-PD_SB_OS_L30-A", "NYPD-PD_SB_OS_OO-A", "NYPD-PD_SB_OS_TOT-A", "NYPD-PD_SB_TIPS_GE30-A",
            "NYPD-PD_SB_TIPS_L30-A", "NYPD-PD_SB_TIPS_OO-A", "NYPD-PD_SB_TIPS_TOT-A", "NYPD-PD_SB_TOT-A",
            "NYPD-PD_SB_T_GE30-A", "NYPD-PD_SB_T_L30-A", "NYPD-PD_SB_T_OO-A", "NYPD-PD_SB_T_TOT-A",
            "NYPD-PD_SB_T_eTIPS_GE30-A", "NYPD-PD_SB_T_eTIPS_L30-A", "NYPD-PD_SB_T_eTIPS_OO-A",
            "NYPD-PD_SB_T_eTIPS_TOT-A", "NYPD-PD_SL_ABS_GE30-A", "NYPD-PD_SL_ABS_L30-A", "NYPD-PD_SL_ABS_OO-A",
            "NYPD-PD_SL_ABS_TOT-A", "NYPD-PD_SL_AG_GE30-A", "NYPD-PD_SL_AG_L30-A", "NYPD-PD_SL_AG_MBS_GE30-A",
            "NYPD-PD_SL_AG_MBS_L30-A", "NYPD-PD_SL_AG_MBS_OO-A", "NYPD-PD_SL_AG_MBS_TOT-A", "NYPD-PD_SL_AG_OO-A",
            "NYPD-PD_SL_AG_TOT-A", "NYPD-PD_SL_AG_eMBS_GE30-A", "NYPD-PD_SL_AG_eMBS_L30-A",
            "NYPD-PD_SL_AG_eMBS_OO-A", "NYPD-PD_SL_AG_eMBS_TOT-A", "NYPD-PD_SL_CORD_GE30-A",
            "NYPD-PD_SL_CORD_L30-A", "NYPD-PD_SL_CORD_OO-A", "NYPD-PD_SL_CORD_TOT-A", "NYPD-PD_SL_EQT_GE30-A",
            "NYPD-PD_SL_EQT_L30-A", "NYPD-PD_SL_EQT_OO-A", "NYPD-PD_SL_EQT_TOT-A", "NYPD-PD_SL_GE30-A",
            "NYPD-PD_SL_L30-A", "NYPD-PD_SL_OO-A", "NYPD-PD_SL_OS_GE30-A", "NYPD-PD_SL_OS_L30-A",
            "NYPD-PD_SL_OS_OO-A", "NYPD-PD_SL_OS_TOT-A", "NYPD-PD_SL_TIPS_GE30-A", "NYPD-PD_SL_TIPS_L30-A",
            "NYPD-PD_SL_TIPS_OO-A", "NYPD-PD_SL_TIPS_TOT-A", "NYPD-PD_SL_TOT-A", "NYPD-PD_SL_T_GE30-A",
            "NYPD-PD_SL_T_L30-A", "NYPD-PD_SL_T_OO-A", "NYPD-PD_SL_T_TOT-A", "NYPD-PD_SL_T_eTIPS_GE30-A",
            "NYPD-PD_SL_T_eTIPS_L30-A", "NYPD-PD_SL_T_eTIPS_OO-A", "NYPD-PD_SL_T_eTIPS_TOT-A", "TYLD-TCMR-10Yr-A",
            "TYLD-TCMR-1Mo-A", "TYLD-TCMR-1Yr-A", "TYLD-TCMR-20Yr-A", "TYLD-TCMR-2Mo-A", "TYLD-TCMR-2Yr-A",
            "TYLD-TCMR-30Yr-A", "TYLD-TCMR-3Mo-A", "TYLD-TCMR-3Yr-A", "TYLD-TCMR-5Yr-A", "TYLD-TCMR-6Mo-A",
            "TYLD-TCMR-7Yr-A"]

params_by_endpoint = {
    "metadata/mnemonics": ["dataset", "output"],
    "metadata/query": ["mnemonic", "fields"],
    "metadata/search": ["query"],
    "series/timeseries": ["mnemonic", "label", "start_date", "end_date", "periodicity", "how", "remove_nulls",
                          "time_format"],
    "calc/spread": ["x", "y", "start_date", "end_date", "periodicity", "how", "remove_nulls", "time_format"],
    "series/full": ["mnemonic", "start_date", "end_date", "periodicity", "how", "remove_nulls", "time_format"],
    "series/multifull": ["mnemonics", "start_date", "end_date", "periodicity", "how", "remove_nulls", "time_format"],
    "series/dataset": ["dataset", "vintage", "start_date", "end_date", "periodicity", "how", "remove_nulls",
                       "time_format"]
}

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

all_params = {
    "x": mnemonic,
    "y": mnemonic,
    "mnemonic": mnemonic,
    "output": ["by_dataset"],
    "vintage": ["p", "f", "a"],
    "remove_nulls": [True, False],
    "time_format": ["date", "ms"],
    "label": ["aggregation", "disclosure_edits"],
    "how": ["first", "last", "mean", "median", "sum"],
    "dataset": ["mmf", "repo", "fnyr", "nypd", "tyld"],
    "periodicity": ["A", "AS", "D", "M", "MS", "W", "B", "BM", "BMS", "Q", "BQ", "QS", "BQS", "BA", "BAS"],
    "fields": ["description", "description/vintage_approach", "description/vintage", "description/notes",
               "description/description", "description/subsetting", "description/subtype", "description/name", "rights",
               "rights/description", "schedule", "schedule/observation_period", "schedule/seasonal_adjustment",
               "schedule/start_date", "schedule/last_update", "parents", "release", "release/long_name", "release/href",
               "release/frecuency", "release/short_name", "unit", "unit/type", "unit/magnitude", "unit/display_magnitude",
               "unit/name", "unit/precision"]
}