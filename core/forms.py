from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'location', 'skills']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'w-full p-2 border rounded-lg text-gray-900'}),
            'location': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg text-gray-900'}),
            'skills': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg text-gray-900'}),
        }