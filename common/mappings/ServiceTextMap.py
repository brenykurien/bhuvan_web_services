from ..enums.Service import Service

service_text_map = {
    Service.LULC205KDataset.value: 'Load LULC205K Dataset',
    Service.GeoWebCacheWMS.value: 'Load GeoWebCache WMS',
    Service.BhuvanV1WMS.value: 'Load Bhuvan V1 WMS',
    Service.BhuvanV2WMS.value: 'Load Bhuvan V2 WMS',
    Service.FloodAnnualLayers.value: 'Flood Annual Layers',
    Service.FloodHazard.value: 'Flood Hazard',
    Service.BhuvanV1WMTS.value: 'Load Bhuvan V1 WMTS',
    Service.BhuvanV2WMTS.value: 'Load Bhuvan V2 WMTS'
}
