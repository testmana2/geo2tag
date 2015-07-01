import geojson

def GeoJsonType(obj):
    jsonObj = geojson.loads(obj)
    if len(jsonObj.keys()) == 2 and 'coordinates' in jsonObj.keys() and isinstance(jsonObj.get('coordinates'), list):
        if jsonObj.get('type') == 'Point' or jsonObj.get('type') == 'Polygon' or jsonObj.get('type') == 'MultiPolygon':
            return jsonObj
        else:
            raise ValueError
    else:
        raise ValueError