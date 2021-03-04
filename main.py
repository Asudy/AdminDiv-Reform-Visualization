import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "中国行政区划改革"
)


Provinces = ['福建', '省份1', '省份2', '省份3', '省份4', '省份5']
Cities = ['厦门', '城市1', '城市2', '城市3', '城市4', '城市5']

st.title("中国行政区划改革")

st.sidebar.header("选择年份")
year = st.sidebar.slider("年份", min_value=1970, max_value=2020, value=2019)
st.sidebar.header("选择行政区")
view = st.sidebar.select_slider("视图", ["国", "省", "市"], value='市')
province, city = "", ""
if view == "省" or view == "市":
    province = st.sidebar.selectbox("省份", Provinces)
if view == "市":
    city = st.sidebar.selectbox("城市", Cities)


st.write("选中年份：{}；省份：{}；城市：{}".format(year, province, city))
st.header("所选行政区地图展示")
st.image("img/Lenna.png", "行政区划图：{}, {}{}".format(year, province, city))

st.header("行政区划具体变化")
st.markdown("**{}：**2019年末，全省常住人口3973万人，其中城镇常住人口2642万人。\
    辖9个地级市，29个市辖区、12个县级市、44个县（合计85个县级行政区划单位），\
        184个街道、653个镇、251个乡、19个民族乡（合计1107个乡级行政区划单位），\
            2649个居委会、14355个村委会。".format(province))
st.markdown("> 读xlsx还没有做所以现在选不同行政区这里还不会变orzzz")