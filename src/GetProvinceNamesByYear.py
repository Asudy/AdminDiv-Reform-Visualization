def GetProvinceNamesByYear(year: int):
    list_Province = ['海南', '青海', '广东', '河北', '浙江', '福建', '江苏', '山东', '山西', '安徽', '江西', '河南',
                     '湖北', '湖南', '内蒙古', '广西', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '宁夏', '新疆', '辽宁', '吉林', '黑龙江']

    if(year >= 1988):
        return list_Province

    return list_Province[1:]


if __name__ == '__main__':
    try: 
        while True:
            y = int(input('Input year: '))
            list = GetProvinceNamesByYear(y)
            print(list)
    except KeyboardInterrupt:
        print('\nKeyboard interrupt received. Exiting.')