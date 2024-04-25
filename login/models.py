from django.db import models

# Create your models here.
class LoginPageImage(models.Model):
    """ Proflow images """

    def get_login_page_path(self, filename, *args, **kwargs):
        return "login_images/%s" % (filename)

    name = models.CharField(verbose_name="Title", max_length=100,
                            blank=True, null=True)
    subtitle = models.TextField(verbose_name="Notes", max_length=100,
                            blank=True, null=True)
    image = models.ImageField(upload_to=get_login_page_path,
                              blank=True, null=True)
    is_active = models.BooleanField(default=True, help_text="Is Active")

    def __str__(self):
        return "%s" % self.name
    
class LogoPolicy(models.Model):
    
    policy = models.TextField(blank=True, null=True, verbose_name="Policy")
    company_logo = models.ImageField(upload_to='login_images/', max_length=200,
                          blank=True, null=True,)
