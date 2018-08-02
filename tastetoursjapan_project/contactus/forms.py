# contactus/forms.py
from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['from_email'].label = "Your email:"
        self.fields['subject'].label = "Subject:"
        self.fields['message'].label = "What would you like to ask us?"
        # Google reCaptcha
        # self.request = kwargs.pop('request', None)
        # super(MyModelForm, self).__init__(*args, **kwargs)

# google recaptcha
    # def clean(self):
    #         ca = self.request.POST["g-recaptcha-response"]
    #         url = "https://www.google.com/recaptcha/api/siteverify"
    #         params = {
    #             'secret': config.RECAPTCHA_SECRET_KEY,
    #             'response': ca,
    #             'remoteip': utility.get_client_ip(self.request)
    #         }
    #         verify_rs = requests.get(url, params=params, verify=True)
    #         verify_rs = verify_rs.json()
    #         status = verify_rs.get("success", False)
    #         if not status:
    #             raise forms.ValidationError(
    #                 _('Captcha Validation Failed.'),
    #                 code='invalid',
    #             )
