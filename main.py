import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 불러오기 (예: CSV 파일)
# df = pd.read_csv('Delivery.csv')

# 예시 데이터 (사용자 데이터에 맞게 변경)
data = {
    'Num': list(range(1, 11)),
    'Latitude': [37.336803, 37.501303, 37.522501, 37.511178, 37.508776, 37.528486, 37.510999, 37.529438, 37.516358, 37.513337],
    'Longitude': [126.712836, 126.787808, 126.777363, 126.743209, 126.738469, 126.741476, 126.778994, 126.742163, 126.734111, 126.734624]
}
df = pd.DataFrame(data)

st.title("위도, 경도 위치 시각화")

fig = px.scatter_mapbox(df,
                        lat="Latitude",
                        lon="Longitude",
                        hover_name="Num",
                        zoom=10,
                        height=600)
fig.update_layout(mapbox_style="open-street-map")

st.plotly_chart(fig)
