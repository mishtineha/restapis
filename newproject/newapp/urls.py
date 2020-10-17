from rest_framework import routers, serializers, viewsets
from newapp.views import UserViewSet,Spam,Searchbyname
from django.contrib import admin
from django.urls import path,include



# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet,basename='userviewset')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('users/',UserViewSet.as_view(),name="userviewset"),
    path('spam/', Spam.as_view(), name="spam"),
    path('searchbyname', Searchbyname.as_view(), name="searchbyname"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]