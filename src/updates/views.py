import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Update
# Create your views here.
from django.views.generic import View
from cfeapi.mixins import JsonResponseMixin
from django.core.serializers import serialize

def json_example_view(request):
    data = {
        "count": 1000,
        "content": "Some new content" 
    }
    return JsonResponse(data)


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
        "count": 1000,
        "content": "Some new content" 
        }
        return JsonResponse(data)

class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"   
        }
        return self.render_to_json_response(data)

class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = obj.serialize()
        return HttpResponse(data, content_type='application/json')

class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        json_data =Update.objects.all().serialize() 
        return HttpResponse(json_data, content_type='application/json')
         