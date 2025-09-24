from django.contrib import admin
from .models import Expense

# Register your models here.

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'amount', 'category', 'date', 'created_at']
    list_filter = ['category', 'date', 'created_at', 'user']
    search_fields = ['title', 'description', 'user__username', 'user__email']
    ordering = ['-date', '-created_at']
    date_hierarchy = 'date'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'title', 'amount', 'category', 'date')
        }),
        ('Additional Details', {
            'fields': ('description',),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def get_queryset(self, request):
        """Superusers can see all expenses, staff users see only their own"""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
