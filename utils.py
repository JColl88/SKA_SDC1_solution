# Catalogue columns for SDC1 submissions
CAT_COLUMNS = [
    "id",
    "ra_core",
    "dec_core",
    "ra_cent",
    "dec_cent",
    "flux",
    "core_frac",
    "b_maj",
    "b_min",
    "pa",
    "size",
    "class",
]

# Columns output by PyBDSF
SRL_COLUMNS = [
    "Source_id",
    "Isl_id",
    "RA",
    "E_RA",
    "DEC",
    "E_DEC",
    "Total_flux",
    "E_Total_flux",
    "Peak_flux",
    "E_Peak_flux",
    "RA_max",
    "E_RA_max",
    "DEC_max",
    "E_DEC_max",
    "Maj",
    "E_Maj",
    "Min",
    "E_Min",
    "PA",
    "E_PA",
    "Maj_img_plane",
    "E_Maj_img_plane",
    "Min_img_plane",
    "E_Min_img_plane",
    "PA_img_plane",
    "E_PA_img_plane",
    "DC_Maj",
    "E_DC_Maj",
    "DC_Min",
    "E_DC_Min",
    "DC_PA",
    "E_DC_PA",
    "DC_Maj_img_plane",
    "E_DC_Maj_img_plane",
    "DC_Min_img_plane",
    "E_DC_Min_img_plane",
    "DC_PA_img_plane",
    "E_DC_PA_img_plane",
    "Isl_Total_flux",
    "E_Isl_Total_flux",
    "Isl_rms",
    "Isl_mean",
    "Resid_Isl_rms",
    "Resid_Isl_mean",
    "S_Code",
]

# Columns output by PyBDSF
GAUL_COLUMNS = [
    "Gaus_id",
    "Isl_id",
    "Source_id",
    "Wave_id",
    "RA",
    "E_RA",
    "DEC",
    "E_DEC",
    "Total_flux",
    "E_Total_flux",
    "Peak_flux",
    "E_Peak_flux",
    "Xposn",
    "E_Xposn",
    "Yposn",
    "E_Yposn",
    "Maj",
    "E_Maj",
    "Min",
    "E_Min",
    "PA",
    "E_PA",
    "Maj_img_plane",
    "E_Maj_img_plane",
    "Min_img_plane",
    "E_Min_img_plane",
    "PA_img_plane",
    "E_PA_img_plane",
    "DC_Maj",
    "E_DC_Maj",
    "DC_Min",
    "E_DC_Min",
    "DC_PA",
    "E_DC_PA",
    "DC_Maj_img_plane",
    "E_DC_Maj_img_plane",
    "DC_Min_img_plane",
    "E_DC_Min_img_plane",
    "DC_PA_img_plane",
    "E_DC_PA_img_plane",
    "Isl_Total_flux",
    "E_Isl_Total_flux",
    "Isl_rms",
    "Isl_mean",
    "Resid_Isl_rms",
    "Resid_Isl_mean",
    "S_Code",
]

# Columns that do not have a bearing on the training of size_id classifier
SRL_COLS_TO_DROP = [
    "Isl_id",
    "RA",
    "E_RA",
    "DEC",
    "E_DEC",
    "RA_max",
    "E_RA_max",
    "DEC_max",
    "E_DEC_max",
    "PA",
    "E_PA",
]

# Categorical columns in source list
SRL_CAT_COLS = ["S_Code"]

# Numerical columns in source list
SRL_NUM_COLS = [
    "Total_flux",
    "E_Total_flux",
    "Peak_flux",
    "E_Peak_flux",
    "Maj",
    "E_Maj",
    "Min",
    "E_Min",
    "Maj_img_plane",
    "E_Maj_img_plane",
    "Min_img_plane",
    "E_Min_img_plane",
    "PA_img_plane",
    "E_PA_img_plane",
    "DC_Maj",
    "E_DC_Maj",
    "DC_Min",
    "E_DC_Min",
    "DC_PA",
    "E_DC_PA",
    "DC_Maj_img_plane",
    "E_DC_Maj_img_plane",
    "DC_Min_img_plane",
    "E_DC_Min_img_plane",
    "DC_PA_img_plane",
    "E_DC_PA_img_plane",
    "Isl_Total_flux",
    "E_Isl_Total_flux",
    "Isl_rms",
    "Isl_mean",
    "Resid_Isl_rms",
    "Resid_Isl_mean",
    "n_gaussians",
]
