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
    def get(self,request):
        owners=Owner.objects.all()
        results=[]
        for owner in owners:
          doggy=owner.dog_set.all().values('name','age')
          results.append({
             'name':owner.name,
             'email':owner.email,
             'age':owner.age,
             'doggy': [dog for dog in doggy]
         })
        return JsonResponse({'RESULT':results}, status=201)
        
   
class DogsView(View):
    def post(self,request):
        data = json.loads(request.body)
        Dog.objects.create(
            name = data['dog'],
            age=data['age'],
            owner = Owner.objects.get(name=data['owner'])
        )
        
        return JsonResponse({'message':'created'}, status=201)
    
    def get(self,request):
        dogs=Dog.objects.all()
        results=[]
        for dog in dogs:
          results.append({
             'name':dog.name,
             'age':dog.age,
             'owner':dog.owner.name
         })
        return JsonResponse({'RESULT':results}, status=201)
    