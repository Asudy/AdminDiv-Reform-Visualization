from typing import Literal


def GetProvinceNamesByYear(year):
    list_Province = ['青海', '重庆', '海南', '广东', '北京市', '天津市', '上海市', '河北', '浙江', '福建', '江苏', '山东', '山西', '安徽',
                     '江西', '河南', '湖北', '湖南', '内蒙古', '广西', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '宁夏', '新疆', '辽宁', '吉林', '黑龙江']
    # if year >= 1980 and year <= 1987 or year == 1991:
    if year <= 1991:
        # 27
        return list_Province[3:]
    elif year <= 1996:
        # 28
        return list_Province[2:]
    else:
        return list_Province


list = GetProvinceNamesByYear(1991)
print(list)
