from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    log_user = forms.BooleanField(required=False)

    class Meta:
        model = Author
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()

        if not cleaned_data.get('name'):
            raise forms.ValidationError("Name is required")

        if not cleaned_data.get('last_name'):
            raise forms.ValidationError("Last name is required")

        if cleaned_data.get('log_user'):
            self.cleaned_data['logged_user_name'] = f"{self.cleaned_data['name']} {self.cleaned_data['last_name']}"

        return cleaned_data

    