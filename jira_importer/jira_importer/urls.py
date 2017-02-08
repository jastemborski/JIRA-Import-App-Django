"""jira_importer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

'''
to hook a view function to a particular URL with Django, we use a URLconf. A URLconf 
is like a table of contents for your Django-powered web site. Basically, it's a mapping
 between URLs and the view functions that should be called for those URLs. It's how you 
 tell Django, For this URL, call this code, and for that URL, call that code.

For example, when somebody visits the URL /foo/, call the view function foo_view(), 
which lives in the Python module views.py. When you executed django-admin startproject in 
the previous chapter, the script created a URLconf for you automatically: the file urls.py.
'''
from django.conf.urls import url
from django.contrib import admin
from jira_importer.views import hello, homepage, current_datetime

"""
 This variable defines the mapping between URLs and the code that handles those URLs. To add 
 a URL and view to the URLconf, just add a mapping between a URL pattern and the view function. 
"""
"""
One more important detail we've introduced here is that r character in front of the regular expression string. This tells Python that the string is a raw string-its contents should not interpret backslashes.
"""
"""
regex are important to be able to work with
"""
"""
 The variable name doesn't matter; all that matters is that it's the second argument to the function, after request. (It's also possible to use keyword, rather than positional, arguments in a URLconf. I cover that in Chapter 7, Advanced Views and URLconfs.)
"""
urlpatterns = [
	url(r'^$', homepage),
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello), 
    url(r'^time/$', current_datetime), 
    url(r'^time/plus/\d(1,2)/$', hours_ahead), 
]

"""
The first argument is a pattern-matching string (a regular expression; more on this in a bit) and the second argument is the view function to use for that pattern.
"""
