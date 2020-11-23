from bank_details.models import Banks,Branches
from bank_details.serializers import BranchesSerializer,BanksSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets,pagination
# from django.core.paginator import Paginator

class BankDetailsApi(viewsets.ViewSet):
    def retrieve(self, request):
        import pdb; pdb.set_trace()
        queryset = Branches.objects.filter(ifsc=request.data.get('strIfsc'))
        serializer = BranchesSerializer(queryset, many=True)
        return Response(serializer.data)

# class  BankListApi(viewsets.ViewSet):
    def list(self,request):
        import pdb; pdb.set_trace()
        pagination_class = pagination.PageNumberPagination
        queryset = Branches.objects.filter(bank__name=request.GET.get('strBank'),city=request.GET.get('strCity'))
        serializer = BranchesSerializer(queryset, many=True)
        # paginator = Paginator(serializer, 25)
        # page_number = 1
        # page_obj = paginator.get_page(page_number)
        return Response(serializer.data)