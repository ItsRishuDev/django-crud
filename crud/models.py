from django.db import models

# Create your models here.
class Empolyee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=250)
    emp_email = models.EmailField(max_length=254)
    emp_contact = models.IntegerField()
    emp_gender = models.CharField(max_length=10)
    emp_dob = models.DateField()

    def __str__(self):
        return self.emp_name
    