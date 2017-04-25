from django.conf.urls import url
from phone import views

urlpatterns = [
    url(
            regex=r'^/phone/list/$',
            view=views.PhoneListView.as_view(),
            name='phone-list'
        ),
    url(
            regex=r'^/phone/(?P<phone_id>[0-9]+)/$',
            view=views.PhoneUpdateView.as_view(),
            name='phone-update'
        ),
    url(
            regex=r'^/phone/$',
            view=views.PhoneInsertView.as_view(),
            name='phone-insert'
        ),
]