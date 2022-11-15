from django import forms
#from library.models import Lib_Man_Sys_Table
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User


#class CourseForm(forms.ModelForm):
#    #name=forms.CharField()
#    #price=forms.IntegerField()
#    #category=forms.CharField()

#    class Meta:
#        model = Lib_Man_Sys_Table
#        fields ="__all__"
#        #fields = ['name','price']

class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUser, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
