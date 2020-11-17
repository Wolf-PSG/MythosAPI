from django.db import models

# Create your models here.

class Entity(models.Model):

  # class roleOptions(models.TextChoices):
  #   GOD = 'GD', _('God')
  #   DEMON = 'DM', _('Demon')
  #   HERO = 'HR', _('Hero')
  #   MONSTER = 'MN', _('Monster')
  
  # class originOptions(models.TextChoices):
  #   GREEK = 'GK', _('Greek')
  #   JAPANESE = 'JP', _('Japanese')
  #   SLAVIC = 'SV', _('Slavic')
  #   NORSE = 'NR', _('Norse')
  
  roleOptions = (
    ('GD', 'God'),
    ('DM', 'Demon'),
    ('HR', 'Hero'),
    ('MN', 'Monster'),
  )

  originOptions = (
    ('GK', 'Greek'),
    ('JP', 'Japanese'),
    ('SV', 'Slavic'),
    ('NR', 'Norse'),
  )
  
  entityID = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20)
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  parents = models.CharField(max_length=20) 
  origin = models.CharField(max_length=2, choices=originOptions)
  role = models.CharField(max_length=2, choices=roleOptions)
  greatest_Feats = models.CharField(max_length=200)
  image = models.ImageField(upload_to='photos/%Y/%m/%d/')

  def __str__(self):
    return self.name

  class Meta:
    ordering = ("origin","name")
