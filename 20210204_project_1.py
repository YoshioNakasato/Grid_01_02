import streamlit as st
import numpy     as np
import pandas    as pd
#import matplotlib.pyplot as plt

#タイトル
st.title('デュレーションカーブ')

#"""
# 潮流実績
#"""
#北海道の潮流データ取り込み
data_h = pd.read_csv('streamlit_time_tide_data_h.csv')
#東北の潮流データ取り込み
data_t = pd.read_csv('streamlit_time_tide_data_t.csv')

"""
# 送電線情報:北海道
"""
info_h = pd.read_csv('streamlit_grid_info_h.csv')
info_h

"""
# 送電線情報:東北
"""
info_t = pd.read_csv('streamlit_grid_info_t.csv')
info_t

#セレクトボックス
option_h = st.selectbox(
    '北海道エリアについては、Grid_Numberを1〜70の間で指定してください',
    list(range(1,70))
)
'Grid_Name:::', info_h[info_h.columns[option_h]][1], ':::'

# 折れ線グラフ
st.line_chart( data_h[data_h.columns[option_h]][1:8785] )
st.line_chart( sorted(data_h[data_h.columns[option_h]][1:8785].astype(float), reverse=True) )


#セレクトボックス
option_t = st.selectbox(
    '東北エリアについては、Grid_Numberを1〜159の間で指定してください',
    list(range(1,159))
)
'Grid_Name:::', info_t[info_t.columns[option_t]][1], ':::'

# 折れ線グラフ
st.line_chart( data_t[data_t.columns[option_t]][1:8785] )
st.line_chart( sorted(data_t[data_t.columns[option_t]][1:8785].astype(float), reverse=True) )


# 折れ線グラフ　matplotlibを使用するコード
#fig1 = plt.figure(figsize=(12,9))
#ax   = plt.axes()
#plt.scatter( data_t[data_t.columns[option_t]][1:8785], data_h[data_h.columns[option_h]][1:8785] )
#st.pyplot(fig1)
