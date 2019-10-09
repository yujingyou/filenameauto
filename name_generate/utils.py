from idlelib.idle_test.test_browser import module

import xlrd, datetime

from name_generate.models import TechniFileName, PlanFileName, RecordFileName, ProjectFlieClass, Project, Scheme, Module

tableHead = [u'文件名称', u'文件编号', u'制定日期', u'制定人', ]
TechniFileNameSqlList = []
PlanFileNameSqlList = []
RecordFileNameSqlList = []


def date(dates):  # 定义转化日期戳的函数,dates为日期戳
    delta = datetime.timedelta(days=dates)
    today = datetime.datetime.strptime('1899-12-30', '%Y-%m-%d') + delta  # 将1899-12-30转化为可以计算的时间格式并加上要转化的日期戳
    return datetime.datetime.strftime(today, '%Y-%m-%d')  # 制定输出日期的格式


def getColnameindex(table):
    for i in range(0, table.nrows):
        for item in table.row_values(i):
            # print(item)
            if tableHead[1] == item:
                return i
    return -1


def parseTechniFileName(item):
    print('parseRecordFileName')
    fileCode = item.get(tableHead[1], None)

    listConde = fileCode.split('-')
    filedict = {}
    pos = 0
    filedict['project'] = Project.objects.get(name=listConde[pos])
    pos += 1
    if len(listConde) == 5:  # 项目名称-方案名-类别代号.模块名-序号-版本 含有方案名则长度为5
        filedict['scheme'] = Scheme.objects.filter(project=filedict['project'], name=listConde[pos]).first()
        pos += 1
    else:
        filedict['scheme'] = None

    codeModule = listConde[pos].split('.')
    filedict['projectflieclass'] = ProjectFlieClass.objects.get(code=codeModule[0])
    if len(codeModule) == 2:  # 类别代号.模块名 含有模块名则长度为2
        filedict['module'] = Module.objects.filter(project=filedict['project'], name=codeModule[1]).first()
    else:
        filedict['module'] = None
    pos += 1
    filedict['number'] = int(listConde[pos])
    pos += 1
    filedict['version'] = listConde[pos]
    filedict['result'] = fileCode
    filedict['date'] = date(item.get(tableHead[2], None))
    filedict['author'] = item.get(tableHead[3], None)
    filedict['name'] = item.get(tableHead[0], None)
    print(filedict)

    obj = TechniFileName(project=filedict['project'], scheme=filedict['scheme'], module=filedict['module'],
                         projectflieclass=filedict['projectflieclass'], number=filedict['number'],
                         version=filedict['version'], result=filedict['result'], date=filedict['date'],
                         author=filedict['author'], name=filedict['name'])
    TechniFileNameSqlList.append(obj)


def parsePlanFileName(item):
    print('parseRecordFileName')
    fileCode = item.get(tableHead[1], None)

    listConde = fileCode.split('-')  # 项目名称-类别代号.阶段代号-日期-序号
    filedict = {}
    pos = 0
    filedict['project'] = Project.objects.get(name=listConde[pos])
    pos += 1

    codePhase = listConde[pos].split('.')
    filedict['projectflieclass'] = ProjectFlieClass.objects.get(code=codePhase[0])
    if len(codePhase) == 2:  # 类别代号.阶段代号 含有模块名则长度为2
        filedict['phase'] = codePhase[1]
    else:
        filedict['phase'] = None
    pos += 2  # 跳过日期
    if len(listConde) > pos:
        filedict['number'] = int(listConde[pos])
    else:
        filedict['number'] = 1

    filedict['result'] = fileCode
    filedict['date'] = date(item.get(tableHead[2], None))
    filedict['author'] = item.get(tableHead[3], None)
    filedict['name'] = item.get(tableHead[0], None)
    print(filedict)
    obj = PlanFileName(project=filedict['project'], phase=filedict['phase'],
                       projectflieclass=filedict['projectflieclass'], number=filedict['number'],
                       result=filedict['result'], date=filedict['date'],
                       author=filedict['author'], name=filedict['name'])
    PlanFileNameSqlList.append(obj)


def parseRecordFileName(item):
    print('parseRecordFileName')
    fileCode = item.get(tableHead[1], None)

    listConde = fileCode.split('-')  # 项目名称-类别代号-日期-序号
    filedict = {}
    pos = 0
    filedict['project'] = Project.objects.get(name=listConde[pos])
    pos += 1

    filedict['projectflieclass'] = ProjectFlieClass.objects.get(code=listConde[pos])

    pos += 2

    if len(listConde) > pos:
        filedict['number'] = int(listConde[pos])
    else:
        filedict['number'] = 1

    filedict['result'] = fileCode
    filedict['date'] = date(item.get(tableHead[2], None))
    filedict['author'] = item.get(tableHead[3], None)
    filedict['name'] = item.get(tableHead[0], None)
    print(filedict)
    obj = RecordFileName(project=filedict['project'],
                         projectflieclass=filedict['projectflieclass'], number=filedict['number'],
                         result=filedict['result'], date=filedict['date'],
                         author=filedict['author'], name=filedict['name'])
    RecordFileNameSqlList.append(obj)


def parseItem(item):
    fileCode = item.get(tableHead[1], None)
    if fileCode is None:
        return
    if TechniFileName.objects.filter(result=fileCode).first() is not None:
        return
    if PlanFileName.objects.filter(result=fileCode).first() is not None:
        return
    if RecordFileName.objects.filter(result=fileCode).first() is not None:
        return

    listConde = fileCode.split('-')
    print(listConde)

    for i in range(1, 3):
        for t in listConde[i].split('.'):
            pfClass = ProjectFlieClass.objects.filter(code=t).first()
            if pfClass is None:
                continue
            else:
                if pfClass.flieclass.name == u'技术类文件':
                    parseTechniFileName(item)
                elif pfClass.flieclass.name == u'计划类文件':
                    parsePlanFileName(item)
                elif pfClass.flieclass.name == u'记录类文件':
                    parseRecordFileName(item)


def ImportDatabase(filename):
    colnameindex = 3  # 表头行位置
    by_index = 1
    # print(filename)
    data = xlrd.open_workbook(filename)
    listd = []
    for table in data.sheets():
        nrows = table.nrows  # 行数
        ncols = table.ncols  # 列数
        colnameindex = getColnameindex(table)
        if colnameindex == -1:
            continue
        colnames = table.row_values(colnameindex)  # 某一行数据
        for rownum in range(colnameindex + 1, nrows):
            row = table.row_values(rownum)
            if row:
                app = {}
                for i in range(len(colnames)):
                    app[colnames[i]] = row[i]
                    # print(row[i])
                # list.append(app)
                listd.append(app)
    for item in listd:
        parseItem(item)
    TechniFileName.objects.bulk_create(TechniFileNameSqlList)
    PlanFileName.objects.bulk_create(PlanFileNameSqlList)
    RecordFileName.objects.bulk_create(RecordFileNameSqlList)