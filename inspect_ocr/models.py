from django.db import models
from django.utils import timezone 
from django.urls import reverse_lazy
from inspectelements.settings import IMAGE_DIR

class Image(models.Model):
    """
    The Model -> Database blueprint for the Image object 
    The model saves ocr data, This can be used in analytics in the future
    as well as food_company+food_product can be used to circument the
    ocr process in the future
    """
    uid = models.AutoField(primary_key=True)
    food_product = models.CharField(
        max_length=100, help_text="Name of the food product", null=True
    )
    food_company = models.CharField(
        max_length=100, help_text="Food Manufactuing company", null=True
    )
    author = models.CharField(max_length=100, help_text="Name of the contributing entity", null=True)
    image = models.FileField(upload_to=IMAGE_DIR, null=True)
    add_date = models.DateField(
        default=timezone.now, help_text="Enter field published_date"
    )
    result = models.CharField(max_length=800, help_text="The Result of OCR", null=True)
    is_ocred = models.BooleanField(default=False)
    
    def __str__(self):
        return self.food_product + " " + self.food_company

    def get_excerpt(self):
        return self.result
