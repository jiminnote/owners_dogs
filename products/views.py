import json

from django.http import JsonResponse
from django.views import View

from products.models import Owner, Dog

class ownersView(View):
    def post(self, request):
        data     = json.loads(request.body)
        Owner.objects.create(
            name=data['owner'],
            emali=data['email'],
            age=data['age'])
        
        return JsonResponse({'messasge':'created'}, status=201)
   
class dogsViw(View):
    def post(self,request):
        data = json.loads(request.body)
        Dog.objects.create(
            name = data['dog'],
            age=data['age'],
            owner = Owner.objects.get(name=data['owner'])
        )
        
        return JsonResponse({'messasge':'created'}, status=201)