from django.shortcuts import render
from django.template import RequestContext

from django_tables2 import RequestConfig
from Web.models.download import Download
from Web.tables.download import DownloadTable
from Web.filters.download import DownloadFilter
from Web.forms.download import DownloadFilterForm


length = len(Download.objects.all())


def downloadIndex(request):
    downloads = Download.objects.all()

    filterQueryset = DownloadFilter(
        request.GET,
        queryset=downloads
    )
    table = DownloadTable(
        filterQueryset.qs
    )
    filters = DownloadFilterForm()
    RequestConfig(
        request,
        paginate={
            "per_page": 12
        }
    ).configure(
        table
    )
    return render(
        request,
        'base.html',
        {
            'table': table,
            'filters': filters,
            'title': u'Downloads'
        },
    )

# vim: set expandtab:ts=4
