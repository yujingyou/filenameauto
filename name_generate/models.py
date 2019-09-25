from django.db import models


# Create your models here.
class FlieClass(models.Model):
    name = models.CharField(max_length=30, verbose_name="文件类型")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '文件分类'


class ProjectClass(models.Model):
    name = models.CharField(max_length=30, verbose_name="项目类型")
    flieclass = models.ForeignKey(FlieClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '项目分类'


class Project(models.Model):
    name = models.CharField(max_length=30, verbose_name="项目名")
    projectclass = models.ForeignKey(ProjectClass, on_delete=models.CASCADE, verbose_name="项目类型")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '项目列表'


class Scheme(models.Model):
    name = models.CharField(max_length=30, verbose_name="方案名")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="项目")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '方案表'


class Module(models.Model):
    name = models.CharField(max_length=30, verbose_name="模块名")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="项目")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '模块表'


class TechniFileName(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, verbose_name="项目")
    scheme = models.ForeignKey(Scheme, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="方案")
    module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="模块")
    name = models.CharField(max_length=30, verbose_name="文件名")
    date = models.DateField(null=True, blank=True, verbose_name="日期")
    author = models.CharField(max_length=30, null=True, blank=True, verbose_name="作者")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '技术类文件'
