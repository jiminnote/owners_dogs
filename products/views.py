import json

from django.http import JsonResponse
from django.views import View

from products.models import Owner, Dog

class ProductsView(View):
    def post(self, request):
        data     = json.loads(request.body)
        owner     = Owner.objects.create(name=data['owner'])
        dog = Dog.objects.create(
            name = data['dog'],
            owner = owner
        )
        
        return JsonResponse({'messasge':'created'}, status=201)