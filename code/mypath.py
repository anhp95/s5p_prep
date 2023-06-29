import os
import glob

BASE_DIR = "../data"
CAMS_REALS_LAT_FILE = os.path.join(BASE_DIR, "interp_latlon", "cams_reals_lat.npy")
CAMS_REALS_LON_FILE = os.path.join(BASE_DIR, "interp_latlon", "cams_reals_lon.npy")

ORG_DIR = os.path.join(BASE_DIR, "org_data")

PREP_DIR = os.path.join(BASE_DIR, "prep_data")

BOUND_DIR = os.path.join(BASE_DIR, "ukr_bound")
UK_SHP_ADM0 = os.path.join(BOUND_DIR, "ukr_admbnda_adm0_sspe_20221005.shp")
