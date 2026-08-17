from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('Client', 'Client'),
        ('Proprietaire', 'Propriétaire'),
        ('Agent', 'Agent Immobilier'),
        ('Admin', 'Administrateur'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Client')

    def __str__(self):
        return f"{self.username} ({self.role})"

class Property(models.Model):
    TYPE_CHOICES = (
        ('Villa', 'Villa'),
        ('Appartement', 'Appartement'),
        ('Maison', 'Maison'),
        ('Studio', 'Studio'),
    )
    STATUS_CHOICES = (
        ('En attente', 'En attente'),
        ('Validé', 'Validé'),
        ('Rejeté', 'Rejeté'),
    )
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=255)
    property_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    area = models.DecimalField(max_digits=8, decimal_places=2) # in m2
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='En attente')
    image = models.ImageField(upload_to='properties/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Reservation(models.Model):
    ACTION_CHOICES = (
        ('Location', 'Location'),
        ('Achat', 'Achat'),
        ('Visite', 'Visite'),
    )
    
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reservations')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    action_type = models.CharField(max_length=20, choices=ACTION_CHOICES, default='Louer')
    date_period = models.CharField(max_length=100) # ex: "Mois de Septembre 2026" or date range
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action_type} - {self.property.title} par {self.client.username}"
        
class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='properties/')

    def __str__(self):
        return f"Image pour {self.property.title}"