from enum import IntEnum


class Service(IntEnum):
    LULC205KDataset = 0
    GeoWebCacheWMS = 1
    BhuvanV1WMS = 2
    BhuvanV2WMS = 3
    FloodAnnualLayers = 4
    FloodHazard = 5
    BhuvanV1WMTS = 6
    BhuvanV2WMTS = 7
