
from django.forms import ModelForm
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            "title",
            "price",
            "num_bedrooms",
            "num_halls",
            "Square_footage",
            "Address",
            "image",
        ]

