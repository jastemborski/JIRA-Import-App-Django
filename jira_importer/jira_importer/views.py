"""from django.template.loader import get_template
from django.template import Context"""
from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime

"""
Each view function takes at least one parameter, called request
by convention his is an object that contains information about
the current web request that has triggered this view,
and is an instance of the class django.http.HttpRequest.

Note: a view is just a Python function that takes an HttpRequest as
its first parameter and returns an instance of HttpResponse.
"""

"""================================
How Django processes a request
================================
A request comes in to /hello/.
Django determines the root URLconf by looking at the ROOT_URLCONF setting.
Django looks at all of the URLpatterns in the URLconf for the first one that
matches /hello/. If it finds a match, it calls the associated view function.
The view function returns an HttpResponse.
Django converts the HttpResponse to the proper HTTP response, which
results in a web page."""


def hello(request):
    return HttpResponse("Hello World ya dig")


def homepage(request):
    return HttpResponse("Yeah I'm sick like that")


""" template loading, context creation, template rendering, and HttpResponse
creation are all taken care of by the render() call. Because render()
returns an HttpResponse object, we can simply return that value in the view.


def current_datetime(request):
    time = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': time}))
    return HttpResponse(html)
"""


def current_datetime(request):
    now = datetime.datetime(request)
    return render(request, 'current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s. \
            </body></html>" % (offset, dt)
    return HttpResponse(html)
