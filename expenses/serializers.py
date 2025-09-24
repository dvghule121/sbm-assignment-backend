from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Expense
        fields = ['id', 'user', 'title', 'amount', 'category', 'date', 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
    
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than 0")
        return value

class ExpenseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category', 'date', 'description']
    
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than 0")
        return value

class ExpenseSummarySerializer(serializers.Serializer):
    category = serializers.CharField()
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    count = serializers.IntegerField()