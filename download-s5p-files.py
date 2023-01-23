# download sp5 files
from sentinel5dl import search, download

# Search for Sentinel-5 products
result = search(
    polygon='POLYGON((36.19 36.73, 36.21 36.73, 36.21 36.74, 36.19 36.74, 36.19 36.73))',
    begin_ts='2023-01-01T00:00:00.000Z',
    end_ts='2023-01-12T23:59:59.999Z',
    product='L2__NO2___',
    processing_level='L2',
    processing_mode='Offline')

# Download found products to the local folder
#download(result.get('products'))

download(result.get('products'), output_dir='/Users/erdoganb/Desktop/erdo-dev/python/gis/s5p_read/no2 files')