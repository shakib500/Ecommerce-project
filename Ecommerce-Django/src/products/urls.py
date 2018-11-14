from django.conf.urls import url

from django.conf.urls import  include
from . import views 
from rest_framework import routers 
router = routers.DefaultRouter ()
router.register('products',views.productsview)

from .views import (
        ProductListView, 
        ProductDetailSlugView, 
        )

urlpatterns = [

    url(r'^restapi/',include((router.urls), namespace='rest' )),
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
]

