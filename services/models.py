from django.db import models




class Services(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    title2 = models.CharField(max_length=120, verbose_name='عنوان 2')
    image = models.ImageField(upload_to= 'services')
    description = models.TextField(verbose_name= 'توضیحات')
    search = models.CharField(max_length=120, verbose_name= 'جستجو')



    def __str__(self):
        return self. title
    



    class Meta:
        verbose_name = 'سرویس'
        verbose_name_plural = 'سرویس ها'




    