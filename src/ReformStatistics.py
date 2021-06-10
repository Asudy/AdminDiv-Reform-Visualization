import streamlit as st
from ReadExcel import ReadExcel
from GetProvinceNamesByYear import GetProvinceNamesByYear

from t_GetStatistics import t_GetStatistics

levels = ['地级市', '县级市', '市辖区']

def DisplayStatistics():
    st.markdown("<center> <h2> 行政区变化统计信息 </h2> </center>", unsafe_allow_html=True)
    t_dic = t_GetStatistics()
    # st.write(t_dic)
    for level in levels:
        st.header(level)
        show_dict = dict()

        modes = list(t_dic[level].keys())
        cols = st.beta_columns(len(modes))

        for i in range(len(cols)):
            key = modes[i]
            with cols[i]:
                if st.checkbox(key, key=level + '_' + key):
                    show_dict[key] = t_dic[level][key]
        
        # st.write(show_dict)
        if len(show_dict):
            st.line_chart(show_dict, height=200, use_container_width=True)
            st.area_chart(show_dict, height=200, use_container_width=True)