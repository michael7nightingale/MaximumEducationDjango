from django import forms

from .models import Good


class GoodCreationForm(forms.ModelForm):
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "min-length": 5,
                "placeholder": "Title"
            }
        ),
        required=True
    )
    description = forms.CharField(
        max_length=255,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "min-length": 5,
                "placeholder": "Description"
            }
        ),
        required=True
    )
    amount = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "min": 1,
                "max": 10000,
                "value": 1,

            }
        ),
        required=True
    )
    price = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "min": 1,
                "max": 1000000,
            }
        ),
        required=True
    )
    discount = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "min": 0,
                "max": 99,
                "value": 0
            }
        ),
        required=True
    )
    photo = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                "placeholder": "Choose good photo"
            }
        ),
        required=True
    )

    class Meta:
        model = Good
        fields = ["title", "description", "amount", "price", "discount", "photo", "subcategory"]
