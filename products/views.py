import json

from django.http import JsonResponse
from django.views import View

from products.models import Owner, Dog

class OwnersView(View):
    def post(self, request):
        data     = json.loads(request.body)
        Owner.objects.create(
            name=data['owner'],
            email=data['email'],
            age=data['age'])
        
        return JsonResponse({'message':'created'}, status=201)
   
class DogsView(View):
    def post(self,request):
        data = json.loads(request.body)
        Dog.objects.create(
            name = data['dog'],
            age=data['age'],
            owner = Owner.objects.get(name=data['owner'])
        )
        
        return JsonResponse({'message':'created'}, status=201)