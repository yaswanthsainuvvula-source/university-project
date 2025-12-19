from django.urls import path
from .views import index,about,contact,branches,cse,it,mech,eee,ece,result_search,get_result

urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('branches/', branches, name='branches'),
    path('cse/', cse, name='cse'),
    path('it/', it, name='it'),
    path('mech/', mech, name='mech'),
    path('eee/', eee, name='eee'),
    path('ece/', ece, name='ece'),
    path('resultpage/',result_search,name='resultpage'),
    path('get_result/',get_result,name='get_result')

]
