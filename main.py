from os import terminal_size
import streamlit as st
import pandas as pd
from GetProvinceNamesByYear import GetProvinceNamesByYear
from ReadExcel import ReadExcel

st.set_page_config(
    page_title = "中国行政区划改革",
    initial_sidebar_state="expanded"
)

# Provinces = ['福建', '省份1', '省份2', '省份3', '省份4', '省份5']
Cities = ['厦门', '城市1', '城市2', '城市3', '城市4', '城市5']

### Set title
st.title("🇨🇳中国行政区划改革")

### Set sidebar
st.sidebar.header("选择年份")
year = st.sidebar.slider("年份", min_value=1977, max_value=2020, value=1983)
Provinces = GetProvinceNamesByYear(year)
st.sidebar.header("选择省份")
province = st.sidebar.selectbox("省份", Provinces)
## 只能选省份了，以下代码弃用
# view = st.sidebar.select_slider("视图", ['国', '省', '市'], value='省')
# province, city = "", ""
# if view == "省" or view == "市":
#     province = st.sidebar.selectbox("省份", Provinces)
# if view == "市":
#     city = st.sidebar.selectbox("城市", Cities)

## Display info (map && detail)
# st.code("Debug信息：选中年份：{}；视图：；省份：{}；城市：".format(year, province))
# st.header("所选行政区地图展示")
st.markdown("<center> <h2> 所选行政区地图展示 </h2> </center>", unsafe_allow_html=True)
try:
    st.image("img/{}/province/{}.png".format(year, province), 
                caption="行政区划图：{}年, {}".format(year, province))
except FileNotFoundError:
    try:
        st.image("img/2020/{}.png".format(province), 
                    caption="行政区划图：{}".format(province))
    except FileNotFoundError as e:
        st.markdown("File `" + e.filename + "` do not exist.")

changes = ReadExcel(year, province)

st.markdown("**{}：**".format(province) + changes['description'][0][1])
# st.header("行政区划具体变化")
if len(changes) > 1:
    st.markdown("<center> <h2> 行政区划具体变化 </h2> </center>", unsafe_allow_html=True)
    # st.write(changes)
    for k, v in changes.items():
        if k == 'description': 
            continue
        md = "| 类型 | 内容 |\n| :--: | :-- |\n"
        st.subheader(k + '变化')
        for tup in v:
            md += "| {} | {} |\n".format(
                # (lambda x: x[:2] + '<br/>' + x[2:])(tup[0]),
                tup[0],
                tup[1].replace('\n', ' '))
        st.markdown(md, unsafe_allow_html=True)
        # df = pd.DataFrame(v, columns = ['类别', '内容'])
        # st.table(df)