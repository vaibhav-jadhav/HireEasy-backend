from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from rest_framework.response import Response
from . serializer import JObsSerializer, ApplicationsSerializer,InterviewSerializer
from .models import Jobs
from .models import Applications,Interview
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def getjobs(request):
    jobs=Jobs.objects.all()
    serialize=JObsSerializer(jobs,many=True)
    print("data = ",serialize.data)
    return JsonResponse(serialize.data,safe=False)
@csrf_exempt
def getapps(request):
    apps=Applications.objects.all()
    serialize=ApplicationsSerializer(apps,many=True)
    print("data = ",serialize.data)
    return JsonResponse(serialize.data,safe=False)
@csrf_exempt
def apply(request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        response_data = {"rada":"rada"}
        content = body[0]
        unique_id = get_random_string(length=25)
        application=Applications()
        application.jobid=content['id']
        application.email=content['email']
        application.full_name=content['full_name']
        application.address=content['address']
        application.applyid=unique_id
        application.status=""
        application.phone=content['phone']
        application.resume=content['resume']
        application.feedback=""
        application.save()       
        print(content)
        return JsonResponse(unique_id,safe=False)
    # feedupdate
@csrf_exempt
def feedupdate(request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        response_data = {"rada":"rada"}
        content = body[0]
        print(content)
        intrv=Applications.objects.get(applyid=content['applyid'])
        intrv.status=content['status']
        intrv.feedback=content['feedback']
        intrv.save()
        # intr=Interview()
        # intr.applyid=content['applyid']
       
        # application=Applications()
        # application.jobid=content['id']
        return JsonResponse("Updated",safe=False)
@csrf_exempt
def addinteview(request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        response_data = {"rada":"rada"}
        content = body[0]
        print(content)
        try:
            # go = Interview.objects.get(applyid=ids).latest('id')
            intr=Interview.objects.get(applyid=content['applyid'])
            #  intrv=Applications.objects.get(applyid=content['applyid'])
            # intr.applyid=content['applyid']
            intr.title=content['title']
            intr.link=content['link']
            intr.time=content['time']
            intr.note=content['note']
            intr.save()
            # go = Applications.objects.filter(applyid=ids).values('full_name')
        except Interview.DoesNotExist:
            intr=Interview()
            intr.applyid=content['applyid']
            intr.title=content['title']
            intr.link=content['link']
            intr.time=content['time']
            intr.note=content['note']
            intr.save()
        # application=Applications()
        # application.jobid=content['id']
        return JsonResponse("interview added",safe=False)
@csrf_exempt
def getinterview(request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        response_data = {"rada":"rada"}
        content = body[0]
        ids=content['applyid']
        print("IDDD",ids)
        try:
            go = Interview.objects.get(applyid=ids)
            # go = Applications.objects.filter(applyid=ids).values('full_name')
        except Interview.DoesNotExist:
            go = None
            return JsonResponse(None,safe=False)
        
        serialize= InterviewSerializer(go,many=False)
        print("----------------------------",serialize.data)
        return JsonResponse(serialize.data,safe=False)
    
    
    
@csrf_exempt 
def getstatus(request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        response_data = {"rada":"rada"}
        content = body[0]
        ids=content['id']
        try:
            go = Applications.objects.get(applyid=ids)
            # go = Applications.objects.filter(applyid=ids).values('full_name')
        except Applications.DoesNotExist:
            go = None
            return JsonResponse(None,safe=False)
        print("----------------------------",go)
        serialize= ApplicationsSerializer(go,many=False)
        return JsonResponse(serialize.data,safe=False)
    #      jobid = models.CharField(max_length=10)
    # full_name = models.CharField(max_length=60)
    # email = models.CharField(max_length=60)
    # address = models.CharField(max_length=60)
    # phone = models.CharField(max_length=60)
    # resume = models.CharField(max_length=60)
    # status= models.CharField(max_length=60)
    # applyid=models.CharField(max_length=50)
    # feedback=models.CharField(max_length=300)