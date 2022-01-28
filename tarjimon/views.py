from django.shortcuts import render
from .models import Lugat

def index(request):
	word = request.GET.get('q', '')
	if word and word != '':
		result = Lugat.objects.filter(english=word).all()
	else:
		result = None
		
	return render(request, 'index.html', {'q': word, 'result': result})