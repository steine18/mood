from django.shortcuts import render
from .models import Log
from .forms import LogForm

from django.utils import timezone


# Create your views here.
def log_view(request):
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.date = timezone.now()
            log.save()
    else:
        form = LogForm()

    log = Log.objects.all()

    return render(request, 'tracker/log_view.html', {'log':log,
                                                     'form':form,})