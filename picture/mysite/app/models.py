from django.db import models

# Create your models here.

class FileUpload(models.Model):
    picture_1 = models.FileField(upload_to='picture1')
    picture_2 = models.FileField(upload_to='picture2')

"""
@receiver(post_delete, sender=UploadFile)
def delete_file(sender, instance, **kwargs):
    instance.file.delete(False)
"""
