from django import forms
from .models import NippoModel
from bootstrap_datepicker_plus.widgets import DatePickerInput


class NippoFormModel(forms.ModelForm):
     date = forms.DateField(
        label="作成日",
        widget=DatePickerInput(format='%Y-%m-%d')
    )
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

        def __init__(self, *args, **kwargs):
            for key, field in self.base_fields.items():
                if key != "public":
                    field.widget.attrs["class"] = "form-control"
                else:
                    field.widget.attrs["class"] = "form-check-input"
            super().__init__(*args, **kwargs)