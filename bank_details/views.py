from bank_details.models import Banks,Branches
from bank_details.serializers import BranchesSerializer,BanksSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import requests
import json
from rest_framework.permissions import IsAuthenticated



class BankDetailsApi(viewsets.ViewSet):
    """
    Api for returning bank deatails according given ifsc code
    parameter : IFSC number
    {"strIfsc":"ABHY0065001"}
    return bank details or empty list
    """
    permission_classes = [IsAuthenticated]
    def retrieve(self, request):
        queryset = Branches.objects.filter(ifsc=request.data.get('strIfsc'))
        serializer = BranchesSerializer(queryset, many=True)
        return Response(serializer.data)

class  BankListApi(viewsets.ViewSet):
    """
    Api for returning bank deatails according given bank name and city after paginating
    parameter : bank name,city name, limit and offset
    {"strBank":"ABHYUDAYA COOPERATIVE BANK LIMITED","strCity":"MUMBAI","intLimit":10,"intOffset":"2"}
    return : bank details or empty list
    """
    permission_classes = [IsAuthenticated]
    def retrieve(self,request):
        queryset = Branches.objects.filter(bank__name=request.data.get('strBank'),city=request.data.get('strCity'))
        serializer = BranchesSerializer(queryset, many=True)
        if not request.data.get('intLimit') or not request.data.get('intOffset') :
            return Response({'status':'failed','message':'Limit/Offset should be greater than or equal to 1'})
        paginator = Paginator(list(serializer.data), int(request.data.get('intLimit')))
        int_page_number = int(request.data.get('intOffset'))
        if int_page_number > paginator.num_pages:
            data = []
        else:
            obj_page = paginator.page(int_page_number)
            data = obj_page.object_list
        return Response(data)


class UserLoginViewSet(viewsets.ViewSet):


    """
    Used User login
    """
    def post(self, request):
        try:   
            import pdb; pdb.set_trace()
            vchr_username= request.data['userName']
            vchr_password=request.data['userPassword']
            user = authenticate(request, username=vchr_username, password=vchr_password)
            if user:
                login(request, user)
                # token_json = requests.post('http://'+request.get_host()+'/api-token-auth/',{'username':vchr_username,'password':vchr_password})
                token_json = requests.post('http://'+request.get_host()+'/api/auth/jwt/',{'username':vchr_username,'password':vchr_password})
                token = json.loads(token_json._content.decode("utf-8"))['token']
                str_name=vchr_username.title() if user.is_staff else (user.first_name +' '+ user.last_name).title()
                userdetails={'Name':str_name}
            
                return Response({'status':'success','token':token,'userdetails':userdetails})
            
            return Response({'status':'failed'})

        except Exception as e:
            return Response({'status':0,'message':str(e)})