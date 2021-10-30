from django.db import models



class notesdb(models.Model):
    notesNo =models.IntegerField(primary_key=True,blank=False)
    notesdata =models.CharField(blank=False,max_length=500)
    notesName = models.CharField(blank=False,max_length=30)


    def __str__(self):
        return self.notesName