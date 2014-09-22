from django.db import models

class Translation(models.Model):
    title = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.title
    
class Book(models.Model):
    title = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.title

class Chapter(models.Model):
    book = models.ForeignKey(Book)
    number = models.IntegerField(default=0)
    title = models.CharField(max_length=128, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.title
  
  
class Verse(models.Model):
    translation = models.ForeignKey(Translation)
    book = models.ForeignKey(Book)
    chapter = models.ForeignKey(Chapter)
    number = models.IntegerField(default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.title
    
class TempVerse(models.Model):
    title = models.CharField(max_length=1024)
    description = models.TextField()
    
    def __unicode__(self):
        return self.title
