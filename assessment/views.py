from django.shortcuts import render, redirect
from .forms import ContactForm

def homepage_view(request):
    return render(request, 'assessment/home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'assessment/contact.html', {'form': form})

def success_view(request):
    return render(request, 'assessment/success.html')

def about_view(request):
    return render(request, 'assessment/about.html')

def projects_view(request):
    return render(request, 'assessment/projects.html')
