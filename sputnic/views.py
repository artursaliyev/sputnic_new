from django.contrib.postgres.search import SearchVector
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from sputnic.models import Sputnic


class IndexView(TemplateView):
    template_name = 'sputnic/index.html'


class SputnicSearchView(ListView):
    model = Sputnic
    paginate_by = 5
    template_name = 'sputnic/index.html'

    def get_queryset(self):
        qs = super().get_queryset()

        qs_a = qs.annotate(search=SearchVector('title', 'description', config='russian')).\
            filter(search=self.request.GET.get('search', ''))

        if not qs_a:
            print(qs_a)
            query = self.request.GET.get('search', '').split()
            query = " & ".join(query)
            if query:
                query += ":*"

            qs_b = qs.extra(where=['search_vector @@ (to_tsquery(%s)) = true'], params=[query])
            return qs_b

        return qs_a

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Search results'
        context['search'] = self.request.GET.get('search', '')
        return context


class SputnicDetailView(DetailView):
    model = Sputnic
    template_name = 'sputnic/detail.html'

