from django.db import models
from django.core.validators import RegexValidator


# Represents a team member in app
class TeamMember(models.Model):

    # Define role choices
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('regular', 'Regular'),
    ]

    # Define fields for first name, last name, email, phone number, and role for each team member
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
    max_length=17,
    blank=True,
    null=True
  )
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    # Returns string with full name
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    # Validates the model
    def save(self, *args, **kwargs):
        self.full_clean() 
        super().save(*args, **kwargs)

