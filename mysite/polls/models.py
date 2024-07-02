from django.db import models

# Create your models here.
class TB_1(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()

    MY_CHOICES = [
        ('0', 'Android'),
        ('1', 'Apple')
    ]
    device_list = models.CharField(
        max_length = 1,
        choices = MY_CHOICES,
        default = '0'
    )
    _time = models.DateTimeField(auto_now_add=True)

    # 後台會顯示name的名稱
    def __str__(self):
        return self.name
    
    # 設定後台顯示名稱
    class Meta:
        ordering = ['_time']
        verbose_name = '用戶資料庫'
        verbose_name_plural = '用戶資料庫'  # 複數