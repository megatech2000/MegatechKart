from . import views
from django.urls import path


app_name='kartapp'

urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('SearchResult/', views.SearchResult, name='SearchResult'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),

]