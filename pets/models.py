from django.db import models
# Importamos o modelo de usuário padrão do Django
from django.contrib.auth.models import User

# Opções de cores oficiais para padronizar o banco de dados
COR_CHOICES = (
    ('preto', 'Preto'),
    ('branco', 'Branco'),
    ('marrom', 'Marrom'),
    ('cinza', 'Cinza'),
    ('amarelo', 'Amarelo'),
    ('creme', 'Creme'),
    ('caramelo', 'Caramelo'),
    ('outra', 'Outra'),
)

class Animal(models.Model):
    
    STATUS_CHOICES = (
        ('perdido', 'Perdido'),
        ('encontrado', 'Encontrado'),
    )
    
    ESPECIE_CHOICES = (
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
        ('passaro', 'Pássaro'),
        ('outro', 'Outro'),
    )

    # NOVO CAMPO: Vincula o pet a um usuário logado.
    # on_delete=models.CASCADE significa que, se o usuário apagar a conta,
    # os alertas dele também serão apagados automaticamente.
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meus_pets', null=True, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='perdido')
    nome = models.CharField(max_length=100, null=True, blank=True)
    especie = models.CharField(max_length=50, choices=ESPECIE_CHOICES) 
    
    mais_de_uma_cor = models.BooleanField(default=False)
    cores = models.CharField(max_length=100, null=True, blank=True)
    
    foto = models.ImageField(upload_to='pets_fotos/', null=True, blank=True)
    
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    
    def __str__(self):
        if self.nome:
            return f"{self.nome} ({self.get_status_display()})"
        return f"{self.get_especie_display()} sem nome ({self.get_status_display()})"