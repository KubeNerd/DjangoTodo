from django.db import models

# Create your models here.
class TaskBd(models.Model):
    conteudo=models.CharField(max_length=1000)
    #assunto=models.CharField(max_length=100)
    data=models.DateTimeField(auto_now_add=True)
    descricao=models.TextField()

    def __str__(self):
        return str(self.id)