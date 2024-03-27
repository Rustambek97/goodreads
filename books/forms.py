from django import forms

from books.models import Review


class BookReviewForm(forms.ModelForm):
    stars = forms.IntegerField(min_value=1, max_value=5)
    class Meta:
        model = Review
        fields = ('stars', 'description')