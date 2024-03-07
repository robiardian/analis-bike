import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

hour_df = pd.read_csv("hour_cleaned.csv")
day_df = pd.read_csv("https://github.com/robiardian/analis-bike/blob/master/dashboard/day_cleaned.csv")
# Streamlit App# Define function for plotting seasonal usage
def plot_seasonal_usage(day_df):

    st.write("Pertanyaan 1: penyewaan sepeda paling banyak pada musim apa ?")
    seasonal_usage = day_df.groupby('season')[['registered', 'casual']].sum().reset_index()

    fig_seasonal = plt.figure(figsize=(10, 6))
    plt.bar(
        seasonal_usage['season'],
        seasonal_usage['registered'],
        label='Registered',
        color='tab:blue'
    )
    plt.bar(
        seasonal_usage['season'],
        seasonal_usage['casual'],
        label='Casual',
        color='tab:orange'
    )
    plt.xlabel(None)
    plt.ylabel(None)
    plt.title('Jumlah penyewaan sepeda berdasarkan musim')
    plt.legend()
    st.pyplot(fig_seasonal)
    st.write("Berdasarkan hasil analisis menggunakan barplot di atas, dapat disimpulkan bahwa musim yang paling disukai oleh para pengguna sepeda (baik Casual maupun Registered) adalah musim gugur (Fall), diikuti oleh musim panas (Summer), musim dingin (Winter), dan terakhir adalah musim semi (Spring).")

# Define function for plotting bike users based on weather situation
def plot_weather_situation(day_df):
    st.write("Pertanyaan 2: Apakah ada peran dari cuaca terhadap jumlah pengguna sepeda?")
    fig_weather = plt.figure(figsize=(10,6))
    sns.barplot(
        x='weather_situation',
        y='count_cr',
        data=day_df,
        palette='viridis'
    )
    plt.title('Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(fig_weather)
    st.write("Dari analisis menggunakan boxplot, dapat disimpulkan bahwa terdapat korelasi yang jelas antara kondisi cuaca dan jumlah penyewa sepeda. Kondisi cuaca cerah/setengah mendung menarik minat paling banyak, diikuti oleh kondisi berkabut/mendung, sementara kondisi sedikit bersalju/hujan menjadi yang paling kurang diminati.")

# Define function for plotting bike users based on season and temperature
def plot_season_temperature(hour_df):

    st.write("Apakah ada korelasi antara suhu yang mengindikasikan kondisi saat aktivitas penyewaan sepeda sedang tinggi?")
    fig_season_temp = plt.figure(figsize=(10,6))
    season_palette = sns.color_palette("husl", 4)
    sns.scatterplot(
        x='temp',
        y='count_cr',
        data=hour_df,
        hue='season',
        palette=season_palette
    )
    plt.xlabel("Termperatur")
    plt.ylabel("Jumlah Penyepeda")
    plt.title("Sebaran Penyewa berdasarkan musim dan temperatur")
    plt.tight_layout()
    st.pyplot(fig_season_temp)
    st.write("- Ketika suhu rendah, penggunaan sepeda juga rendah, terutama saat musim dingin.")

    st.write("- Saat suhu naik, penggunaan sepeda meningkat, terutama selama musim panas.")
    st.write("- Namun, terdapat suhu ideal di mana penggunaan sepeda mencapai puncaknya, terutama pada musim gugur dan musim panas, yaitu antara 20°C hingga 30°C.")
    st.write("- Pada hari-hari dengan suhu tersebut, diperkirakan penggunaan sepeda akan tinggi.")

# Main function to run the Streamlit app
def main():
    st.title("Visualisasi Penyewaan Sepeda")
    
    # Sidebar for data selection if needed
    st.sidebar.title("Pilihan Data")
    # You can add options here if you have multiple datasets
    
    # Choose which visualization to display
    visualization_option = st.sidebar.selectbox(
        "Pilih Visualisasi:",
        ("Pertanyaan 1", "Pertanyaan 2", "Pertanyaan 3")
    )
    
    # Display the selected visualization
    if visualization_option == "Pertanyaan 1":
        plot_seasonal_usage(day_df)
    elif visualization_option == "Pertanyaan 2":
        plot_weather_situation(day_df)
    elif visualization_option == "Pertanyaan 3":
        plot_season_temperature(hour_df)

if __name__ == "__main__":
    main()
