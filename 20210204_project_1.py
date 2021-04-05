import streamlit as st
import numpy     as np
import pandas    as pd
import matplotlib.pyplot as plt

#タイトル
st.title('デュレーションカーブ')

#"""
# 潮流実績
#"""
#北海道の潮流データ取り込み
data_h = pd.read_csv('streamlit_time_tide_data_h.csv')
#東北の潮流データ取り込み
data_t = pd.read_csv('streamlit_time_tide_data_t.csv')

time  = []
dummy = []
for i in range(len(data_t)-1):
    time.append(i)
    dummy.append(0.0)

"""
# 送電線情報:北海道
"""
info_h = pd.read_csv('streamlit_grid_info_h.csv')
info_h

#セレクトボックス
option_h = st.selectbox(
    '北海道エリアについては、Grid_Numberを1〜70の間で指定してください',
    list(range(1,71))
)
'Grid_Name:::', info_h[info_h.columns[option_h]][1], ':::'

# 折れ線グラフ
st.line_chart( data_h[data_h.columns[option_h]][1:8785] )
st.line_chart( sorted(data_h[data_h.columns[option_h]][1:8785].astype(float), reverse=True) )

#グラフ
try:
    if (int(data_h[data_h.columns[option_h]][0]) > 0):
        #figure()でグラフを表示する領域をつくり，figというオブジェクトにする．
        fig = plt.figure(figsize=(16,12))
        #add_subplot()でグラフを描画する領域を追加する．引数は行，列，場所
        ax1 = fig.add_subplot(2, 2, 1)
        ax2 = fig.add_subplot(2, 2, 2)
        ax3 = fig.add_subplot(2, 2, 3)
        ax4 = fig.add_subplot(2, 2, 4)
    
        ax1.scatter(pd.DataFrame(time), data_h[data_h.columns[option_h]][1:8785], s=10, c='black', alpha=0.2)
        ax1.set_title("Grid Name:"+info_h[info_h.columns[option_h]][1])
        ax1.set_ylim((-1.2)*data_h[data_h.columns[option_h]][0], 1.2*data_h[data_h.columns[option_h]][0])
        ax1.axhline((-1)*data_h[data_h.columns[option_h]][0], color = "magenta")
        ax1.axhline(data_h[data_h.columns[option_h]][0], color = "magenta")
        ax1.text(6000, 1.05*data_h[data_h.columns[option_h]][0], "Operation Capacity", color = "magenta")
        ax1.set_xlabel("Time(hours)")
        ax1.set_ylabel("Capacity(MW)")
    
        ax2.scatter(pd.DataFrame(time), sorted(data_h[data_h.columns[option_h]][1:8785].astype(float), reverse=True), s=10, color='black', alpha=0.2)
        ax2.set_title("Grid Name:"+info_h[info_h.columns[option_h]][1])
        ax2.set_ylim((-1.2)*data_h[data_h.columns[option_h]][0], 1.2*data_h[data_h.columns[option_h]][0])
        ax2.axhline((-1)*data_h[data_h.columns[option_h]][0], color = "magenta")
        ax2.axhline(data_h[data_h.columns[option_h]][0], color = "magenta")
        ax2.text(6000, 1.05*data_h[data_h.columns[option_h]][0], "Operation Capacity", color = "magenta")
        ax2.grid()
        ax2.set_xlabel("Time(hours)")
        ax2.set_ylabel("Capacity(MW)")
        
        ax3.scatter(pd.DataFrame(time), data_h[data_h.columns[option_h]][1:8785], s=10, c='black', alpha=0.2)
        ax3.set_xlabel("Time(hours)")
        ax3.set_ylabel("Capacity(MW)")
    
        ax4.scatter(pd.DataFrame(time), sorted(data_h[data_h.columns[option_h]][1:8785].astype(float), reverse=True), s=10, color='black', alpha=0.2)
        ax4.set_xlabel("Time(hours)")
        ax4.set_ylabel("Capacity(MW)")
        st.pyplot(fig)
        
    else:
        #figure()でグラフを表示する領域をつくり，figというオブジェクトにする．
        fig = plt.figure(figsize=(16,10))
        #add_subplot()でグラフを描画する領域を追加する．引数は行，列，場所
        ax1 = fig.add_subplot(2, 2, 1)
        ax2 = fig.add_subplot(2, 2, 2)
    
        ax1.scatter(pd.DataFrame(time), data_h[data_h.columns[option_h]][1:8785], s=10, c='black', alpha=0.2)
        ax1.set_xlabel("Time(hours)")
        ax1.set_ylabel("Capacity(MW)")
        ax1.set_title("Grid Name:"+info_h[info_h.columns[option_h]][1])
        ax1.text(5250, 0.99*data_h[data_h.columns[option_h]].max(), "Operation Capacity is not disclosed", color = "magenta")
    
        ax2.scatter(pd.DataFrame(time), sorted(data_h[data_h.columns[option_h]][1:8785].astype(float), reverse=True), s=10, color='black', alpha=0.2)
        ax2.set_title("Grid Name:"+info_h[info_h.columns[option_h]][1])
        ax2.grid()
        ax2.set_xlabel("Time(hours)")
        ax2.set_ylabel("Capacity(MW)")
        ax2.text(5250, 0.99*data_h[data_h.columns[option_h]].max(), "Operation Capacity is not disclosed", color = "magenta")
    
        st.pyplot(fig)
              
except ValueError:
        #figure()でグラフを表示する領域をつくり，figというオブジェクトにする．
        fig = plt.figure(figsize=(16,10))
        #add_subplot()でグラフを描画する領域を追加する．引数は行，列，場所
        ax1 = fig.add_subplot(2, 2, 1)
        ax2 = fig.add_subplot(2, 2, 2)
    
        ax1.scatter(pd.DataFrame(time), pd.DataFrame(dummy), s=10, c='black', alpha=0.2)
        ax1.set_xlabel("Time(hours)")
        ax1.set_ylabel("Capacity(MW)")
        ax1.set_title("Grid Name:"+info_h[info_h.columns[option_h]][1])
        ax1.text(8000, 0.006, "No Data", color = "magenta")
    
        ax2.scatter(pd.DataFrame(time), pd.DataFrame(dummy), s=10, color='black', alpha=0.2)
        ax2.set_title("Grid Name:"+info_h[info_h.columns[option_h]][1])
        ax2.grid()
        ax2.set_xlabel("Time(hours)")
        ax2.set_ylabel("Capacity(MW)")
        ax2.text(8000, 0.006, "No Data", color = "magenta")
    
        st.pyplot(fig)




"""
# 送電線情報:東北
"""
info_t = pd.read_csv('streamlit_grid_info_t.csv')
info_t

#セレクトボックス
option_t = st.selectbox(
    '東北エリアについては、Grid_Numberを1〜158の間で指定してください',
    list(range(1,159))
)
'Grid_Name:::', info_t[info_t.columns[option_t]][1], ':::'

# 折れ線グラフ
st.line_chart( data_t[data_t.columns[option_t]][1:8785] )
st.line_chart( sorted(data_t[data_t.columns[option_t]][1:8785].astype(float), reverse=True) )

# グラフ
try:
    if (int(data_t[data_t.columns[option_t]][0]) > 0):
        #figure()でグラフを表示する領域をつくり，figというオブジェクトにする．
        fig = plt.figure(figsize=(16,12))
        #add_subplot()でグラフを描画する領域を追加する．引数は行，列，場所
        ax1 = fig.add_subplot(2, 2, 1)
        ax2 = fig.add_subplot(2, 2, 2)
        ax3 = fig.add_subplot(2, 2, 3)
        ax4 = fig.add_subplot(2, 2, 4)
    
        ax1.scatter(pd.DataFrame(time), data_t[data_t.columns[option_t]][1:8785], s=10, c='black', alpha=0.2)
        ax1.set_title("Grid Name:"+info_t[info_t.columns[option_t]][1])
        ax1.set_ylim((-1.2)*data_t[data_t.columns[option_t]][0], 1.2*data_t[data_t.columns[option_t]][0])
        ax1.axhline((-1)*data_t[data_t.columns[option_t]][0], color = "magenta")
        ax1.axhline(data_t[data_t.columns[option_t]][0], color = "magenta")
        ax1.text(6000, 1.05*data_t[data_t.columns[option_t]][0], "Operation Capacity", color = "magenta")
        ax1.set_xlabel("Time(hours)")
        ax1.set_ylabel("Capacity(MW)")
    
        ax2.scatter(pd.DataFrame(time), sorted(data_t[data_t.columns[option_t]][1:8785].astype(float), reverse=True), s=10, color='black', alpha=0.2)
        ax2.set_title("Grid Name:"+info_t[info_t.columns[option_t]][1])
        ax2.set_ylim((-1.2)*data_t[data_t.columns[option_t]][0], 1.2*data_t[data_t.columns[option_t]][0])
        ax2.axhline((-1)*data_t[data_t.columns[option_t]][0], color = "magenta")
        ax2.axhline(data_t[data_t.columns[option_t]][0], color = "magenta")
        ax2.text(6000, 1.05*data_t[data_t.columns[option_t]][0], "Operation Capacity", color = "magenta")
        ax2.grid()
        ax2.set_xlabel("Time(hours)")
        ax2.set_ylabel("Capacity(MW)")
        
        ax3.scatter(pd.DataFrame(time), data_t[data_t.columns[option_t]][1:8785], s=10, c='black', alpha=0.2)
        ax3.set_xlabel("Time(hours)")
        ax3.set_ylabel("Capacity(MW)")
    
        ax4.scatter(pd.DataFrame(time), sorted(data_t[data_t.columns[option_t]][1:8785].astype(float), reverse=True), s=10, color='black', alpha=0.2)
        ax4.set_xlabel("Time(hours)")
        ax4.set_ylabel("Capacity(MW)")
        st.pyplot(fig)
        
    else:
        #figure()でグラフを表示する領域をつくり，figというオブジェクトにする．
        fig = plt.figure(figsize=(16,10))
        #add_subplot()でグラフを描画する領域を追加する．引数は行，列，場所
        ax1 = fig.add_subplot(2, 2, 1)
        ax2 = fig.add_subplot(2, 2, 2)
    
        ax1.scatter(pd.DataFrame(time), data_t[data_t.columns[option_t]][1:8785], s=10, c='black', alpha=0.2)
        ax1.set_xlabel("Time(hours)")
        ax1.set_ylabel("Capacity(MW)")
        ax1.set_title("Grid Name:"+info_t[info_t.columns[option_t]][1])
        ax1.text(5250, 0.99*data_t[data_t.columns[option_t]].max(), "Operation Capacity is not disclosed", color = "magenta")
    
        ax2.scatter(pd.DataFrame(time), sorted(data_t[data_t.columns[option_t]][1:8785].astype(float), reverse=True), s=10, color='black', alpha=0.2)
        ax2.set_title("Grid Name:"+info_t[info_t.columns[option_t]][1])
        ax2.grid()
        ax2.set_xlabel("Time(hours)")
        ax2.set_ylabel("Capacity(MW)")
        ax2.text(5250, 0.99*data_t[data_t.columns[option_t]].max(), "Operation Capacity is not disclosed", color = "magenta")
    
        st.pyplot(fig)
              
except ValueError:
        #figure()でグラフを表示する領域をつくり，figというオブジェクトにする．
        fig = plt.figure(figsize=(16,10))
        #add_subplot()でグラフを描画する領域を追加する．引数は行，列，場所
        ax1 = fig.add_subplot(2, 2, 1)
        ax2 = fig.add_subplot(2, 2, 2)
    
        ax1.scatter(pd.DataFrame(time), pd.DataFrame(dummy), s=10, c='black', alpha=0.2)
        ax1.set_xlabel("Time(hours)")
        ax1.set_ylabel("Capacity(MW)")
        ax1.set_title("Grid Name:"+info_t[info_t.columns[option_t]][1])
        ax1.text(8000, 0.006, "No Data", color = "magenta")
    
        ax2.scatter(pd.DataFrame(time), pd.DataFrame(dummy), s=10, color='black', alpha=0.2)
        ax2.set_title("Grid Name:"+info_t[info_t.columns[option_t]][1])
        ax2.grid()
        ax2.set_xlabel("Time(hours)")
        ax2.set_ylabel("Capacity(MW)")
        ax2.text(8000, 0.006, "No Data", color = "magenta")
    
        st.pyplot(fig)



