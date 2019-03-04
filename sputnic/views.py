from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from sputnic.models import Sputnic


def index(request):
    return render(
        request=request,
        template_name='sputnic/index.html'
    )


class SputnicSearchView(ListView):
    model = Sputnic
    paginate_by = 5
    template_name = 'sputnic/index.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(Q(title__iregex=self.request.GET.get('search', '')) |
                       Q(description__iregex=self.request.GET.get('search', '')))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['count'] = self.get_queryset().count()
        context['title'] = 'Search results'
        context['search'] = self.request.GET.get('search', '')
        return context



