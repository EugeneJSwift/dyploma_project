from django.db import models

# Create your models here.

class Catigories(models.Model):
    name  = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug  = models.SlugField(max_length=200, unique=True,blank=True, null=True, verbose_name='URL')


    class Meta:
        db_table:str = 'category'
        verbose_name: str = 'Категорию'
        verbose_name_plural: str = 'Категории'
        
    def __str__(self)-> None:
        return self.name

class Products(models.Model):
    name  = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug  = models.SlugField(max_length=200, unique=True,blank=True, null=True, verbose_name='URL')
    descriprion = models.TextField(blank=True,null= True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images',blank=True,null= True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в процентах')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Catigories, on_delete=models.CASCADE, verbose_name='Категория')
    
    
    class Meta:
        db_table: str = 'product'
        verbose_name: str = 'Продукт'
        verbose_name_plural: str = "Продукты"
        
    def __str__(self)-> None:
        return self.name
    
    def display_id (self):
        return f" {self.id:05}"
    
    def sell_price(self):
        if self.discount:
            return round (self.price - (self.price * self.discount) / 100, 2)
        return self.price
        
        
    