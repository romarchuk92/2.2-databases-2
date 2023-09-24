from django.db import models


class Tag(models.Model):

    name = models.CharField(max_length=30, verbose_name='Тег')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
   
    def __str__(self):
        return self.name



class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tag, through='ArticleScope', verbose_name='Тематики статьи', related_name='tag')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title



class ArticleScope(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE,verbose_name='Статья', related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Раздел', related_name='scopes')
    is_main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        verbose_name = 'Привязка'
        verbose_name_plural = 'Тематики статьи'