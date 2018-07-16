from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
     url(r'^store/', include('store.urls'), name='store'),
     url('', include('social.apps.django_app.urls', namespace='social')),
     url(r'^accounts/', include('registration.backends.default.urls')),
     url(r'^admin/', include(admin.site.urls)),
]
