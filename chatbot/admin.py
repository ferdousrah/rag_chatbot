# chatbot/admin.py
from django.contrib import admin
from .models import Product, KnowledgeBase

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock_quantity')
    search_fields = ('name', 'category')
    list_filter = ('category',)
    ordering = ('name',)
    readonly_fields = ('id',)
    fields = (
        'id', 
        'name', 
        'description', 
        'price', 
        'category', 
        'stock_quantity', 
        'specifications', 
        'image'
    )

@admin.register(KnowledgeBase)
class KnowledgeBaseAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question', 'answer')
    ordering = ('question',)
    readonly_fields = ('id',)
    fields = ('id', 'question', 'answer')
