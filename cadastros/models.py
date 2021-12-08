from django.db import models

# Create your models here.
class Campo(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição', max_length=200)

    def __str__(self) :
        return self.nome

class Atividade(models.Model):
    titulo = models.CharField('Titulo', max_length=50, default='')
    numero = models.IntegerField('Numero')
    descricao = models.TextField('Descrição', max_length=150)
    pontos = models.DecimalField(decimal_places=1, max_digits=4)
    detalhes = models.CharField('Detalhes', max_length=100)

    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)

    def __str__(self) :
        return  self.titulo

