from django.db import models

# Create your models here.


class box(models.Model):
    box_name = models.CharField(max_length = 10)
    colors = (('red','red'),
              ('blu','blue'),
              ('gre','green'),
              ('yel','yellow')
    )
    box_color = models.CharField(max_length=3,choices=colors,default='red')
    mass = models.DecimalField(max_digits=5,decimal_places=2)
    
    def __str__(self):
        return self.box_name

