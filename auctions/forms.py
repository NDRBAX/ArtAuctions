from django import forms 

class ListingForm(forms.Form):
    title = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "class": "form-control form-group",
            "placeholder": "Title"
        })
    )
    description = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            "class": "form-control form-group",
            "placeholder": "Description"
        })

    )
    avatar = forms.URLField(
        label="",
        widget=forms.URLInput(attrs={
            "class": "form-control form-group",
            "placeholder": "Image"
        })
    )
    price = forms.DecimalField(
        label="",
        widget=forms.NumberInput(attrs={
            "class": "form-control form-group",
            "placeholder": "Price"
        })
    )
    open_price = forms.DecimalField(
        label="",
        widget=forms.NumberInput(attrs={
            "class": "form-control form-group",
            "placeholder": "Open Price"
        })
    )
    category = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "class": "form-control form-group",
            "autocomplete": "on",
            "placeholder": "Category"
        })
    )

class CommentForm(forms.Form):
    comment = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            "class": "form-control form-group",
            "placeholder": "Comment"
        })
    )