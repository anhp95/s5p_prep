#%%
import harp
import numpy as np
import xarray as xr
import geopandas as gpd
import matplotlib.pyplot as plt

from mypath import *


def harp_convert(files, name, year):
    outfile = os.path.join(PREP_DIR, f"{year}", f"{name}.nc")

    if not os.path.exists(outfile):
        interp_lat = np.load(CAMS_REALS_LAT_FILE)
        interp_lon = np.load(CAMS_REALS_LON_FILE)
        res = 0.1

        nlat = round(((interp_lat[-1] - interp_lat[0]) / res) + 2)
        nlon = round(((interp_lon[-1] - interp_lon[0]) / res) + 2)

        lats = interp_lat[0] - 0.05
        lons = interp_lon[0] - 0.05

        operations = ";".join(
            [
                "tropospheric_NO2_column_number_density_validity>75",
                "derive(surface_wind_speed {time} [m/s])",
                "surface_wind_speed<5",
                "keep(latitude_bounds,longitude_bounds,datetime_start,datetime_length,tropospheric_NO2_column_number_density, surface_wind_speed)",
                "derive(datetime_start {time} [days since 2000-01-01])",
                "derive(datetime_stop {time}[days since 2000-01-01])",
                "exclude(datetime_length)",
                f"bin_spatial({nlat},{lats},{res},{nlon},{lons},{res})",
                "derive(tropospheric_NO2_column_number_density [Pmolec/cm2])",
                "derive(latitude {latitude})",
                "derive(longitude {longitude})",
                "count>0",
            ]
        )

        reduce_operations = ";".join(
            [
                "squash(time, (latitude, longitude, latitude_bounds, longitude_bounds))",
                "bin()",
            ]
        )
        try:
            mean_no2 = harp.import_product(
                files, operations, reduce_operations=reduce_operations
            )
            harp.export_product(mean_no2, outfile)
        except:
            print(f"no data {name}")


def path2date(path_):

    return path_.split("\\")[-1].split("____")[-1].split("T")[0]


def main(year):
    org_dir = r"C:\S5P-RPRO" if year == 2020 else ORG_DIR
    ORG_DATAS = glob.glob(os.path.join(org_dir, f"{year}", "*.nc"))

    list_dates = [path2date(f) for f in ORG_DATAS]
    list_dates = sorted(list(set(list_dates)))

    for date in list_dates:

        prefix = f"NO2____{date}"
        no2_files = [f for f in ORG_DATAS if prefix in f]
        harp_convert(no2_files, date, year)

        # ploting
    #     a = xr.open_dataset(os.path.join(PREP_DIR, f"{date}.nc"))
    # ukr_bound = gpd.read_file(UK_SHP_ADM0)
    # fig, ax = plt.subplots(1, 1)
    # a.tropospheric_NO2_column_number_density.plot(ax=ax)
    # ukr_bound.plot(ax=ax, facecolor="None", edgecolor="black")


# %%
