from django.shortcuts import render
from django.db.models import Sum, Count
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Expense
from .serializers import ExpenseSerializer, ExpenseCreateSerializer, ExpenseSummarySerializer

# Create your views here.

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Return expenses only for the authenticated user"""
        return Expense.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """Automatically set the user when creating an expense"""
        serializer.save(user=self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ExpenseCreateSerializer
        return ExpenseSerializer
    
    @action(detail=False, methods=['get'])
    def summary(self, request):
        """Get expense summary by category for the authenticated user"""
        summary_data = self.get_queryset().values('category').annotate(
            total_amount=Sum('amount'),
            count=Count('id')
        ).order_by('-total_amount')
        
        serializer = ExpenseSummarySerializer(summary_data, many=True)
        return Response(serializer.data)

def reports_view(request):
    """Render the reports page with Chart.js visualization"""
    return render(request, 'expenses/reports.html')
