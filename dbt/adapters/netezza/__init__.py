from dbt.adapters.netezza.connections import NetezzaConnectionManager
from dbt.adapters.netezza.connections import NetezzaCredentials
from dbt.adapters.netezza.impl import NetezzaAdapter
from dbt.adapters.netezza.relation import NetezzaRelation

from dbt.adapters.base import AdapterPlugin
from dbt.include import netezza


Plugin = AdapterPlugin(
    adapter=NetezzaAdapter,
    credentials=NetezzaCredentials,
    include_path=netezza.PACKAGE_PATH)
