import _datetime
from django import forms 
from multiselectfield import MultiSelectField

# categories = (
#             ("Antiques", "Antiques"),
#             ("Drawing", "Drawing"),
#             ("Watercolor", "Watercolor"),
#             ("Design", "Design"),
#             ("Miniature", "Miniature"),
#             ("Painting", "Painting"),
#             ("Photography", "Photography"),
#             ("Sculpture", "Sculpture"),
#             ("Prints", "Prints"),
#             ("Oil", "Oil"),
#             ("Acrylic", "Acrylic"),
#             ("Original artwork", "Original artwork")
#         )

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
    category = MultiSelectField()



    # category = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple(),
    #     choices = categories,
    # )

    # category = MultiSelectField(choices=categories,
    #                             max_choices=3,
    #                             max_length=3)

    # def clean_category(self):
    #     data = self.cleaned_data['category']
    #     return ", ".join(data)
    
    # # when the user select three categories, others will be disabled
    # def __init__(self, *args, **kwargs):
    #     self.max_choices = 3
    #     super(ListingForm, self).__init__(*args, **kwargs)
    
    # def clean(self):
    #     cleaned_data = super(ListingForm, self).clean()
    #     category = cleaned_data.get('category')
    #     if len(category) > self.max_choices:
    #         raise forms.ValidationError('You can select only 3 categories')
    #     return cleaned_data
    
  


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