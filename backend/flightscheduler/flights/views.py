from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from flights.models import Schedule
from flights.serializer import ScheduleSerializer, UserSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer


#APIS
#Fligths/
@csrf_exempt
def fligth_list(request):
    #GET ALL RECORDS
    if request.method == 'GET':
        schedules = Schedule.objects.all()
        schedules_serializer = ScheduleSerializer(schedules, many=True)
        return JsonResponse(schedules_serializer.data, safe=False )
    
    # ADD ONE RECORD
    if request.method == 'POST':
        schedule_data = JSONParser().parse(request)
        schedule_serializer = ScheduleSerializer(data=schedule_data)
        if schedule_serializer.is_valid():
            schedule_serializer.save()
            return JsonResponse(schedule_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(ScheduleSerializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE ALL RECORD
    if request.method == 'DELETE':
         Schedule.objects.all().delete()
         return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def fligth_detail(request,pk):
    try:
        schedule = Schedule.objects.get(pk=pk)
    except Schedule.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    #GET one RECORD
    if request.method== 'GET':
        print('Hola get fligth_detail')
        schedule_serializer=ScheduleSerializer(schedule)
        return JsonResponse(schedule_serializer.data)
    
    #Update one RECORD
    if request.method== 'PUT':
        schedule_data= JSONParser().parse(request)
        
        schedule_serializer= ScheduleSerializer(schedule, data=schedule_data)
        
        if schedule_serializer.is_valid():
            schedule_serializer.save()         
            return JsonResponse(schedule_serializer.data)
            
        return JsonResponse(schedule_serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    
    #DELETE ONE RECORD
    if request.method=='DELETE':
        schedule.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)



