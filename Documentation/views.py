from django.shortcuts import render

def documentation(request):
	return render(request,'index.html')
