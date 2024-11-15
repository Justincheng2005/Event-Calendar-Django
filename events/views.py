from django.utils import timezone
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Event
from users.models import Profile


def home(request):
    if(request.user.is_authenticated):
        profile, created = Profile.objects.get_or_create(user=request.user)
        events = profile.rsvped_events.filter(dateTime__gte=timezone.now()).order_by("dateTime")
        return render(request, 'events/home.html', {"events": events})
    else:
        return render(request, 'events/home.html', )
    
def event_calendar(request):
    events = Event.objects.filter(dateTime__gte=timezone.now()).order_by("dateTime")
    return render(request, "events/calendar.html", {"events": events})

class event_list(ListView):
    model = Event
    template_name = "events/list.html"
    def get_queryset(self):
        return  Event.objects.filter(dateTime__gte=timezone.now()).order_by("dateTime")