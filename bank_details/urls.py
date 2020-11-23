from django.conf.urls import url
from bank_details.views import BankDetailsApi,BankListApi,UserLoginViewSet

urlpatterns = [
    url(r'^bankdetails/$',BankDetailsApi.as_view({'post':'retrieve'}),name='bankdetails'),
    url(r'^banklist/$',BankListApi.as_view({'post':'retrieve'}),name='banklist'),
    url(r'^login/$',UserLoginViewSet.as_view({'post':'post'}),name='login'),
]