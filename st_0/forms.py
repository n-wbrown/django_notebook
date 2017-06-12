from django import forms
from .models import box



class indivTrigger(forms.Form):
    name = forms.CharField(
        label="EEE",
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'CUSTOM! Text',
            'id_extras': 'PREFIX',
        }
    ))

    def clean_name(self):
        data = self.cleaned_data['name']
        if len(data) <= 0 :
            raise forms.ValidationError(_('No Name'))
        # if 1:
        # raise forms.ValidationError("ERROR",code="bad")
        return data


class configureBox(forms.Form):
    
    class Meta:
        model = box
    
    new_name = forms.CharField(
        label="Box Name",
        max_length=10, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username','type':'text'})
    )
    
    new_mass= forms.DecimalField(
        label="Box Mass",
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control','type':'number'}),
    )
    '''
    new_color=forms.CharField(
        label="Box Color",
        ChoiceField = box.colors,
    )
    '''
    new_color=forms.ChoiceField(
        label="Box Color",
        choices = box.colors,
        widget=forms.Select(attrs={'class': 'custom-select',}),
    )

    extra_count = forms.CharField(
        label="count Field",
        widget=forms.HiddenInput()
    )

    
    def clean_new_mass(self):
        data = self.cleaned_data['new_mass']
        if data < 0 :
            raise ValidationError(_('Negative mass!'))
        return data


    def __init__(self,*args,**kwargs):
        # print("from forms:",args,kwargs)
        extra_fields=kwargs.pop('extra',0)
        super().__init__(*args,**kwargs)

        self.fields['extra_count'].initial = extra_fields

        for index in range(int(extra_fields)):
            # generate extra fields in the number specified via extra_fields
            self.fields['extra_field_{index}'.format(index=index)] = forms.CharField( label = 'extra_field_{index}'.format(index=index))
            #self.fields['extra_field_{index}'.format(index=index)] = forms.CharField()





