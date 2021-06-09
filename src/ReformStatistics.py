import streamlit as st
from ReadExcel import ReadExcel
from GetProvinceNamesByYear import GetProvinceNamesByYear

from t_GetStatistics import t_GetStatistics

def DisplayStatistics():
    st.markdown("<center> <h2> 行政区变化统计信息 </h2> </center>", unsafe_allow_html=True)
    t_dic = t_GetStatistics()
    # st.write(t_dic)
    for mode in ['地级市', '县级市', '市辖区']:
        st.header(mode)
        st.area_chart(t_dic[mode], height=180, use_container_width=True)