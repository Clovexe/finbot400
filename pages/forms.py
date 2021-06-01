from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import PasswordChangeForm
from users.models import Costumer

class CostumerForms(forms.ModelForm):
    firstname = forms.CharField(required=True,
                widget=forms.TextInput(
                    attrs={
                        "type":"text",
                        "name":"firstname",
                        "placeholder": "Ex Juan"
                    }
                )
    )
    lastname = forms.CharField(required=True,
                widget=forms.TextInput(
                    attrs={
                        "type":"text",
                        "name":"lastname",
                        "placeholder": "Dela Cruz"
                    }
                )
    )
    username = forms.CharField(required=True,
                widget=forms.TextInput(
                    attrs={
                        "type":"text",
                        "name":"username",
                        "placeholder": "What should we call you?"
                    }
                )
    )
    email = forms.CharField(required=True,
                widget=forms.TextInput(
                    attrs={
                        "type":"email",
                        "name":"lastname",
                        "placeholder": "Dela Cruz"
                    }
                )
    )
    contact = forms.CharField(required=True,
                widget=forms.TextInput(
                    attrs={
                        "type":"number",
                        "name":"contact",
                        "placeholder": "997XXXXXXX"
                    }
                )
    )
    password = forms.CharField(required=True,
                widget=forms.TextInput(
                    attrs={
                        "type":"password",
                        "name":"password",
                        "placeholder": "Please Make Password as Secure as Possible"
                    }
                )
    )
  
    about = forms.CharField(required=False,
            widget=forms.Textarea(
                    attrs={
                        "placeholder": "Tell us something about you",
                        "rows": 20,
                        "cols":50,
                    }
                )
    )
    class Meta:
        model = Costumer
        fields=[
            "firstname",
            "lastname",
            "username",
            "email",
            "password",
           
        ]
    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        if costumer.objects.filter(username=username).exists():
            raise forms.ValidationError('This username address is already in use.')
        else: return username
        
        

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if ".com" not in email:
            raise costumer.ValidationError("Invalid email")
        email = self.cleaned_data.get('email')

        if costumer.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        else:return email

            
        
        

    def clean_password(self, *args, **kwargs):
        passw  = self.cleaned_data.get("password")
        
        if len(passw) < 8:
            raise forms.ValidationError("Minimum 8 Characters for Passwords ")
        
        if len(passw) > 15:
            raise forms.ValidationError("Maximum 15 Characters for Passwords ")
        return passw

class UpdateForms(forms.ModelForm):
    firstname = forms.CharField(required=True,
                widget=forms.TextInput(
                    attrs={
                        "type":"text",
                        "name":"firstname",
                        "placeholder": "Ex Juan"
                    }
                )
    )
    lastname = forms.CharField(required=True,
                widget=forms.TextInput(
                    attrs={
                        "type":"text",
                        "name":"lastname",
                        "placeholder": "Dela Cruz"
                    }
                )
    )


    contact = forms.CharField(required=True,
                widget=forms.TextInput(
                    attrs={
                        "type":"number",
                        "name":"contact",
                        "placeholder": "997XXXXXXX"
                    }
                )
    )
  
    about = forms.CharField(required=False,
            widget=forms.Textarea(
                    attrs={
                        "placeholder": "Tell us something about you",
                        "rows": 10,
                        "cols":50,
                    }
                )
    )
    class Meta:
        model = Costumer
        fields=[
            "firstname",
            "lastname",
            "contact",
            "about"
            
           
        ]
    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        if costumer.objects.filter(username=username).exists():
            raise forms.ValidationError('This username address is already in use.')
        else: return username
        
        

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if ".com" not in email:
            raise costumer.ValidationError("Invalid email")
        email = self.cleaned_data.get('email')

        if costumer.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        else:return email    


class PasswordForms(PasswordChangeForm):
    old_password = forms.CharField(required=True,
                widget=forms.TextInput(
                    attrs={
                        "type":"password",
                        "name":"old_password",
                        "placeholder": "Please Make Password as Secure as Possible"
                    }
                )
    )
    new_password1 = forms.CharField(required=True,
                widget=forms.TextInput(
                    attrs={
                        "type":"password",
                        "name":"new_password1",
                        "placeholder": "Please Make Password as Secure as Possible"
                    }
                )
    )
    new_password2 = forms.CharField(required=True,
                widget=forms.TextInput(
                    attrs={
                        "type":"password",
                        "name":"new_password2",
                        "placeholder": "Please Make Password as Secure as Possible"
                    }
                )
    )
    class Meta:
        model = Costumer
        fields = ('old_password', 'new_password1', 'new_password2')

            
   
