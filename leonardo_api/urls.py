

from django.conf.urls import url, include

from .authtoken.views import obtain_auth_token

from .router import router

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/auth/', obtain_auth_token),
    url(r'^', include('leonardo_api.graphql.urls')),
]
