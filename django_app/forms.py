from django_app.models import contact
from django.forms import ModelForm


class contactform(ModelForm):
    class Meta:
        model = contact
        fields = '__all__'