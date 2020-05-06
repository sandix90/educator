from django import forms

from educator.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['sender_name', 'email', 'text']
        widgets = {
            'sender_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'email': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'text': forms.Textarea(
                attrs={'class': 'form-control'}
            )
        }
