from django.db import models
from django.contrib.auth.models import User


class CaseFile(models.Model):

    case_id = models.ForeignKey("Case", on_delete=models.CASCADE,
                            related_name="case_id",default="")
    attachments = models.FileField(upload_to="calender_attachments/",default=True)


# Create your models here.
class Case(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="addcase")
    alien_number = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(null=True, blank=True, max_length=50)
    email =  models.EmailField(blank=True, null=True)
    Address = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=200,blank=True, null=True)
    zipcode = models.CharField(max_length=200,blank=True, null=True)
    country = models.CharField(max_length=200,blank=True, null=True)
    type_of_case = models.CharField(max_length=200)
    i_589_filed = models.BooleanField(default=False, verbose_name = "I 59 filed ?")
    erop = models.BooleanField(default=False, verbose_name = "Erop ?")
    e_28_filed = models.BooleanField(default=False, verbose_name = "E28 filed ?")
    biometrics_filed = models.BooleanField(default=False, verbose_name = "Biometrics filed?")
    foia_submitted = models.BooleanField(default=False, verbose_name = "Foia submitted?")
    foia_uploaded = models.BooleanField(default=False, verbose_name = "Foia uploaded?")
    work_permit_applied = models.BooleanField(default=False, verbose_name = "Work permit applied?")
    hearing_date = models.DateTimeField(verbose_name="Hearing Date", auto_now_add=True)
    hearing_location = models.CharField(max_length=200)
    total_billing_amount = models.CharField(max_length=200)
    amount_paid = models.CharField(max_length=200)
    date = models.DateTimeField(null=True, blank=True)
    # attach = models.ManyToManyField(CaseFile)


    def __str__(self):
        return self.first_name





    

