from scrape_base.base.code import CodeObject


IMPROPER_DATA_FORMAT = CodeObject(
    http_status=400,
    state_code='SCRAPE_BASE_IDF_400'
)

UNEXPECTED_ERROR = CodeObject(
    http_status=400,
    state_code='SCRAPE_BASE_UE_400'
)