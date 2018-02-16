from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
# from tours.forms import

# Create your views here.


def tours(request):
    return render(request, 'tours/tours_all.html')

def edooutpost(request):
    return render(request, 'tours/edooutpost.html')
