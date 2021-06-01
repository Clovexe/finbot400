from django import forms
from .models import product

class product_form(forms.ModelForm):
    title       = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "placeholder":"The Title"
    }))
    
    description = forms.CharField(
                    required=False, 
                    widget=forms.Textarea(
                        attrs={
                            "class": "new-class-name two",
                            "rows": 20,
                            "cols":50,

                        }
                        ))
    price       = forms.DecimalField()

    class Meta:
        model = product
        fields =[
            'title',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "Item" in title:
            raise forms.ValidationError("This is an invalid title")
        if len(title) < 8:
            raise forms.ValidationError("The title is less than the required lenght min 8")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("com"):
            raise forms.ValidationError("This is not a valid email")
        return email

class raw_product_form(forms.Form):
    title       = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "placeholder":"The Title"
    }))
    description = forms.CharField(
                    required=False, 
                    widget=forms.Textarea(
                        attrs={
                            "class": "new-class-name two",
                            "rows": 20,
                            "cols":50,

                        }
                        ))
    price       = forms.DecimalField()