from django.urls import path,include
from api import views


urlpatterns = [

    path('', views.apiOverview, name= 'apioverview'),
    path('product-list/', views.showAll, name= 'productlist'),
    path('product-create/', views.productCreate, name= 'productcreate'),
    path('product-detail/<int:pk>', views.viewProduct, name= 'productview'),
    path('product-update/<int:pk>', views.productUpdate, name= 'productupdate'),
    path('product-delete/<int:pk>', views.productDelete, name= 'productdelete'),

]