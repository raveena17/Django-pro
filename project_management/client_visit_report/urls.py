from django.conf.urls import url
from project_management.client_visit_report.views import *

app_name = 'client_visit_report'
urlpatterns = [

    url(r'^$', list),
    url(r'^create/$', create, name='create'),
    url(r'^report/(?P<id>\d+)/$', view_cvr_report),
    url(r'^(?P<id>\d+)/(?P<status>\w+)$', cvr_approval),
    url(r'^(?P<status>\w+)$', reports)

]
