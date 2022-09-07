from django.db import models
# Create your models here.
class MetaTag(models.Model):
    url = models.TextField(verbose_name='URL Path',help_text='Example: /about-us')
    title = models.CharField(verbose_name='Meta Title',max_length=400,null=True,blank=True,help_text='Title Tag')
    meta_description = models.TextField(verbose_name='Meta Description',help_text='Meta Description',null=True,blank=True)
    meta_keywords = models.TextField(verbose_name='Meta Keywords',help_text='Meta Keywords',null=True,blank=True)
    meta_canonical = models.URLField(verbose_name='Canonical',null=True,blank=True)
    meta_robots = models.CharField(verbose_name='meta_robots',null=True,blank=True,max_length=400)
    og_description = models.TextField(verbose_name='Og Description',null=True,blank=True)
    og_image = models.ImageField(verbose_name='Og Image',null=True,blank=True,)
    og_url = models.URLField(verbose_name='Og url',null=True,blank=True)
    og_site_name = models.CharField(verbose_name='Og Site name',null=True,blank=True,max_length=400)
    og_title = models.CharField(verbose_name='Og Title',max_length=400,null=True,blank=True)
    
    def __str__(self):
        return self.url

    class Meta:
        verbose_name = "Meta Tag"
        verbose_name_plural = "Meta Tags"


class CustomMetaTag(models.Model):
    TAG_NAME = (('name','name'),('property','property'),)
    status = models.CharField(verbose_name='status',choices=TAG_NAME,max_length=400,default=TAG_NAME[0])
    seo = models.ForeignKey(MetaTag,on_delete=models.SET_NULL,null=True,related_name='custom_meta')
    name = models.CharField(verbose_name='Meta Property / Meta Name',max_length=400,help_text='<meta name="" content="" />')

    content = models.TextField(verbose_name='Meta Content',max_length=400,help_text='<meta name="" content="" />')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Custom Meta Tag'
        verbose_name_plural = 'Custom Meta Tags'

class Schema(models.Model):
    schema = models.JSONField(verbose_name='Schema',null=True)
    url = models.TextField(verbose_name='URL Path',help_text='Example: /about-us')

    def __str__(self):
        return  self.url
    
    
    class Meta:
        verbose_name = 'Schema'
        verbose_name_plural = 'Schemas'
        


    