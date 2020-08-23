from django import forms
from .models import TaskBd

class ConteudoForm(forms.ModelForm):
    class Meta:
        model=TaskBd
        fields = ['conteudo','descricao',]
        widgets = {
			'conteudo':forms.TextInput(attrs={'placeholder':'Digite o nome da tarefa'}),
			'descricao':forms.Textarea(attrs={'placeholder':"Digite a descrição da tarefa"})
	
		}