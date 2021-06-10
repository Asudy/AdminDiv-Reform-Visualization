import streamlit as st
from SpecificReform import SelectAndDisplaySingleChange
from ReformStatistics import DisplayStatistics

if __name__ == "__main__":

    st.set_page_config(
        page_title = "中国行政区划改革",
        page_icon = '🇨🇳',
        initial_sidebar_state="expanded",
        layout='wide'
    )

    ### Set title
    st.title("🇨🇳中国行政区划改革（1978~2020）")

    ### Set sidebar
    st.sidebar.header("选择功能")
    func = st.sidebar.radio('', [0, 1], index=1, 
        format_func=lambda x: ['具体行政区划变化查询', '行政区划变化统计信息查询'][x])

    if (func == 0):
        SelectAndDisplaySingleChange()
    else:
        DisplayStatistics()
        # a, b = st.checkbox('a'), st.checkbox('b')
        # c = st.checkbox('c')
        # show_dic = {}
        # if a:
        #     show_dic['a'] = {}
        #     for k, v in zip(range(1978, 1984), [1,2,1,3,1,4]):
        #         show_dic['a'].update({k: v})
        #     st.write(show_dic)
        # if b:
        #     show_dic['b'] = [2,4,2,7,5,8]
        # if c:
        #     # show_dic['c'] = {1978: 1, 1979: 3, 1980: -2, 1981: 4, 1982: 2, 1983: 1}
        #     show_dic['c'] = {'1978': 1, '1979': 3, '1980': -2, '1981': 4, '1982': 2, '1983': 1}
        # st.area_chart(show_dic, use_container_width=True)