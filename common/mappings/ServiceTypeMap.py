from ..enums.Service import Service
from ..enums.ServiceType import ServiceType


service_type_map = {
    Service.LULC205KDataset.value: ServiceType.WebMapService.value,
    Service.BhuvanV1WMS.value: ServiceType.WebMapService.value,
    Service.BhuvanV2WMS.value: ServiceType.WebMapService.value,
    Service.BhuvanV1WMTS.value: ServiceType.WebMapTileService.value,
    Service.BhuvanV2WMTS.value: ServiceType.WebMapTileService.value
}
