from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'valor mínimo: R$20000')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1960:
            self.add_error('factory_year', 'Não é possível cadastrar carros anteriores a 1960')
        return factory_year

    def clean_model_year(self):
        model_year = self.cleaned_data.get('model_year')
        if model_year < 1960:
            self.add_error('model_year', 'Não é possível cadastrar carros anteriores a 1960')
        return model_year
