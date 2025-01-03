from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackerStatus"),
    path("search/", views.search, name="Search"),
    path("productview/", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("productslist/", views.productlist, name="ProductsItems"),
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
