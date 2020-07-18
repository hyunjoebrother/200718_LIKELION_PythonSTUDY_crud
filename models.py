from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True) 
    body=models.TextField() 


    def __str__(self):
        return self.title #제목 값으로 바꿔주는 함수는 model에 추가