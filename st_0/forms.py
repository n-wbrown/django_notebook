from django import forms
from .models import box
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

    def clean_new_mass(self):
        data = self.cleaned_data['new_mass']
        if data < 0 :
            raise ValidationError(_('Negative mass!'))
        return data


