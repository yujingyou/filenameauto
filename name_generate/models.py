from django.db import models


# Create your models here.
class FlieClass(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ProjectClass(models.Model):
    name = models.CharField(max_length=30)
    flieclass = models.ForeignKey(FlieClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=30)
    projectclass = models.ForeignKey(ProjectClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Scheme(models.Model):
    name = models.CharField(max_length=30)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=30)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TechniFileName(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    scheme = models.ForeignKey(Scheme, on_delete=models.SET_NULL, null=True)
    module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30)
    date = models.DateField(null=True, blank=True)
    author = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name
