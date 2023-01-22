from rest_framework import serializers
from .models import TimingTodo, Todo
import re
from django.template.defaultfilters import slugify
class TodoSeriazlier(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    class Meta:
        model = Todo
        # fields = ['uid','todo_title','slug', 'todo_description','is_done' ]
        exclude = ['created_at','updated_at']

    
    def get_slug(self, obj):
        return slugify(obj.todo_title)


    #this the way we can validate todo_title
    def validate_todo_title(self, data):
        if data:
            todo_title = data
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if len(todo_title) < 3:
                raise serializers.ValidationError('todo_title must be greater than 3 characters')
            if not regex.search(todo_title) == None: 
                raise serializers.ValidationError('todo_title cannot contains special characters')
        return data
    #this is the another way
    # def validate(self, validated_data):
    #     if validated_data.get('todo_title'):
    #         todo_title = validated_data['todo_title']
    #         regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    #         if len(todo_title) < 3:
    #             raise serializers.ValidationError('todo_title must be greater than 3 characters')
    #         if not regex.search(todo_title) == None: 
    #             raise serializers.ValidationError('todo_title cannot contains special characters')

    #     return validated_data

class TimingTodoSerializer(serializers.ModelSerializer):
    todo = TodoSeriazlier()
    class Meta:
        model = TimingTodo
        exclude = ['created_at','updated_at']
        # depth = 1
