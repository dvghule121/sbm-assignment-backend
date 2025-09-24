from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Entertainment', 'Entertainment'),
        ('Utilities', 'Utilities'),
        ('Healthcare', 'Healthcare'),
        ('Shopping', 'Shopping'),
        ('Education', 'Education'),
        ('Other', 'Other'),
    ]
    
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='expenses',
        help_text="User who created this expense"
    )
    title = models.CharField(max_length=200, help_text="Brief description of the expense")
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text="Amount in INR"
    )
    category = models.CharField(
        max_length=50, 
        choices=CATEGORY_CHOICES, 
        default='Other',
        help_text="Category of the expense"
    )
    date = models.DateField(help_text="Date when the expense occurred")
    description = models.TextField(
        blank=True, 
        null=True, 
        help_text="Additional details about the expense"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'
    
    def __str__(self):
        return f"{self.user.username} - {self.title} - ₹{self.amount} ({self.category})"
