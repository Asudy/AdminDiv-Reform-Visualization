from random import randint

def _generate_dict(lower: int, upper: int):
    yearList = list(map(str, range(1978, 2021)))
    randList = [randint(lower, upper) for _ in range(len(yearList))]
    ret = dict()
    for k, v in zip(yearList, randList):
        ret.update({k: v})
    return ret
    

def t_GetStatistics():
    statistics_return_dict = {
        '地级市': {
            '撤地设市': _generate_dict(0, 15),
            '地市合并': _generate_dict(0, 15),
            '县市升格': _generate_dict(0, 15),
            '切块设市': _generate_dict(0, 15),
            '总计': _generate_dict(16, 30)
        },
        '市辖区': {
            'xx模式': _generate_dict(0, 15),
            'yy模式': _generate_dict(0, 15),
            'zz模式': _generate_dict(0, 15),
            '总计':   _generate_dict(16, 30)
        },
        '县级市': {
            '撤县设市': _generate_dict(0, 15),
            '切块设市': _generate_dict(0, 15),
            '降级':     _generate_dict(0, 15),
            '总计':     _generate_dict(16, 30)
        }
    }
    return statistics_return_dict


if __name__ == '__main__':
    print(t_GetStatistics())