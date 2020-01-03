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
            obj, created = Log.objects.update_or_create(
                date=timezone.now(),user=request.user,
                defaults={'response': log.response},)
            obj.save()

    if request.user.is_authenticated:
        log = Log.objects.filter(user=request.user)
        form = LogForm()
        context ={'log':log,
                  'form':form,}
    else:
        context={'log':[],
                  'form':''}
    return render(request, 'tracker/log_view.html', context)