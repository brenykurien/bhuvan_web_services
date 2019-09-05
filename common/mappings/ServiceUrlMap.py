from ..enums.Service import Service

service_url_map = {
    Service.LULC205KDataset.value: 'https://bhuvan-ras2.nrsc.gov.in/cgi-bin/LULC250K.exe',
    Service.GeoWebCacheWMS.value: 'https://bhuvan-vec1.nrsc.gov.in/bhuvan/gwc/service/wms/',
    Service.BhuvanV1WMS.value: 'https://bhuvan-vec1.nrsc.gov.in/bhuvan/nuis/wms',
    Service.BhuvanV1WMTS.value: 'https://bhuvan-vec1.nrsc.gov.in/bhuvan/nuis/gwc/service/wmts',
    Service.BhuvanV2WMS.value: 'https://bhuvan-vec2.nrsc.gov.in/bhuvan/wms',
    Service.BhuvanV2WMTS.value: 'https://bhuvan-vec2.nrsc.gov.in/bhuvan/gwc/service/wmts'
}
