import streamlit as st
from ReformStatistics import _reformDict
from ReadExcel import GetStatistics
import altair as alt
import pandas as pd
import numpy as np
from vega_datasets import data

dd = GetStatistics()
# st.write(dd)
_reformDict(dd)
# st.write(dd)

dff = pd.DataFrame(dd['地级市'])
st.write(dff)

t_base = alt.Chart(dff).encode(x = '年份:O')
t_line_1 = t_base.mark_line(color='red').encode(y='撤地设市:Q', tooltip=['年份', '撤地设市'])
t_line_2 = t_base.mark_line().encode(y='地市合并:Q')
t_line_3 = t_base.mark_line().encode(y='县市升格:Q')
t_line_4 = t_base.mark_line().encode(y='切块设市:Q')

text = alt.Chart({'values':[{}]}).mark_text(
    align="left", baseline="top"
).encode(
    x=alt.value(5),  # pixels from left
    y=alt.value(5),  # pixels from top
    text=alt.value(['Line 1', 'Line 2']))

box = alt.Chart({'values':[{}]}).mark_rect(stroke='black', color='orange').encode(
    x=alt.value(3),
    x2=alt.value(50),
    y=alt.value(3),
    y2=alt.value(30))

# graph = t_line_1 + t_line_2 + t_line_3 + t_line_4 + box + text
graph = t_line_1 + box + text
# graph = box + text
# graph = alt.layer(
#     t_line_1,
#     t_line_2,
#     t_line_3,
#     t_line_4,
#     box,
#     text,
# ).interactive()

st.altair_chart(graph, use_container_width=True)





# df = pd.DataFrame(
#     np.random.randn(200, 3),
#     columns=['a', 'b', 'c'])

# c = alt.Chart(df).mark_circle().encode(
#     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

# st.altair_chart(c, use_container_width=True)


source = data.wheat()
st.write(source)
base = alt.Chart(source).encode(x='year:O')
bar = base.mark_bar().encode(y='wheat:Q', tooltip=['year', 'wheat'])
line =  base.mark_line(color='red').encode(
    y='wages:Q',
    tooltip=['year', 'wages']
)
(bar + line).properties(width=600)
st.altair_chart((bar+line), use_container_width=True)