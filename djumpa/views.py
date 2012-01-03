from django.views.generic.base import RedirectView
from django.http import Http404

from .models import Djumpa

class DjumpaRedirectView(RedirectView):
    model           = NotImplemented
    redirect_field  = NotImplemented
    permanent       = False

    def get_redirect_url(self, **kwargs):
        try:
            obj = self.model.objects.get(pk=kwargs['pk'])
            redirect = getattr(obj, self.redirect_field)
        except:
            raise Http404
        Djumpa.objects.create(
            referer     = self.request.META.get('HTTP_REFERER'),
            sessionid   = self.request.session.session_key,
            redirect    = redirect,
            rank        = self.request.GET.get('rank')
        )
        return redirect

