from django.shortcuts import render
from newapp.serializer import UserSerializer
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from newapp.models import User_Table,Contacts
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserViewSet(APIView):
        def post(self, request, format=None):
            serializer = UserSerializer(data = request.data)

            if serializer.is_valid():
                if serializer.validated_data.get('password2') != serializer.validated_data.get('password'):
                    return Response({'message': 'both password field doesnot match'})
                if User.objects.filter(Q(username=str(serializer.validated_data.get('user_information')['Phone']))
                                       | Q(email = serializer.validated_data.get('email'))).exists():
                    return Response({'message': 'phonenumber or emaild id already exists'})


                user = User.objects.create(username = str(serializer.validated_data.get('user_information')['Phone']))
                user.set_password(serializer.validated_data.get('password'))
                user.save()
                if serializer.validated_data.get('email'):
                    user.email = serializer.validated_data.get('email')
                    user.save()
                User_Table.objects.create(user = user,Name = serializer.validated_data.get('user_information')['Name'],Phone =serializer.validated_data.get('user_information')['Phone'])

                return Response({'message':'usercreated'})
            else:
                return Response(serializer.errors)


class Spam(APIView):
    def post(self,request):
        print(request.data['Phone'])
        try:
            x = User_Table.objects.get(Phone = request.data['Phone'])
            x.is_spam = True
            x.save()
            print("xxxx")
        except ObjectDoesNotExist:
            try:
                x =Contacts.objects.get(Phone = request.data['Phone'])
                x.is_spam = True
                x.save()
            except ObjectDoesNotExist:
                Contacts.objects.create(Phone = request.data['Phone'],is_spam = True)
        return Response({'message':'Number Marked as spam'})

class Searchbyname(APIView):
    def get(self,request):
        print("====================================================")
        print(request.query_params.get('Name'))
        request_user_phone = User_Table.objects.get(user = request.user).Phone
        reg = User_Table.objects.filter(Name__icontains = request.query_params.get('Name'))
        cont = Contacts.objects.filter(Name__icontains = request.query_params.get('Name'))
        resp = []
        for i in reg:
            print("=========================================================")
            print(i.contacts.first().Phone)
            if i.contacts.filter(Phone = request_user_phone).exists():
                resp.append({'Name': i.Name, 'Phone': i.Phone, 'is_spam': i.is_spam,'email':request.user.email})
            else:
                resp.append({'Name':i.Name,'Phone':i.Phone,'is_spam':i.is_spam})
        for i in cont:
            resp.append({'Name': i.Name, 'Phone': i.Phone, 'is_spam': i.is_spam})
        return Response(resp)



# {
# "phonenumber":1234567891,
# "password":"Neha",
# "Name":"Neha"
#
# }
#
# # Create your views here.
# {
# "phonenumber":7065119155,
# "password":"Neha",
# "password2":"Neha",
# "Name":"Neha2",
# "email":"Neha@gmail.com"
#
# }