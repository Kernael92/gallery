from django.shortcuts import render,redirect
from django.http import HttpResponse ,Http404
import datetime as dt 


# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def gallery_today(request):
    date = dt.date.today()
    return render(request, 'all-gallery/today-gallery.html', {"date": date,})

def past_days_gallery(request,past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assertFalse
    if date == dt.date.today():
        return redirect(gallery_today)

    
            
    return render(request,'all-gallery/past-gallery.html', {"date": date,})


