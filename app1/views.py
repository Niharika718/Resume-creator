from django.shortcuts import render, redirect
from.forms import ResumeForm
from .models import Resume



def create_resume(request):
    form = ResumeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('resume_list')
    return render(request, 'form.html', {'form': form})

def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'list.html', {'resumes': resumes})


def update_resume(request, id):
    resume = Resume.objects.get(id=id)
    
    form = ResumeForm(request.POST or None, request.FILES or None, instance=resume)
    
    if form.is_valid():
        form.save()
        return redirect('resume_list')
    
    return render(request, 'form.html', {'form': form, 'is_edit': True})

def resume_detail(request, id):
    resume = Resume.objects.get(id=id)
    return render(request, 'resume_detail.html', {'resume': resume})


def delete_resume(request, id):
    resume = Resume.objects.get(id=id)
    resume.delete()
    return redirect('resume_list')