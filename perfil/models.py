from django.db import models



class Perfil(models.Model):
    nome = models.CharField(max_length=50)
    amigos = models.ForeignKey("self")

class Usuario(models.Model):
    email = models.EmailField(max_length=254)
    data = models.DateField(auto_now_add=True)
    senha = models.CharField(max_length=16)
    perfil = models.ManyToManyField(Perfil)

class Postagem(models.Model):
    texto = models.CharField(max_length=50)
    data = models.DateField(auto_now_add=True)
    perfil = models.ManyToManyField(Perfil)

class Comentario(models.Model):
    texto = models.CharField(max_length=50)
    data = models.DateField(auto_now_add=True)
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE)
    postagem = models.ManyToManyField(Postagem)

class Reacao(models.Model):
    tipo = models.CharField(max_length=50)
    peso = models.CharField(max_length=50)
    data = models.DateField(auto_now_add=True)
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE)
    postagem = models.ManyToManyField(Postagem)

