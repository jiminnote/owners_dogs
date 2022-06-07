from django.urls import path

from products.views import OwnersView, DogsView

urlpatterns = [
    path('', OwnersView.as_view()),
    
]