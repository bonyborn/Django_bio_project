from django.shortcuts import render, redirect
from .forms import BioForm
from .models import Bio

def create_bio(request):
    if request.method == 'POST':
        form = BioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_bio')
    else:
        form = BioForm()
    return render(request, 'bioapp/bio_form.html', {'form': form})

def view_bio(request):
    bios = Bio.objects.all()
    return render(request, 'bioapp/bio_view.html', {'bios': bios})