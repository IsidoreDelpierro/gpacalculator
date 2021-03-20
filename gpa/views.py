from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return HttpResponse("Wow! This is an <strong>amazing</strong> app.<br>Now, I can calculate my GPA")
