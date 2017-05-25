from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import (
    login_required, user_passes_test
)
from django.conf import settings
import requests
import json


        	
def index(request):
	return render_to_response("index.html",locals(),RequestContext(request))

def contact(request):
	return render_to_response("contact.html",locals(),RequestContext(request))