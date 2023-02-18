from django.db import models


class Img(models.Model):

    title = models.CharField(max_length=32, verbose_name='название')
    date = models.TimeField(auto_now_add=True, verbose_name='время')
    img = models.ImageField(upload_to='%Y/%m/%d/', verbose_name='картинка')

    class Meta:
        verbose_name='Картинка'
        verbose_name_plural='Картинки'
        ordering=['date']

class Comment(models.Model):
    author = models.CharField(max_length=64, verbose_name='автор')
    text = models.TextField(verbose_name='текст')
    date = models.TimeField(auto_now_add=True, verbose_name='дата')
    img = models.ForeignKey(Img, on_delete=models.CASCADE, verbose_name='картинка', related_name='comments')
    
    
    def __str__(self):
        return self.text[:32]
    
    class Meta:
        verbose_name='Комментарий'
        verbose_name_plural='Комментарии'
        ordering=['-date',]