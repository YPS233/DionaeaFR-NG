from django.urls import path

from Web.views.other import home
from Web.views.connection import connectionIndex, connectionDetail
from Web.views.download import downloadIndex
from Web.views.graph import services, servicesData
from Web.views.graph import ports, portsData
from Web.views.graph import urls, urlsData
from Web.views.graph import malware, malwareData
from Web.views.graph import ips, ipsData, ipsCountries
from Web.views.graph import connections, connectionsData, connCountries
from Web.views.graph import timeline
from Web.views.map import attackersMap, countriesMap


urlpatterns = [
    path(
        r'',
        home
    ),
    path(
        r'connections',
        connectionIndex,
        name='connection-index'
    ),
    path(
        r'connections/(<int:connection_id>\d+)',
        connectionDetail,
        name='connection-detail'
    ),
    path(
        r'downloads',
        downloadIndex,
        name='download-index'
    ),
    path(
        r'graphs/services',
        services,
        name='services'
    ),
    path(
        r'graphs/servicesdata/',
        servicesData,
        name='services-data'
    ),
    path(
        r'graphs/ports',
        ports,
        name='ports'
    ),
    path(
        r'graphs/portsdata/',
        portsData,
        name='ports-data'
    ),
    path(
        r'graphs/urls',
        urls,
        name='urls'
    ),
    path(
        r'graphs/urlsdata/',
        urlsData,
        name='urls-data'
    ),
    path(
        r'graphs/malware',
        malware,
        name='malware'
    ),
    path(
        r'graphs/malwaredata/',
        malwareData,
        name='malware-data'
    ),
    path(
        r'graphs/ips',
        ips,
        name='ips'
    ),
    path(
        r'graphs/ipsdata/',
        ipsData,
        name='ips-data'
    ),
    path(
        r'graphs/connections',
        connections,
        name='connections'
    ),
    path(
        r'graphs/connectionsdata/',
        connectionsData,
        name='connections-data'
    ),
    path(
        r'graphs/timeline/',
        timeline,
        name='timeline'
    ),
    path(
        r'graphs/conncountries/',
        connCountries,
        name='conn-countries'
    ),
    path(
        r'graphs/ipscountries/',
        ipsCountries,
        name='ips-countries'
    ),
    path(
        r'maps/attackers',
        attackersMap,
        name='attackers-map'
    ),
    path(
        r'maps/countries',
        countriesMap,
        name='countries-map'
    ),
]

# vim: set expandtab:ts=4
