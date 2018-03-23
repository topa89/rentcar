from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from .models import Subscribers
from .forms import SubscriberForm

@require_POST
def addSub(request):
    form = SubscriberForm(request.POST)

    if form.is_valid():
        new_sub = Subscribers(email=request.POST['email'])
        new_sub.save()

    return redirect('/')