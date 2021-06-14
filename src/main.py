import streamlit as st
from SpecificReform import SelectAndDisplaySingleChange
from ReformStatistics import DisplayStatistics

if __name__ == "__main__":

    st.set_page_config(
        page_title = "中国行政区划改革",
        page_icon = '🇨🇳',
        initial_sidebar_state="expanded",
        # layout='wide'
    )

    ### Set title
    st.title("中国行政区划改革（1977~2020）")

    ### Set sidebar
    st.sidebar.header("功能")
    func = st.sidebar.radio('', [0, 1], 
        format_func=lambda x: ['具体行政区划变化查询', '行政区划变化统计信息查询'][x])

    if (func == 0):
        SelectAndDisplaySingleChange()
    else:
        DisplayStatistics()