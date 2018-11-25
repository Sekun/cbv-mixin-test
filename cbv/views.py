from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

class View1(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('cbv.do_something'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponse("Contenu view1")

class View2(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        response =  super().dispatch(request, *args, **kwargs)
        if not request.user.has_perm('cbv.do_something'):
            raise PermissionDenied
        return response

    def get(self, request, *args, **kwargs):
        return HttpResponse("Contenu view2")

@method_decorator(login_required, name='dispatch')
class View3(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('cbv.do_something'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponse("Contenu view2")

