from django.http import HttpResponse

from django.shortcuts import render
from .forms import ImageForm

from . import ainetwork


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            imf = 'img/' + form.instance.image.name
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance

            img_obj.title = ainetwork.predict(imf)
            
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})
