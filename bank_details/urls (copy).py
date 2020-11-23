from django.conf.urls import url
from bank_details.views import BankDetailsApi #,BankListApi

urlpatterns = [
    url(r'^bankdetails/$',BankDetailsApi.as_view({'post':'retrieve','get':'list'}),name='bankdetails'),
    # url(r'^banklist/$',BankListApi.as_view({'post':'retrieve'}),name='banklist'),
]