from django.db import models
from account.models import User
from django_jalali.db import models as jmodels



class Article(models.Model):
    author = models.ForeignKey(User, null=True ,on_delete=models.SET_NULL, related_name='user')
    title = models.CharField(max_length=1200, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='blogs', verbose_name='عکس')
    created_at = jmodels.jDateField(auto_now_add=True, verbose_name='زمان ثبت')
    status = models.BooleanField(default=True, verbose_name='وضعیت')
    search = models.CharField(max_length=200, verbose_name='جستجو')




    def __str__(self):
        return self.title
    


    class Meta:
        ordering = ('-id',)
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'






