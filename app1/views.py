from django.shortcuts import render, redirect
from.forms import ResumeForm
from .models import Resume

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def create_resume(request):
    form = ResumeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('resume_list')
    return render(request, 'form.html', {'form': form})

def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'list.html', {'resumes': resumes})

def download_resume(request, id):
    resume = Resume.objects.get(id=id)

    template = get_template('resume_pdf.html')
    html = template.render({'resume': resume})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    pisa.CreatePDF(html, dest=response)

    return response

def update_resume(request, id):
    resume = Resume.objects.get(id=id)
    
    form = ResumeForm(request.POST or None, request.FILES or None, instance=resume)
    
    if form.is_valid():
        form.save()
        return redirect('resume_list')
    
    return render(request, 'form.html', {'form': form, 'is_edit': True})

def delete_resume(request, id):
    resume = Resume.objects.get(id=id)
    resume.delete()
    return redirect('resume_list')