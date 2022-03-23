from django.db.models import Count
from django.shortcuts import render
from leaveformapp.models import Students
from django.contrib import messages
from datetime import datetime, timedelta
import pytz


# Create your views here.


def form(request):
    if request.method == 'POST':
        # getting form values
        name = request.POST['fullname']
        crn = request.POST['number']
        year = request.POST['year']
        reason = request.POST['reason']
        # time in db
        tz_ktm = pytz.timezone('Asia/Kathmandu')
        now = datetime.now(tz_ktm)
        now = str(now).split(" ")
        date = now[0]
        time = now[1].split(".")[0]

        # message displaying and saving if form is correct
        if len(name) < 2 or len(crn) != 6 or len(reason) < 2:
            messages.error(request, "Please fill the aplication correctly")
            return render(request, 'form.html')

        else:
            instance = Students(fullname=name, roll=crn,
                                year=year, reason=reason, createdDate=date, createdTime=time)
            instance.save()
            messages.success(request, "Your Application has been Submitted")
            return render(request, 'form.html')
        return render(request, 'form.html')
    else:
        return render(request, 'form.html')


def listofapplicants(request):

    # searching in db
    if request.method == 'POST':
        searched = request.POST['searched']

        searched_data = Students.objects.filter(
            roll=searched).order_by('-id')

        return render(request, 'applicants.html', {'searched_data': searched_data})
        # if not searching
    else:
        tz_ktm = pytz.timezone('Asia/Kathmandu')
        now = datetime.now(tz_ktm)
        # grouping by dates today ,yesterday, ani tyo paxi date chai sabai eutai ma
        # dates
        today = str(now).split(" ")[0]
        yesterday = str(now-timedelta(days=1)).split(" ")[0]
        remainingdays = str(now-timedelta(days=2)).split(" ")[0]
        # ---
        todaydata = Students.objects.all().filter(
            createdDate=today).order_by('-id')

        yesterdaydata = Students.objects.all().filter(
            createdDate=yesterday).order_by('-id')

        remainingdata = Students.objects.all()

        context = {
            'today': todaydata,
            'yesterday': yesterdaydata,
            'remainings': remainingdata
        }
        return render(request, 'applicants.html', context)
        # return render(request, 'applicants.html', {'list_of_object': Alldatas})
