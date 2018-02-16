# contactus/views.py
from django.core.mail import EmailMultiAlternatives, send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
import os
import requests
from .forms import ContactForm


# Create your views here.
def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:

                subject = '"{}" has sent a "contact us" form via the website'.format(form.cleaned_data['from_email'])
                text_content = "We have received a request from '{}' with the subject heading '{}' and the message as follows: '{}'".format(form.cleaned_data['contact_name'],form.cleaned_data['subject'],form.cleaned_data['message'])
                # html_content = "<p>We have received a request from '{}'<br> with the subject heading '{}' <br>and the message as follows: {}</p>".format(form.cleaned_data['contact_name'],form.cleaned_data['subject'],form.cleaned_data['message'])
                msg = EmailMultiAlternatives(subject, text_content, to=["customersupport@tastetourstokyo.com"])
                # msg.attach_alternative("html body", "text/html")
                msg.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'The form has been sent successfully. Thank you for getting in touch with us!')
    return render(request, "contactus/email.html", {'form': form})
