from django.db import models

# Create your models here.
class AiModel(models.Model):
    """Model definition for AiModel."""

    model_category = (
        (1,'text'),
        (2,'photos'),
        (3,'video'),
        (4,'nlp'),
        (5,'others'),
    )

    name = models.CharField(max_length=255,default='Model')
    summary = models.TextField()
    model_file = models.FileField(blank=True,upload_to='ai_models')
    category = models.IntegerField(choices=model_category,default=model_category[0][1])
    model_image = models.ImageField(blank=True,upload_to='ai_models/images')


    def __str__(self):
        return self.name
