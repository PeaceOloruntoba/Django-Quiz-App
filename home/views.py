from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import random

# Create your views here.

# {
#     'status':True
#     'data':[
#         {},
#     ]
# }
def home(request):
    return HttpResponse("Hello World!")

def get_quiz(request):
    try:
        question_objs = list(Question.objects.all())
        data = []
        random.shuffle((question_objs))
        print(question_objs)
        for question_obj in question_objs:
            data.append({
                "category" : question_obj.category.category_name,
                "question" : question_obj.question,
                "marks" : question_obj.marks,
                "answers" : question_obj.get_answer()
            })
        payload = {'status': True, 'data':data}
        return JsonResponse(payload)
    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong!!")