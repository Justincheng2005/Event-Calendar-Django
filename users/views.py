from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Event, Profile


def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        mail=request.POST['email']
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        pwd1=request.POST["password"]
        pwd2=request.POST["password2"]

        if pwd1!=pwd2:
            messages.info(request,"Password doesn't match")
            redirect('register/')

        else:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Sorry! Username already registered")
                return redirect ('register')
            else:
                new_user=User.objects.create_user(username=username, first_name=fname, last_name=lname, email=mail,password=pwd1)
                Profile.objects.create(user=new_user)
                user = authenticate(request, username=new_user.username, password=pwd1)
                if user is not None:
                    login(request, user)
                messages.success(request, f'Thanks for registering {new_user.username}.', extra_tags='alert alert-success alert-dismissible fade show')
                return redirect('/')
    return render(request,'users/register.html')

@login_required
def joinEvent(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        event_id = data.get("event_id")
        event = get_object_or_404(Event, id=event_id)
        profile, created = Profile.objects.get_or_create(user=request.user)

        if event in profile.rsvped_events.all():
            return JsonResponse({"status": "already_joined", "message": "You have already added this event to your calendar."})

        profile.rsvped_events.add(event)
        return JsonResponse({"status": "success", "message": "You have successfully added the event to your calendar."})
    return JsonResponse({"status": "error", "message": "Invalid request method."})

@login_required
def leaveEvent(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        event_id = data.get("event_id")
        event = get_object_or_404(Event, id=event_id)
        profile = Profile.objects.get(user=request.user)
        
        if event in profile.rsvped_events.all():
            profile.rsvped_events.remove(event)
            return JsonResponse({"status": "success", "message": "You have successfully un-RSVPed from the event."})
        else:
            return JsonResponse({"status": "error", "message": "You are not RSVPed for this event."})
    
    return JsonResponse({"status": "error", "message": "Invalid request method."})