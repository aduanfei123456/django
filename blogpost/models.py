from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink
import datetime
from django.utils import timezone
# Create your models here.
class Blogpost(models.Model):
    title=models.CharField(max_length=100,unique=True)
    author=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    body=models.TextField()
    posted=models.DateField(db_index=True,auto_now_add=True)
    #return stringpattern of the class
    def __unicode__(self):
        return'%s'%self.title
    @permalink
    def get_absolute_url(self):
        return ('view_blog_post',None,{'slug':self.slug})

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    def __unicode__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)
#Cascade deletes. Django emulates the behavior of the SQL
# constraint ON DELETE CASCADE and also deletes the object containing the ForeignKey.
class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text

