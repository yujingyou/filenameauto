from name_generate.models import Project, Scheme, Module, TechniFileName, PlanFileName, ProjectFlieClass


class TechnicalFileNameAuto:
    def __init__(self, project, name, projectflieclass, scheme=None, module=None, date=None, author=None, number=None,
                 version=None):  # 构造函数，类接收外部传入参数全靠构造函数
        self.projectflieclass = projectflieclass
        self.project = project
        self.scheme = scheme
        self.module = module
        self.name = name
        self.date = date
        self.author = author
        self.number = number
        self.version = version

    def getFileName(self):
        result = ''
        project = Project.objects.get(pk=self.project)
        result += project.name

        if self.scheme is not None and self.scheme is not '':
            result += '-' + Scheme.objects.get(pk=self.scheme).name
        else:
            self.scheme = None

        result += '-' + ProjectFlieClass.objects.get(pk=self.projectflieclass).code

        if self.module is not None and self.module is not '':
            result += '.' + Module.objects.get(pk=self.module).name
        else:
            self.module = None

        fileObj = TechniFileName.objects.filter \
            (project=self.project, scheme=self.scheme, module=self.module,
             projectflieclass=self.projectflieclass).order_by('-number').first()
        if fileObj is not None and fileObj is not '':
            self.number = fileObj.number + 1
        else:
            self.number = 1

        print('TechniFileName num %d' % self.number)
        result += '-' + '%02d' % self.number
        isRelease = self.version

        fileObj = TechniFileName.objects.filter \
            (project=self.project, projectflieclass=self.projectflieclass, scheme=self.scheme, module=self.module,
             name=self.name).order_by('-version').first()

        if fileObj is not None and fileObj is not '':
            s1 = list(fileObj.version)
            if isRelease == 'debug':
                s1[3] = str(int(s1[3]) + 1)
            elif isRelease == 'release':
                s1[1] = str(int(s1[1]) + 1)
                s1[3] = '0'
            self.version = ''.join(s1)
        else:
            self.version = 'v0.1'

        result += '-' + self.version
        result += ' ' + self.name

        # if self.date is not None and self.date is not '':
        #     result += '-' + self.date
        # else:
        #     self.date = None
        # if self.author is not None and self.author is not '':
        #     result += '-' + self.author
        # else:
        #     self.author = None
        print(result)
        return result


class PlanFileNameAuto:
    def __init__(self, project, name, projectflieclass, phase=None, date=None, author=None, number=None,
                 ):  # 构造函数，类接收外部传入参数全靠构造函数
        self.projectflieclass = projectflieclass
        self.project = project
        self.phase = phase
        self.name = name
        self.date = date
        self.author = author
        self.number = number

    def getFileName(self):
        result = ''

        project = Project.objects.get(pk=self.project)
        result += project.name

        result += '-' + ProjectFlieClass.objects.get(pk=self.projectflieclass).code

        if self.phase is not None and self.phase is not '':
            result += '.' + self.phase
        else:
            self.phase = None
        if self.date is not None and self.date is not '':
            temp = self.date
            temp = temp.replace('-', '')
            result += '-' + temp
        else:
            self.date = None

        fileObj = PlanFileName.objects.filter \
            (project=self.project, projectflieclass=self.projectflieclass, name=self.name, date=self.date).order_by(
            '-number').first()

        if fileObj is not None and fileObj is not '':
            self.number = fileObj.number + 1
        else:
            self.number = 1

        print('PlanFileName num %d' % self.number)
        result += '-' + '%02d' % self.number

        result += ' ' + self.name

        # if self.date is not None and self.date is not '':
        #     result += '-' + self.date
        # else:
        #     self.date = None
        # if self.author is not None and self.author is not '':
        #     result += '-' + self.author
        # else:
        #     self.author = None
        print(result)
        return result


class RecordFileNameAuto:
    def __init__(self, project, name, projectflieclass, date=None, author=None, number=None
                 ):  # 构造函数，类接收外部传入参数全靠构造函数
        self.projectflieclass = projectflieclass
        self.project = project
        self.name = name
        self.date = date
        self.author = author
        self.number = number

    def getFileName(self):
        result = ''

        project = Project.objects.get(pk=self.project)
        result += project.name

        result += '-' + ProjectFlieClass.objects.get(pk=self.projectflieclass).code

        if self.date is not None and self.date is not '':
            temp = self.date
            temp = temp.replace('-', '')
            result += '-' + temp
        else:
            self.date = None

        fileObj = PlanFileName.objects.filter \
            (project=self.project, projectflieclass=self.projectflieclass, name=self.name, date=self.date).order_by(
            '-number').first()

        if fileObj is not None and fileObj is not '':
            self.number = fileObj.number + 1
        else:
            self.number = 1

        print('PlanFileName num %d' % self.number)
        result += '-' + '%02d' % self.number

        result += ' ' + self.name

        # if self.date is not None and self.date is not '':
        #     result += '-' + self.date
        # else:
        #     self.date = None
        # if self.author is not None and self.author is not '':
        #     result += '-' + self.author
        # else:
        #     self.author = None
        print(result)
        return result
