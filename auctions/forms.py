import _datetime
from django import forms 

categories = (
            ("Antiques", "Antiques"),
            ("Drawing", "Drawing"),
            ("Watercolor", "Watercolor"),
            ("Design", "Design"),
            ("Miniature", "Miniature"),
            ("Painting", "Painting"),
            ("Photography", "Photography"),
            ("Sculpture", "Sculpture"),
            ("Prints", "Prints"),
            ("Oil", "Oil"),
            ("Acrylic", "Acrylic"),
            ("Original artwork", "Original artwork")
        )

def year_choices():
    return [(r,r) for r in range(_datetime.date.today().year, 1000 ,-1)]

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
    size = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "class": "form-control form-group",
            "placeholder": "Size"
        })
    )
    artist = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "class": "form-control form-group",
            "placeholder": "Artist"
        })
    )
    year = forms.ChoiceField(
        label="",
        widget=forms.Select(attrs={
            "class": "form-control form-group",
            "aria-describedby": "yearLabel"
       
            }),
        choices=year_choices()
    )
    avatar = forms.URLField(
        label="",
        widget=forms.URLInput(attrs={
            "class": "form-control form-group",
            "placeholder": "Give a link to an image of the artwork"
        })
    )
    open_price = forms.DecimalField(
        label="",
        widget=forms.NumberInput(attrs={
            "class": "form-control form-group",
            "placeholder": "Starting bid"
        })
    )
    category = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "form-check-input",
                "id": "category",
                "onclick": "maxCategorieChecked('category', this, 3)"
             
            }
        ),
        choices = categories,
    )

 
    def clean_category(self):
        data = self.cleaned_data['category']
        return ", ".join(data)
    
    # disable others checkboxes when one is checked

    


class CommentForm(forms.Form):
    comment = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            "class": "form-control form-group comment-textarea",
            "placeholder": "Leave a comment",
            "rows": 5
        })
    )

class BidForm(forms.Form):
    bid = forms.DecimalField(
        label="",
        widget=forms.NumberInput(attrs={
            "class": "form-control form-group",
            "placeholder": "Bid", "name": "bid"
        })
    )