import streamlit as st
from ReadExcel import ReadExcel
from GetProvinceNamesByYear import GetProvinceNamesByYear

def SelectAndDisplaySingleChange():
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
    if len(changes) > 1:
        st.markdown("<center> <h2> 行政区划具体变化 </h2> </center>", unsafe_allow_html=True)
        for k, v in changes.items():
            if k == 'description': 
                continue
            with st.beta_expander(k + '变化'):
                md = "| 类型 | 内容 |\n| :--: | :--: |\n"
                for tup in v:
                    md += "| {} | {} |\n".format(
                        tup[0],
                        tup[1].replace('\n', ' '))
                st.markdown(md)
                st.write('\n')
            st.write('\n')
