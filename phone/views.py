# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from phone.models import Phone
from phone.constants import STATUS_TYPE
from phone.serializers import PhoneListSerializer, PhoneAddDataSerializer, PhoneUpdateDataSerializer
from django.shortcuts import render

# Create your views here.

class PhoneListView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            phone_list = Phone.objects.all()
            phone_list_serializer = PhoneListSerializer(phone_list, many=True)
            return Response(
                phone_list_serializer.data, status=status.HTTP_200_OK)
        except Exception, e:
            return Response(
                {"error": e.__str__()}, status=status.HTTP_400_BAD_REQUEST)

class PhoneInsertView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            serializer = PhoneAddDataSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.data

            phone_exist = Phone.objects.filter(phone=data['phone'], status__in=[STATUS_TYPE.NEW.value])
            if phone_exist:
                return Response(
                    {"error": "Phone Already in new state"}, status=status.HTTP_400_BAD_REQUEST)
            phone = Phone(
                **data
            )
            phone.save()

            phone_list_serializer = PhoneListSerializer(phone)
            return Response(
                phone_list_serializer.data, status=status.HTTP_201_CREATED)

        except Exception, e:
            return Response(
                {"error": e.__str__()}, status=status.HTTP_400_BAD_REQUEST)

class PhoneUpdateView(APIView):

    def post(self, request, phone_id, *args, **kwargs):
        try:
            serializer = PhoneUpdateDataSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.data

            phone = Phone.objects.get(id=phone_id)
            phone.status = data['status']
            phone.count += 1
            phone.save()

            phone_list_serializer = PhoneListSerializer(phone)
            return Response(
                phone_list_serializer.data, status=status.HTTP_201_CREATED)

        except Exception, e:
            return Response(
                {"error": e.__str__()}, status=status.HTTP_400_BAD_REQUEST)