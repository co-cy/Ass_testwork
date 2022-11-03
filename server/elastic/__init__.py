from elasticsearch import AsyncElasticsearch
from serverConfig import ElasticConfig


async def connect_elasticsearch():
    get_elastic.elastic = AsyncElasticsearch(hosts=ElasticConfig.hosts, verify_certs=False)
    if not (await get_elastic().ping()):
        await get_elastic().close()
        raise "ERROR Connetction"


def get_elastic() -> AsyncElasticsearch:
    return get_elastic.elastic
