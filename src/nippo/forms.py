from django import forms

class NippoFormClass(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'タイトル...'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '内容...'}))

    #def __init__(self, *args, **kwargs):
       #self.base_fields['title'].initial = 'basefield'
       #super().__init__(*args, **kwargs)