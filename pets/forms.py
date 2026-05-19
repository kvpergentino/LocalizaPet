from django import forms
from .models import Animal, COR_CHOICES

class AnimalForm(forms.ModelForm):
    # Sobrescrevemos o campo cores para ser de múltipla escolha com checkboxes
    cores = forms.MultipleChoiceField(
        choices=COR_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'flex flex-wrap gap-4'}),
        required=False,
        label="Cores do Animal"
    )

    class Meta:
        model = Animal
        fields = ['status', 'nome', 'especie', 'mais_de_uma_cor', 'cores', 'foto', 'cep', 'bairro', 'cidade', 'uf']
        
        widgets = {
            'status': forms.Select(attrs={'class': 'w-full rounded-lg border-outline-variant/30 bg-surface p-2.5 text-on-surface'}),
            'nome': forms.TextInput(attrs={'class': 'w-full rounded-lg border-outline-variant/30 bg-surface p-2.5 text-on-surface', 'placeholder': 'Ex: Mio'}),
            'especie': forms.Select(attrs={'class': 'w-full rounded-lg border-outline-variant/30 bg-surface p-2.5 text-on-surface'}),
            'mais_de_uma_cor': forms.CheckboxInput(attrs={'class': 'rounded border-outline-variant/50 text-primary focus:ring-primary w-5 h-5'}),
            'foto': forms.FileInput(attrs={'class': 'w-full rounded-lg border-outline-variant/30 bg-surface p-2 text-on-surface'}),
            
            # CEP livre para digitar
            'cep': forms.TextInput(attrs={'class': 'w-full rounded-lg border-outline-variant/30 bg-surface p-2.5 text-on-surface', 'placeholder': 'Ex: 14000-000'}),
            
            # Campos bloqueados (readonly) com fundo levemente acinzentado para indicar que são automáticos
            'bairro': forms.TextInput(attrs={'class': 'w-full rounded-lg border-outline-variant/30 bg-surface-container-high p-2.5 text-on-surface-variant cursor-not-allowed', 'readonly': 'readonly'}),
            'cidade': forms.TextInput(attrs={'class': 'w-full rounded-lg border-outline-variant/30 bg-surface-container-high p-2.5 text-on-surface-variant cursor-not-allowed', 'readonly': 'readonly'}),
            'uf': forms.TextInput(attrs={'class': 'w-full rounded-lg border-outline-variant/30 bg-surface-container-high p-2.5 text-on-surface-variant cursor-not-allowed', 'readonly': 'readonly'}),
        }

    # Esta função junta as cores selecionadas em um texto único antes de salvar no banco
    def clean_cores(self):
        cores_list = self.cleaned_data.get('cores')
        if cores_list:
            return ", ".join(cores_list)
        return ""