from django.shortcuts import render

# Create your views here.
from django.template import loader

from django.http import HttpResponse
from mysite.utility import fetch_data, fetch_record


def index(request):
	template = loader.get_template('index.html')
	context = {
		'results': False,
	}
	return HttpResponse(template.render(context, request))


def search(request):
	keyword = request.GET.get('keyword')
	template = loader.get_template('index.html')
	result = fetch_data(keyword)
	context = {
		'results': True,
		'list': result
	}
	return HttpResponse(template.render(context, request))


def show(request, app_id):
	result = fetch_record(app_id)
	template = loader.get_template('show.html')
	context = {
		'result': result
	}
	return HttpResponse(template.render(context, request))
