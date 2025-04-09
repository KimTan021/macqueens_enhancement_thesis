import streamlit as st
from views import crime_hotspots, evaluation_metrics, gap_statistics, algorithm_used, enhancement_made, compare_crime_statistics, chatbot

st.set_page_config(page_title="Crime Statistics", page_icon=":chart_with_upwards_trend:", layout="centered")
st.title("📈 Crime Statistics")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Crime Hotspots", "Compare Crime Statistics", "K-Means Algorithms Comparison", "Gap Statistics",
                                        "Algorithm Used", "Enhancements Made", "Chatbot"])

with tab1:
    crime_hotspots.app()
with tab2:
    compare_crime_statistics.app()
with tab3:
    evaluation_metrics.app()
with tab4:
    gap_statistics.app()
with tab5:
    algorithm_used.app()
with tab6:
    enhancement_made.app()
with tab7:
    chatbot.app()