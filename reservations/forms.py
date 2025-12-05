from django import forms

class ReservationForm(forms.Form):
    date = forms.DateField(label="Tarih")
    start_time = forms.TimeField(label="Başlangıç Saati")
    end_time = forms.TimeField(label="Bitiş Saati")
