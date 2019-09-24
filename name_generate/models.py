from django.db import models


# Create your models here.
class FlieClass(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ProjectClass(models.Model):
    name = models.CharField(max_length=30)
    flie_class = models.ForeignKey(FlieClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Project(models.Model):
    project_name = models.CharField(max_length=30)
    scheme_name = models.CharField(max_length=30)
    module_name = models.CharField(max_length=30)

    project_class = models.ForeignKey(ProjectClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FileName(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    file_name = models.CharField(max_length=30)
    date = models.DateField(null=True, blank=True)
    author = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name
