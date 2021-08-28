from django.forms import ModelForm, TextInput
from .models import MainCities, Client

# class ClientForm(ModelForm):
#     class Meta:
#         model = Client
#         fields = {
#             'user'
#         }
#         widgets = {'name': TextInput(attrs={'class': 'searchInput', 'placeholder': 'Choose a city...'})}