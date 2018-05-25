# contactus/views.py
from django.core.mail import EmailMultiAlternatives, send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
import json
import urllib
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
            # ''' Begin reCAPTCHA validation ''' Need to figure our reCapture
            # recaptcha_response = request.POST.get('g-recaptcha-response')
            # url = 'https://www.google.com/recaptcha/api/siteverify'
            # values = {
            #     'secret': "6LfZdVsUAAAAAOaNhC1XIaY7u-CQrOGpTjcJAx2p",
            #     'response': recaptcha_response
            # }
            # data = urllib.parse.urlencode(values).encode()
            # req =  urllib.request.Request(url, data=data)
            # response = urllib.request.urlopen(req)
            # result = json.loads(response.read().decode())
            # ''' End reCAPTCHA validation '''

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
                return HttpResponse('Invalid reCapture. Please try again')
            messages.success(request, 'The form has been sent successfully. Thank you for getting in touch with us!' , extra_tags='alert')
    return render(request, "contactus/email.html", {'form': form})
