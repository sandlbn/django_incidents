
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import StrictButton, UneditableField
from .models import Incident


class IncidentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(IncidentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-5'
        self.helper.form_action = '.'
        self.helper.layout = Layout(
            'start_date',
            'end_date',
            UneditableField('test', css_class="input-xlarge"),
            'street',
            'street_nr',
            'incident_type',
            Submit('submit', 'Submit')
        )

    class Meta:
        model = Incident

