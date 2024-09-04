from django.forms import ModelForm
from .models import Investimento


class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimento
        fields = '__all__'
        
# class Meta: é o campo onde vocÊ dá as especificações para o formulário

# model = investimento: serve para especificar que todos os objetos presentes no modelo Investimento estarão disponiveis para o formulario
        
#fields: Este atributo define quais campos do modelo devem ser incluídos no formulário. Quando você usa __all__, 
# está dizendo ao Django para incluir todos os campos do modelo Investimento no formulário.
#Se você quisesse incluir apenas alguns campos específicos, poderia fazer algo como fields = ['campo1', 'campo2'].