from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from home.models import TimingTodo, Todo
from.serializer import TimingTodoSerializer, TodoSeriazlier
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import  TokenAuthentication
from django.core.paginator import Paginator
from .helper import paginate
# Create your views here.

#This is the fist method to create api in this we can implement all api methods in one function
@api_view(['GET','POST','PATCH'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status':200,
            'message': 'Yes! Django rest framework is work!!!',
            'method': 'you called GET method'
        })
    elif request.method == 'POST':
        return Response({
            'status': 200,
            'message':'Yes! Django rest framework is work!!!',
            'method':'you called POST method'
             
        })
    elif request.method == 'PATCH':
        return Response({
            'status':200,
            'message':'Yes! Django rest framework is work!!!',
            'method':'you called PATCH method'
        })
    else:
         return Response({
            'status':200,
            'message':'Yes! Django rest framework is work!!!',
            'method':'you this method is not available'
        })



# This is the second method to create an api in this we are create different function for api methods
@api_view(['GET'])
def get_todo(request):
    todo_obj = Todo.objects.all()
    serializer = TodoSeriazlier(todo_obj, many =True)

    return Response({
        'status': True,
        'message':"Todo Fetched",
        'data': serializer.data
    })

@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSeriazlier(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':True,
                'message':'Success Todo Created',
                'data':serializer.data
            })
        # else:
        return Response({
            'status': False,
            'message':'UnSuccess to create',
            'data': serializer.errors
        })

    except Exception as e:
        print(e)
    return Response({
        'status':False,
        'message':'unsuccess'
    })

@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
                'status':False,
                'message':'uid is required',
                'data':{}
            })
        obj= Todo.objects.get(uid = data.get('uid'))
        serializer = TodoSeriazlier(obj, data= data,partial =True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':True,
                'message':'Success data',
                'data':serializer.data
            })
        else:
            return Response({
                'status':False,
                'message':'Invalid data',
                'data':serializer.errors
            })
    except Exception as e:
        return Response({
                'status':True,
                'message':'invalid uid',
                'data':{}
            })

# This is the third method for create all apis without need to create another routers

class TodoView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # print(request.user)
        todo_obj = Todo.objects.filter(user = request.user)
        page = request.GET.get('page',1)
        page_obj = Paginator(todo_obj, 2)
        # print(page_obj)
        results = paginate(todo_obj, page_obj,page)
        print(results)
        serializer = TodoSeriazlier(results['results'], many =True)

        return Response({
            'status': True,
            'message':"Todo Fetched",
            'data': {'data':serializer.data,'pagination': results['pagination']}
        })

    def post(self, request):
        try:
            data = request.data
            data['user'] = request.user.id
            serializer = TodoSeriazlier(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':True,
                    'message':'Success Todo Created',
                    'data':serializer.data
                })
            # else:
            return Response({
                'status': False,
                'message':'UnSuccess to create',
                'data': serializer.errors
            })

        except Exception as e:
            print(e)
        return Response({
            'status':False,
            'message':'unsuccess'
        })

    def patch(self, request):
        try:
            data = request.data
            if not data.get('uid'):
                return Response({
                    'status':False,
                    'message':'uid is required',
                    'data':{}
                })
            obj= Todo.objects.get(uid = data.get('uid'))
            serializer = TodoSeriazlier(obj, data= data,partial =True)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':True,
                    'message':'Success data',
                    'data':serializer.data
                })
            else:
                return Response({
                    'status':False,
                    'message':'Invalid data',
                    'data':serializer.errors
                })
        except Exception as e:
            return Response({
                    'status':True,
                    'message':'invalid uid',
                    'data':{}
                })


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSeriazlier

    @action(detail=False, methods=['get'])
    def get_timing_todo(self, request):
        objs = TimingTodo.objects.all()
        serializer = TimingTodoSerializer(objs, many=True)
        return Response({
            "status": True,
            "message":"Timing todo fetched",
            "data": serializer.data
        })


    @action(detail=False, methods=['post'])
    def add_date_to_todo(self,request):
        try:
            data = request.data
            serializer = TimingTodoSerializer(data= data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':True,
                    'message':'Success Todo Created',
                    'data':serializer.data
                })
            else:
                return Response({
                    'status': False,
                    'message':'UnSuccess to create',
                    'data': serializer.errors
                })
        except Exception as e:
            return Response({
                    'status': False,
                    'message':'invalid to create',
                    'data': {}
                })
