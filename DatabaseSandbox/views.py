from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import json
import os
import random

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import datetime

from rest_framework.permissions import IsAuthenticated, AllowAny

from DatabaseSandbox.models import VisitorLogSB, LazarusCommanderAccountSB, \
    LazarusModProjectSB, BasicUploadTrackerSB, TotalAnnihilationUploadedFile
from django.template import loader
import subprocess
from chat.models import JawnUser



# Create your views here.
class BasicUploadExample(APIView):
    # serializer_class = SuperBasicModelSerializer
    permission_classes = (AllowAny,)  # IsAuthenticated

    def get(self, request, format=None):
        allmodels = Car.objects.all()
        print(allmodels)
        return Response(allmodels)

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES['file']
        # f = open('/usr/src/app/static/uploaded_file', 'w')
        # print('preparing to write file to /usr/src/app/static/uploaded_file')
        # myfile = File(f)
        # myfile.write(ContentFile(file_obj.read()))


        path = default_storage.save(request.user.username.strip() + '/' + str(file_obj), ContentFile(file_obj.read()))

        tmp_file = os.path.join(settings.MEDIA_ROOT, path)

        response = {'result': 'everything is finished ! ! ! ' + str(tmp_file)}

        file_name_regular = str(path).replace(request.user.username.strip()+'/','')
        but_DB = BasicUploadTrackerSB(file_name=file_name_regular,
                                      download_url='/media/'+path,
                                      system_path=str(tmp_file),
                                      author=request.user.username
                                      )
        but_DB.save()
        print('PROCESS COMPLETED!!!')
        return Response(response)

class KubaNetAnalytics(APIView):
    def get(self, request, format=None):
        permission_classes = (AllowAny,)
        visitors = VisitorLogSB.objects.all()
        list_data = []
        total_visitors = 0
        total_unique_visitors = 0
        unique = {}
        # res = {}
        for item in visitors:
            res = {}
            res['remote_addr'] = item.remote_addr
            res['date_visited'] = item.date_created
            list_data.append(res)
            total_visitors += 1
            unique[str(item.remote_addr)] = item.http_usr
        final_answer = {}
        final_answer['total_visitors'] = total_visitors
        final_answer['total_unique_visitors'] = len(unique)
        final_answer['visior_data'] = list_data
        return Response(final_answer)




class UserAgentTracker(APIView):
    def get(self, request, format=None):
        _1 = str(request.META['REMOTE_ADDR'])
        _2 = str(request.META['HTTP_USER_AGENT'])
        _3 = str(request.META['HTTP_ACCEPT_LANGUAGE'])
        _date = datetime.date
        newRecord = VisitorLogSB(remote_addr=_1, http_usr=_2, http_accept=_3)
        newRecord.save()

        html = '<div>' + \
               '<h1> User Visitor Tracking </h1>' + \
               '<h3> REMOTE_ADDR </h3>' + \
               '<p>' + str(_1) + '</p>' + \
               '<h3> HTTP_USER_AGENT </h3>' + \
               '<p>' + str(_2) + '</p>' + \
               '<h3> HTTP_ACCEPT_LANGUAGE </h3>' + \
               '<p>' + str(_3) + '</p>' + \
               '<h4> date </h4>' + \
               '<p>' + str(_date.today()) + '</p>' + \
               '<h5> username </h5>' + \
               '<p>' + str(request.user) + '</p>' + \
               '</div>'
        return HttpResponse(html)
