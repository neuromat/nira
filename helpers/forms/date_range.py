from django import forms
from django.utils.translation import ugettext_lazy as _


#  Form with jquerys datepicker
DateInput = forms.DateInput(format=['%d-%m-%Y'], attrs={'class': 'datepicker'})


#  Creates a form that comes with the datepicker widget
class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=DateInput, label=_('Start date'), required=False)
    end_date = forms.DateField(widget=DateInput, label=_('End date'), required=False)
