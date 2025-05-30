import pandas as pd
import folium

# 엑셀 파일 불러오기 (파일 경로에 맞게 수정)
df = pd.read_excel("your_file.xlsx")

# 지도 중심을 첫 번째 좌표로 설정
map_center = [df.iloc[0, 1], df.iloc[0, 2]]
m = folium.Map(location=map_center, zoom_start=12)

# 각 위치에 마커 추가
for idx, row in df.iterrows():
    lat = row[1]  # 2열 (위도)
    lon = row[2]  # 3열 (경도)
    folium.Marker(location=[lat, lon]).add_to(m)

# HTML로 저장
m.save("map.html")
