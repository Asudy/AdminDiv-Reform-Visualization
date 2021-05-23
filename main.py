from numpy import e
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
st.title("中国行政区划改革")

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

## 失败的读 shp 文件代码，暂弃
# df = gpd.read_file("data/countypoint_1996_湖北省_sample.shp")
# # st.write(df.head())
# inline_data = alt.InlineData(df.to_json())
# chart = alt.Chart(inline_data).mark_geoshape()
# st.altair_chart(chart)


## Display info (map && detail)
st.code("Debug信息：选中年份：{}；视图：；省份：{}；城市：".format(year, province))
st.header("所选行政区地图展示")
try:
    st.image("img/{}/province/{}.png".format(year, province), 
                caption="行政区划图：{}年, {}".format(year, province))
except FileNotFoundError as e:
    st.write("File " + e.filename + " do not exist，将来此处显示最新{}地图".format(province))

changes = ReadExcel(year, province)

st.header("行政区划具体变化")
st.markdown("**{}：**".format(province) + changes['description'][0][1])
if len(changes) > 1:
    for k, v in changes.items():
        if k == 'description': 
            continue
        st.subheader(k + '变化')
        df = pd.DataFrame(v, columns = ['类别', '内容'])
        st.table(df)    