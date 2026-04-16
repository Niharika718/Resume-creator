from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        widgets = {
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            
            'career_objective':forms.Textarea(attrs={'class': 'form-control'}),
            'education': forms.Textarea(attrs={'class': 'form-control'}),
            't_skills': forms.Textarea(attrs={'class': 'form-control'}),
            's_skills': forms.Textarea(attrs={'class': 'form-control'}),
             'projects': forms.Textarea(attrs={'class': 'form-control'}),
            
            'experience': forms.Textarea(attrs={'class': 'form-control'}),
        }