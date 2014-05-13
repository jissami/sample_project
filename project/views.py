# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from project.models import Category
from project.models import Page

def index(request):
    context = RequestContext(request)
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render_to_response('project/index.html', context_dict, context)
