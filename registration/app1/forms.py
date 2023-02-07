#forms.py
from django import forms  
from app1.models import StudentForm  #models.py
    
class StudentForm(forms.ModelForm):  
    class Meta:  
        model = StudentForm  
        fields = "__all__"
        
        widgets={
            'email': forms.TextInput(attrs={'class':'form-control'}),
            
        }