from django import forms

from music_works.models import Work_Metadata

class Work_Metadata_Form(forms.ModelForm):
    class Meta:
        model = Work_Metadata
        fields = ('title','contributor','iswc')
    