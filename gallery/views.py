from django.shortcuts import render,redirect
from django.http import HttpResponse ,Http404
import datetime as dt 
from .models import Image,Location,Category


# Create your views here.
def gallery_today(request):
    date = dt.date.today()
    images = Image.objects.all()
    return render(request,"all-gallery/today-gallery.html",{"date":date,"images":images,})

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
    gallery = Image.days_gallery(date)        
    return render(request,'all-gallery/past-gallery.html', {"date": date, "gallery":gallery,})

def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-gallery/search.html',{"message":message,"images":searched_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gallery/search.html',{"message":message})
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-gallery/image.html",{"image":image})
def filter_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        filtered_images = Image.filter_by_location(search_term)
        message = f"{search_term}"

        return render(request, 'all-gallery/search.html',{"message":message,"images":filtered_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gallery/search.html',{"message":message})


