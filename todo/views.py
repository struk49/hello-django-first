from django.shortcuts import render
# Create your views heree


def get_todo_list(request):
    return render(request, 'todo/todo_list.html')