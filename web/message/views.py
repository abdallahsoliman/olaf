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
        contacts = self.request.user.contact_set.annotate(latest_active=Max("phonenumber__message__received_at")).order_by("-latest_active")
        context['contacts'] = contacts
        return context

