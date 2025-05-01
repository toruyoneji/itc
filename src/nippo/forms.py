from django import forms
from .models import NippoModel


class NippoFormModel(forms.ModelForm):
    class Meta:
        model=NippoModel
        fields="__all__"
        #exclude = ['user']

# class NippoFormClass(forms.Form):
#      title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'タイトル...'}))
#      content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '内容...'}))

#     #def __init__(self, *args, **kwargs):
#        #self.base_fields['title'].initial = 'basefield'
#        #super().__init__(*args, **kwargs)

    def __init__(self, user=None,*args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs["class"] = "form-control"
            self.user = user
        super().__init__(*args, **kwargs)