import pandas as pd

# dict format:
# 'description':[('description','xxxxxxxxxxxx')]
# '地级市':[('xxxx','yyyyyyyyyyyyyyyyy'),('xxxx','zzzzzzzzzzzzzzzzzzz')]
# '县级市':

province = {'北京': 0, '天津': 1, '河北': 2, '浙江': 3, '福建': 4, '上海': 5, '江苏': 6, '山东': 7, '广东': 8, '海南': 9, '山西': 10, '安徽': 11, '江西': 12, '河南': 13, '湖北': 14, '湖南': 15,
            '内蒙古': 16, '广西': 17, '重庆': 18, '四川': 19, '贵州': 20, '云南': 21, '西藏': 22, '陕西': 23, '甘肃': 24, '青海': 25, '宁夏': 26, '新疆': 27, '辽宁': 28, '吉林': 29, '黑龙江': 30}
# the dic of province name and its index

# input year, province name and type

def getFrequency():
    d = pd.read_excel(r"data/statistics/地级市.xlsx", sheet_name="按年份分", index_col=0,
                           header=0, keep_default_na=False)
    #print("输出列标题",d.columns.values)
    dict1 = dict()
    for type in d.columns.values:
        listNum = []
        dict1[type] = listNum
    for type in d.columns.values:
        for i in d.index.values:
            if(d.loc[i,type]):
                dict1[type].append(d.loc[i,type])
            else:
                dict1[type].append(0)

    d = pd.read_excel(r"data/statistics/市辖区.xlsx", sheet_name="按年份分", index_col=0,
                           header=0, keep_default_na=False)
    #print("输出列标题",d.columns.values)
    dict2 = dict()
    for type in d.columns.values:
        listNum = []
        dict2[type] = listNum
    for type in d.columns.values:
        for i in d.index.values:
            if(d.loc[i,type]):
                dict2[type].append(d.loc[i,type])
            else:
                dict2[type].append(0)

    d = pd.read_excel(r"data/statistics/县级市.xlsx", sheet_name="按年份分", index_col=0,
                           header=0, keep_default_na=False)
    #print("输出列标题",d.columns.values)
    dict3 = dict()
    for type in d.columns.values:
        listNum = []
        dict3[type] = listNum
    for type in d.columns.values:
        for i in d.index.values:
            if(d.loc[i,type]):
                dict3[type].append(d.loc[i,type])
            else:
                dict3[type].append(0)

    dictResult = dict()
    dictResult['地级市'] = dict1
    dictResult['市辖区'] = dict2
    dictResult['县级市'] = dict3
    #print(dictResult)
    return dictResult
    

def getdata(year, provincename, type=""):
    if(type == "县级市"):
        df = pd.read_excel(r"data/县级市.xlsx", index_col=0,
                           header=1, keep_default_na=False)    # 即指定第一列为行索引,第二行为列索引
    elif(type == "地级市" or type == ""):
        df = pd.read_excel(r"data/地级市.xlsx", index_col=0,
                           header=1, keep_default_na=False)    # 即指定第一列为行索引,第二行为列索引
    elif(type == "市辖区"):
        df = pd.read_excel(r"data/市辖区.xlsx", index_col=0,
                           header=1, keep_default_na=False)    # 即指定第一列为行索引,第二行为列索引

    # print(df)
    Dict = dict()
    data = df.iloc[year-1977, province[provincename]]
    # read data from excel 单元格
    # print(data)

    # read according to []
    index = 0
    first = -1
    second = -1
    for index in range(len(data)):
        if(data[index] == '[' or data[index] == '［'):
            last = index
            if(first < second and second < last):
                key = data[first:second]
                val = data[second+1:last]
                other = 'others'
                Tuple = (key, val)
                if index in Dict:
                    Dict[other].append(Tuple)
                    # Dict[key]+=val
                else:
                    Dict.setdefault(other, []).append(Tuple)
            elif(first == -1 and second == -1 and last != -1):
                key = 'description'
                val = data[0:last]
                Tuple = (key, val)
                Dict.setdefault(key, []).append(Tuple)
            first = index+1
        elif(data[index] == ']' or data[index] == '］'):
            second = index

    if(first < second and second < index):
        key = data[first:second]
        val = data[second+1:index+1]
        other = 'others'
        Tuple = (key, val)
        if key in Dict:
            Dict[other].append(Tuple)
        else:
            Dict.setdefault(other, []).append(Tuple)

    if(Dict):
        return Dict
    else:
        key = 'description'
        val = data[0:index+1]
        Tuple = (key, val)
        Dict.setdefault(key, []).append(Tuple)
        # print(Dict)

    return Dict


def ReadExcel(year, provincename):
    Dict = dict()
    dic1 = getdata(year, provincename, '地级市')
    dic2 = getdata(year, provincename, '县级市')
    dic3 = getdata(year, provincename, '市辖区')
    key = 'description'
    if(key in dic1):
        Dict[key] = dic1[key]
    elif(key in dic2):
        Dict[key] = dic2[key]
    elif(key in dic3):
        Dict[key] = dic3[key]

    other = 'others'

    if(other in dic1):
        Dict['地级市'] = dic1[other]

    if(other in dic2):
        Dict['县级市'] = dic2[other]

    if(other in dic3):
        Dict['市辖区'] = dic3[other]

    # print(Dict)
    return Dict


# main

#dic = dict()
#dic = ReadExcel(1989,'青海')
#print(dic)
# get data use the year and province name


#getFrequency()
