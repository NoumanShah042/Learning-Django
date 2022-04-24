from django.shortcuts import render
from django.views.generic.base import TemplateView

# class HomeTemplateView(TemplateView):
#     template_name = 'school/home.html'

class HomeTemplateView(TemplateView):
    template_name = 'school/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Sonam'
        context['roll'] = 101
        # context = {                                   # extra context problem in this syntax
        #     'name': 'Sonam',
        #     'roll': 101
        # }
        print(context)
        print(kwargs)   #  get get from url file ( cl )
        # we can use this context in the above mentioned html file ( extra context will automatically passed )
        return context
