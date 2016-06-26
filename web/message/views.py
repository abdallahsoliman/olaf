from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . import models

class MessageList(ListView):
    model = models.Message

    def get_queryset(self, contact):
        return models.Message.objects.all(sender=contact).order_by('-received_at')

class MessageView(TemplateView):
    template_name = "message/index.html"

    def get_context_data(self, **kwargs):
        context = super(MessageView, self).get_context_data(**kwargs)
        context['contacts'] = models.Contact.objects.all()
        return context

