from django_app.models import contact
from django.forms import ModelForm
from captcha.fields import CaptchaField



class contactform(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = contact
        fields = '__all__'

