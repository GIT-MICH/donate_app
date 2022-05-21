from django import forms

from portfoliolab_app.models import Institution, Account


class DonationForm(forms.Form):
    quantity = forms.IntegerField()
    # categories = forms.MultipleChoiceField(Category, widget=forms.CheckboxSelectMultiple),
    institution = forms.ModelChoiceField(queryset=Institution.objects.all())
    phone_number = forms.CharField(max_length=20)
    address = forms.CharField(max_length=20)
    city = forms.CharField(max_length=20)
    zip_code = forms.IntegerField()
    pick_up_date = forms.DateField() #initial=datetime.date
    pick_up_time = forms.TimeField() #(default=timezone.now)
    pick_up_comment = forms.CharField(widget=forms.Textarea)#, default='Brak uwag') #(default='Brak uwag')
    user = forms.ModelChoiceField(queryset=Account.objects.all())
#   default_data = {'pick_up_comment': 'Brak uwag'}