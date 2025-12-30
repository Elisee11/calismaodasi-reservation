from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    date = forms.DateField(
        input_formats=['%d.%m.%Y'],
        widget=forms.DateInput(
            format='%d.%m.%Y',
            attrs={'placeholder': 'JJ.MM.AAAA'}
        )
    )

    class Meta:
        model = Reservation
        fields = ['date', 'start_time', 'end_time']
