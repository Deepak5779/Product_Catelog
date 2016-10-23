from django.conf.urls import *
from django.contrib import admin
from catelog import views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^catelog/', views.index),
    # ... your url patterns
]
