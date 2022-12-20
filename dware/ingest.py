#from PIL import Image, ExifTags
from pathlib import Path
import exifread

pict_fname = Path('~/sandbox/dware/kayaks.JPEG').expanduser()

# For documentation on GPS* properties:
# https://exiftool.org/TagNames/GPS.html

def get_metadata(pict_fname):
    """Get photo metadata and thumbnail.

    Meta to include:
    google_map_url
    lat, lon, alt, bearing
    ... !!!
    """
    meta = dict()

    #!im = Image.open(pict_fname)
    #!exif = im.getexif()

    tags = exifread.process_file(open(pict_fname, 'rb'), details=False)

    # See: https://developers.google.com/maps/documentation/urls/guide
    # OLD http://www.google.com/maps/place/lat,lng
    # NEW https://www.google.com/maps/search/?api=1&query=latitude,longitude
    # NEW https://www.google.com/maps/@{lat},{long},{zoom}z
    # https://www.google.com/maps/@?api=1&map_action=map&{lat},{long},{zoom}z

    lon = tags['GPS GPSLongitude'].values
    lg = lon[0]+lon[1]/60.0+float(lon[2])/3600
    if 'W' == tags['GPS GPSLongitudeRef'].values:
        lg *= -1
    lat = tags['GPS GPSLatitude'].values
    lt = lat[0]+lat[1]/60.0+float(lat[2])/3600
    if 'S' == tags['GPS GPSLatitudeRef'].values:
        lt *= -1
    meta['mapurl'] = f'https://www.google.com/maps/@?api=1&map_action=map&center={lt},{lg}'
    meta.update(tags)

    return meta
