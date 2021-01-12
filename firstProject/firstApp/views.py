
# Create your views here.
from django.http import HttpResponse
def display_view(request):
	s="HELLO WORLD"
	return HttpResponse(s)
