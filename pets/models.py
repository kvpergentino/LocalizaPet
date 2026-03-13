from django.db import models

class Animal(models.Model):
    
    # Opções de status do animal: perdido ou encontrado
    STATUS_CHOICES = (
        ('perdido', 'Perdido'),
        ('encontrado', 'Encontrado'),
    )
    
    # Opções de espécie do animal: cachorro, gato, pássaro ou outro
    ESPECIE_CHOICES = (
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
        ('passaro', 'Pássaro'),
        ('outro', 'Outro'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='perdido')
    
    
    # Nome opcional no banco, para permitir o cadastro de animais encontrados
    nome = models.CharField(max_length=100, null=True, blank=True)
    especie = models.CharField(max_length=50, choices=ESPECIE_CHOICES) 
    
    
    # Cores
    mais_de_uma_cor = models.BooleanField(default=False)
    cores = models.CharField(max_length=100)
    
    
    # Foto do animal
    foto = models.ImageField(upload_to='pets_fotos/', null=True, blank=True)
    
    
    # Localização - usar API do ViaCEP
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    

    # Exibiçao do nome ou espécie
    def __str__(self):
        
        if self.nome:
            return f"{self.nome} ({self.get_status_display()})"
        return f"{self.get_especie_display()} sem nome ({self.get_status_display()})"