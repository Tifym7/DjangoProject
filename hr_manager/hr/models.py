from django.db import models

class MyModel(models.Model):
    class Meta:
        abstract =  True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    class Meta:
        db_table = 'hr_user'
    name = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, default="hei")

    def __str__(self):
        return f'{type(self)} {self.id}'

class Note(models.Model):
    class Meta:
        db_table = 'hr_notes'
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    summary = models.CharField(max_length=255, default="Dear Diary")
    content = models.TextField(default="")

    def __str__(self):
        return f'{type(self)} {self.id}'