from django.db import models




types = [('Computer Engineering','Computer Engineering'),('Instructor','Instructor')]
types1 = [('1st Year','1st Year'),('2nd Year','2nd Year'),('3rd Year','3rd Year'),('4th Year','4th Year')]
types2 = [('Male','Male'),('Female','Female')]
class Profile(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    date = models.DateField()
    phone = models.BigIntegerField()
    email = models.EmailField()
    gender = models.CharField(choices=types2,max_length=20,null=True,blank=False,default='')
    year = models.CharField(choices=types1,max_length=20,null=True,blank=False,default='')
    Course = models.CharField(choices=types,max_length=20,null=True,blank=False,default='')
    present = models.BooleanField(default=False)
    image = models.ImageField()
    updated = models.DateTimeField(auto_now=True)
    time = models.TimeField()
    
    def __str__(self):
        return self.first_name +' '+self.last_name


class LastFace(models.Model):
    last_face = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.last_face

