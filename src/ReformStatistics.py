import streamlit as st
import altair as alt
from ReadExcel import GetStatistics


levels = ['地级市', '县级市', '市辖区']


def _reformDict(d: dict) -> dict:
    yearList = list(map(str, range(1978, 2021)))

    for v in d.values():
        v['年份'] = yearList
        for kk, vv in v.items():
            v[kk] = vv[:len(yearList)]

    # for v in d.values():
    #     for kk, vv in v.items():    # kk: str, vv: list[int]
    #         dd = dict()
    #         for kkk, vvv in zip(yearList, vv[:len(yearList)]):
    #             dd.update({kkk: vvv})
    #         v[kk] = dd
    return d


def DisplayStatistics():
    # Set sidebar
    st.sidebar.header('视图')
    view = st.sidebar.radio('', ['按省份统计', '按年份统计'], index=1)
    st.sidebar.header('查询行政区划级别')
    level = st.sidebar.radio('', levels)
    
    st.markdown("<center> <h2> 行政区变化统计信息 </h2> </center>", unsafe_allow_html=True)
    stats = GetStatistics()
    _reformDict(stats)
    # st.write(t_dic)
    # st.write(_reformDict(t_dic))
    
    st.header(level)

    modes = list(stats[level].keys())
    cols = st.beta_columns(len(modes))

    if view == '按年份统计':
        show_dict = dict()

        for i in range(len(cols)):
            key = modes[i]
            with cols[i]:
                if st.checkbox(key, key=level + '_' + key):
                    show_dict[key] = stats[level][key]
        
        # st.write(show_dict)
        if len(show_dict):
            st.line_chart(show_dict, height=200, use_container_width=True)
            st.area_chart(show_dict, height=200, use_container_width=True)
            st.bar_chart(show_dict, height=200, use_container_width=True)
    else:   # Stat by province
        mode = st.sidebar.selectbox('选择行政区划变化模式', modes)
        st.image(f"img/stat/{level}/{mode}.png", caption=f'省份统计图：{level}，{mode}')