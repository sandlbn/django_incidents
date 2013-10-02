# Create your views here.
from .models import Incident
from .forms import IncidentForm
from django.views.generic.edit import CreateView


class IncidentCreate(CreateView):

    model = Incident
    form_class = IncidentForm
