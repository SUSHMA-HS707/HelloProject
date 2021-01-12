
# Create your views here.
from django.http import HttpResponse
def display_view(request):
	s="hai how are you"
	return HttpResponse(s)
