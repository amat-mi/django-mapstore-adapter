# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright 2018, GeoSolutions Sas.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
#
#########################################################################

import os

from django.conf.urls import url, include
from django.utils.module_loading import import_string


_urlpatterns = [
    url(r'^mapstore/', include('mapstore2_adapter.api.urls')),
]

try:
    urlconf = os.getenv('MAPSTORE2_ADAPTER_ROOT_URLCONF','geonode.urls')
    urlpatterns = import_string("%s.urlpatterns" % urlconf)
    urlpatterns += _urlpatterns
except BaseException:
    urlpatterns = _urlpatterns
