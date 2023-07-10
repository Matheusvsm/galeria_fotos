from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome


class Foto(models.Model):
    imagem = models.ImageField(upload_to='fotos/')
    data_de_criacao = models.DateTimeField(auto_now_add=True)
    aprovada = models.BooleanField(default=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'Foto {self.id}'

class Comentario(models.Model):
    texto = models.TextField()
    data_de_criacao = models.DateTimeField(auto_now_add=True)
    foto = models.ForeignKey(Foto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comentario {self.id}'
