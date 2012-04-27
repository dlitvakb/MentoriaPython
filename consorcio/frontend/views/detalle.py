from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.contrib.auth.models import AnonymousUser

class DetalleView(TemplateView):
    url = r'^detalle/'
    template_name = 'frontend/detalle.html'

    def get(self, request):
        return self.render_to_response({'request': request})
