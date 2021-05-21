import pandas as pd

#dict format:
#'description':'xxxxxxxxxxxx'
#'县市升格':'yyyyyyyyyyyy'
#'撤县立市':'zzzzzzzzzzzz'

province={'北京':0 , '天津':1 , '河北':2 , '浙江':3	, '福建':4 , '上海':5 , '江苏':6 , '山东':7 , '广东':8 , '海南':9 ,	'山西':10 , '安徽':11 , '江西':12 ,	'河南':13 ,	'湖北':14,	'湖南':15,	'内蒙古':16,	'广西':17,	'重庆':18,	'四川':19,	'贵州':20,	'云南':21,	'西藏':22,	'陕西':23,	'甘肃':24,	'青海':25,	'宁夏':26,	'新疆':27,	'辽宁':28,	'吉林':29, '黑龙江':30}
#the dic of province name and its index


#input year and province name
def getdata(year,provincename):
    df = pd.read_excel(r"data\city.xlsx",index_col=0,header=1)	# 即指定第一列为行索引,第二行为列索引
    #print(df)
    Dict=dict()
    data = df.iloc[year-1977, province[provincename]]
    #read data from excel 单元格
    #print(data)
    
    #read according to []
    first=-1
    second=-1
    for index in range(len(data)):
        if(data[index]=='[' or data[index]=='［'):
            last=index
            if(first<second and second<last):
                key=data[first:second]
                val=data[second+1:last]
                if key in Dict: 
                    #D[key]+=';'
                    Dict[key]+=val
                else: Dict[key]=val
            elif(first==-1 and second==-1 and last!=-1):
                key='description'
                val=data[0:last]
                Dict[key]=val
            first=index+1
        elif(data[index]==']' or data[index]=='］'):
            second=index

    if(first<second and second<index):
        key=data[first:second]
        val=data[second+1:index+1]
        if key in Dict: 
            #D[key]+=';'
            Dict[key]+=val
        else: Dict[key]=val



    if(Dict): print(Dict)
    else:
        key='description'
        val=data[0:index+1]
        Dict[key]=val
        print(Dict)

    return Dict


#main

dic=dict()
dic=getdata(1979,'广东')
#get data use the year and province name