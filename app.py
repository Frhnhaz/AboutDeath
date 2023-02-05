import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image 


@st.cache
def load_data():
    data = pd.read_csv('cause_of_deaths.csv')
    pd.to_datetime(data.Year, format='%Y')
    return data

data = load_data()
    
st.title('__Informasi Tentang Kematian di Dunia__')

with st.container():
    death_img = Image.open('death.jpg')
    st.image(death_img, caption='Tengkorak manusia yang sering menjadi simbol kematian', use_column_width='always')

with st.container():
    st.subheader('*Tentang Kematian*')    
    '''
    Kematian adalah suatu fenemona berhentinya semua tanda-tanda kehidupan
    pada makhluk hidup. Kematian memang fenomena yang mengerikan dan menyedihkan.
    Namun, kematian tetaplah sesuatu yang sangat menarik untuk dibahas.
    '''
    '''
    Oleh sebab itu, berikut adalah informasi mengenai kematian di seluruh dunia.
    '''

    st.subheader('*Jumlah Kematian Tiap Negara Sejak Tahun 1990-2019*')

    def total_of_death_global():
        year = st.slider('Tahun', 1990, 2019, 2019)
        death_global=data[data['Year']== year]
        death_global["Total"]=death_global.iloc[:, 3:].sum(axis=1)
        fig = px.choropleth(data_frame = death_global,
                            locations="Country/Territory",locationmode='country names', color="Total",
                            color_continuous_scale="viridis",height= 500,scope="world",
                            template='plotly_dark')

        fig.update_layout(title={"text": year,
                                "y":0.5,
                                "x":0.5,
                                "xanchor": "center",
                                "yanchor": "top"})
        st.write(fig)
        
    total_of_death_global()
    '''
    Tiongkok sejak tahun 1990 sampai 2019 menjadi negara dengan tingkat kematian tertinggi di dunia.
    Hal ini sesuai karena Tiongkok juga yang memiliki total populasi terbanyak di dunia.
    '''

with st.container():
    def cause_of_death():
        sebab_kematian_dunia = data.drop(['Country/Territory', 'Code', 'Year'], axis=1).sum().sort_values(ascending=False)

        sns.set_style("darkgrid")

        fig = plt.figure(figsize=(19.2, 10.8))

        palette = ["#991f17"]

        sns.barplot(x=sebab_kematian_dunia.values, y=sebab_kematian_dunia.index, palette=palette)
        plt.xlabel('Jumlah Kematian', fontsize=18, color='black')

        plt.title('Penyebab Kematian di Seluruh Dunia Tahun 1990-2019', fontsize=25, color='black')

        for p in plt.gca().patches:
            value = p.get_width()
            if value >= 1e9:
                value = '{:,.1f} B'.format(value / 1e9)
            elif value >= 1e6:
                value = '{:,.1f} M'.format(value / 1e6)
            elif value >= 1e3:
                value = '{:,.1f} K'.format(value / 1e3)
            plt.gca().annotate(value, (p.get_width(), p.get_y() + p.get_height() / 2),
                            ha='left', va='center', xytext=(5, 0), textcoords='offset points', fontsize=15, color='black')

        plt.gcf().autofmt_xdate(rotation=45)

        plt.tick_params(top=False, bottom=False, left=False, right=False, labelleft=True, labelbottom=False)
        
        st.write(fig)
        

    st.subheader('Penyebab Kematian di Dunia Sejak Tahun 1990-2019')
    
    cause_of_death()
    
    '''
    Berdasarkan grafik di atas, penyebab kematian terbesar adalah
    penyakit yang berkaitan dengan jantung dan pembuluh darah.
    '''
with st.container():
    
    '''
    Lalu bagaimana dengan Indonesia?
    Grafik di bawah akan menampilkan penyebab kematian yang ada di Indonesia.
    '''
    
    st.subheader('Penyebab Kematian di Indonesia Sejak Tahun 1990-2019')
    
    def cause_of_death_id():
        data_indonesia = data[data['Country/Territory']=='Indonesia']

        data_indonesia = data_indonesia.drop(['Country/Territory', 'Code', 'Year'], axis=1).sum().sort_values(ascending=False)

        sns.set_style("darkgrid")

        fig = plt.figure(figsize=(19.2, 10.8))

        palette = ["#991f17"]

        sns.barplot(x=data_indonesia.values, y=data_indonesia.index, palette=palette)
        plt.xlabel('Jumlah Kematian', fontsize=18, color='black')

        plt.title('Penyebab Kematian di Indonesia Tahun 1990-2019', fontsize=25, color='black')

        for p in plt.gca().patches:
            value = p.get_width()
            if value >= 1e9:
                value = '{:,.1f} B'.format(value / 1e9)
            elif value >= 1e6:
                value = '{:,.1f} M'.format(value / 1e6)
            elif value >= 1e3:
                value = '{:,.1f} K'.format(value / 1e3)
            plt.gca().annotate(value, (p.get_width(), p.get_y() + p.get_height() / 2),
                            ha='left', va='center', xytext=(5, 0), textcoords='offset points', fontsize=15, color='black')

        plt.gcf().autofmt_xdate(rotation=45)

        plt.tick_params(top=False, bottom=False, left=False, right=False, labelleft=True, labelbottom=False)
        
        st.write(fig)
    
    cause_of_death_id()
    
    '''
    Penyebab kematian nomor satu di Indonesia juga penyakit yang berkaitan dengan jantung 
    dan pembuluh darah.
    '''

with st.container():
    st.subheader('Penutup')
    '''
    Demikian informasi singkat ini, pesan yang dapat kami sampaikan adalah
    jagalah diri Anda dan berusahalah supaya tidak mendapat kematian yang buruk.
    '''