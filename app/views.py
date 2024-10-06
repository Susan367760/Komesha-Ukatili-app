from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request, 'index.html')

def submit_report(request):
    if request.method == 'POST' and request.FILES.get('media'):
        media = request.FILES['media']
        description = request.POST.get('description', '')
        fs = FileSystemStorage()
        filename = fs.save(media.name, media)
        media_url = fs.url(filename)
        
        # Save report logic here (e.g., saving to the database)
        
        return redirect('index')
    
    return render(request, 'index.html')

