
from django.urls import path
from .views import TodoView, TodoViewSet, get_todo, home, patch_todo , post_todo
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'todo-view-set',TodoViewSet, basename = 'todo')
urlpatterns = [
    path('',home, name="home"),
    path('post-todo/', post_todo, name="post_todo" ),
    path('get-todo/',get_todo, name='get_todo'),
    path('patch-todo/',patch_todo,name='patch_todo'),
    path('todo/',TodoView.as_view(),name='TodoView')
]

urlpatterns += router.urls
