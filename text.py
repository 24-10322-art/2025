import streamlit as st
import pandas as pd
import pydeck as pdk

destinations = {
    "파리": {"lat": 48.8566, "lon": 2.3522},
    "도쿄": {"lat": 35.6762, "lon": 139.6503},
    "뉴욕": {"lat": 40.7128, "lon": -74.0060},
    "런던": {"lat": 51.5074, "lon": -0.1278}
}

df = pd.DataFrame([
    {"city": city, "lat": data["lat"], "lon": data["lon"]}
    for city, data in destinations.items()
])

deck = pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v10',
    initial_view_state=pdk.ViewState(latitude=20, longitude=0, zoom=1),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200000,
            pickable=True
        )
    ],
    tooltip={"text": "{city}"}
)

st.pydeck_chart(deck)
