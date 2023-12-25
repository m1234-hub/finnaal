from django.shortcuts import render, HttpResponseRedirect
from.forms import StudentRegistration
from .models import User
# Create your views here.

#This function will add new item and add all items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            pry = fm.cleaned_data['pair']
            ssy = fm.cleaned_data['session']
            ppy = fm.cleaned_data['pips']
            dty = fm.cleaned_data['date']
            ety = fm.cleaned_data['entry_time']
            cmy = fm.cleaned_data['comment']
            bcy = fm.cleaned_data['before_chart']
            acy = fm.cleaned_data['after_chart']
            reg = User(pair=pry, session=ssy, pips=ppy, date=dty, entry_time=ety, comment=cmy, before_chart=bcy, after_chart=acy)

            reg.save()
            fm = StudentRegistration()
            
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

#This Funntion will update/Edit
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)

    return render(request, 'enroll/updatestu.html' , {'form':fm})

#This function will delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
