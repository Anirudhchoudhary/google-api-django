from django.views.generic import TemplateView
from oauth2client.contrib.django_util import oauth2_settings

class Home(TemplateView):
    template_name = 'base.html'