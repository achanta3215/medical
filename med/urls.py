from django.conf.urls import url
from . import views
urlpatterns = [
    
    #url(r'^hi/$', views.result_list, name='result_list'),
    url(r'^$', views.login, name='login'),
    url(r'^customer/$',views.customer,name='customer'),
    url(r'^customer/add/$',views.customer_add,name='customer_add'),
    url(r'^customer/add/database/$',views.add_database,name='customer_add_database'),
    url(r'^customer/cart$',views.addtocart,name='addtocart'),
    url(r'^customer/cart/existing$',views.existingusercheck,name='addtocart')
    #url(r'^new/$',forms.ResultCreateView, name='result_create'),
]