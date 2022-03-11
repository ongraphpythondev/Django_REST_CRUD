from django.urls import path 
from CRUD.views import Books , Book_class

urlpatterns = [
    path('', Books.as_view()  , name = 'login'),
    path('<int:pk>', Book_class.as_view()  , name = 'login'),
]