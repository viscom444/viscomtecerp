

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.response import Response
from . models import Todo
from . serializers import TodoSerializer
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 


# Create your views here.

class ListTodoAPIView(APIView):
    def get(self,request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

class TodoDetailAPIView(APIView):
    def get(self,request,pk):
        todos = Todo.objects.get(id=pk)
        serializer = TodoSerializer(todos, many=False)
        return Response(serializer.data)

class CreateTodoAPIView(APIView):
     
     def post(self,request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UpdateTodoAPIView(APIView):
       
    def put(self, request, pk):
      item = Todo.objects.get(pk=pk) 
      tutorial_data = JSONParser().parse(request) 
      tutorial_serializer = TodoSerializer(item, data=tutorial_data) 
      if tutorial_serializer.is_valid():  
         tutorial_serializer.save() 
         return JsonResponse(tutorial_serializer.data) 
         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
     
       
        

class DeleteTodoAPIView(APIView):
    
    def delete(self, request, pk):
        
        item = Todo.objects.get(pk=pk) 
        item.delete()
        return Response({"Item Deleted"})
        