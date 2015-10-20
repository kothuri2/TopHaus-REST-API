from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views



urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/getUser/(?P<pk>[0-9]+)/$', views.UserDetailRetrieve.as_view()),
    url(r'^users/newUser/$', views.UserDetailCreate.as_view()),
    url(r'^users/deleteUser/(?P<pk>[0-9]+)/$', views.UserDetailDestroy.as_view()),
    url(r'^users/updateUser/(?P<pk>[0-9]+)/$', views.UserDetailUpdate.as_view()),

    url(r'^houses/$', views.HouseList.as_view()),
    url(r'^houses/getHouse/(?P<pk>[0-9]+)/$', views.HouseDetailRetrieve.as_view()),
    url(r'^houses/newHouse/$', views.HouseDetailCreate().as_view()),
    url(r'^houses/deleteHouse/(?P<pk>[0-9]+)/$', views.HouseDetailDestroy.as_view()),
    url(r'^houses/updateHouse/(?P<pk>[0-9]+)/$', views.HouseDetailUpdate.as_view()),

    url(r'^amenities/$', views.AmenityList.as_view()),
    url(r'^amenities/getAmenity/(?P<pk>[0-9]+)/$', views.AmenityDetailRetrieve.as_view()),
    url(r'^amenities/newAmenity/$', views.AmenityDetailCreate.as_view()),
    url(r'^amenities/deleteAmenity/(?P<pk>[0-9]+)/$', views.AmenityDetailDestroy.as_view()),
    url(r'^amenities/updateAmenity/(?P<pk>[0-9]+)/$', views.AmenityDetailUpdate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)