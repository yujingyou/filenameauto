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
    code = models.CharField(max_length=30,null=True,blank=True, verbose_name="代号")
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
    number = models.IntegerField(null=True, blank=True, verbose_name="序号")
    version = models.CharField(max_length=30, null=True, blank=True, verbose_name="版本")
    result = models.CharField(max_length=50, null=False, verbose_name="文件全名")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '技术类文件'


phase_CHOICES = [
    ('01', '1'),
    ('02', '2'),
    ('03', '3'),
    ('04', '4'),
    ('05', '5'),
    ('06', '6'),
    ('07', '7'),
    ('08', '8'),
    ('09', '9'),
    ('10', '10'),
]


class PlanFileName(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, verbose_name="项目")
    phase = models.CharField(null=True, max_length=30, blank=True, verbose_name="阶段", choices=phase_CHOICES)
    date = models.DateField(null=True, blank=True, verbose_name="日期")
    name = models.CharField(max_length=30, verbose_name="文件名")
    author = models.CharField(max_length=30, null=True, blank=True, verbose_name="作者")
    number = models.IntegerField(null=True, blank=True, verbose_name="序号")
    result = models.CharField(max_length=60, null=True, verbose_name="文件全名")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '计划类文件'


class RecordFileName(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, verbose_name="项目")
    date = models.DateField(null=True, blank=True, verbose_name="日期")
    name = models.CharField(max_length=30, verbose_name="文件名")
    author = models.CharField(max_length=30, null=True, blank=True, verbose_name="作者")
    number = models.IntegerField(null=True, blank=True, verbose_name="序号")
    result = models.CharField(max_length=60, null=True, verbose_name="文件全名")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '记录类文件'
