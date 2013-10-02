# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from results import views

urlpatterns = patterns('',
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.IncidentCreate.as_view(),
        name='incident_create'
    ),
)
