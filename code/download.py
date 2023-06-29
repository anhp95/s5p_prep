#%%
import sentinelsat

api = sentinelsat.SentinelAPI(
    "s5pguest", "s5pguest", "https://s5phub.copernicus.eu/dhus"
)

result = api.query(
    footprint="Intersects(POLYGON((21.845147456690164 50.563133442400925,42.79792777871161 50.517763122619215,42.83362246409836 45.283294741644426,21.666674029756418 45.43378371246877,21.845147456690164 50.563133442400925,21.845147456690164 50.563133442400925)))",
    beginPosition="[2019-02-04T00:00:00.000Z TO 2019-06-30T23:59:59.999Z]",
    endPosition="[2019-02-04T00:00:00.000Z TO 2019-06-30T23:59:59.999Z]",
    platformname="Sentinel-5",
    producttype="L2__NO2___",
    processinglevel="L2",
    processingmode="Reprocessing",
)

products_df = api.to_dataframe(result)
#%%
api.download_all(products_df.index)
# %%
