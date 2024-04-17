import pandas as pd
import streamlit as st
import plotly.express as px
from src.data import functions as fc

animes_df = pd.read_csv('anime.csv')

# Converting the Score, Score-10 and Score-1 columns to float
fc.convert_scores(animes_df)
# Function to classify animes according to their score
animes_df['Appreciation'] = animes_df['Score'].apply(fc.find_rating)

st.set_page_config(layout="wide")

st.title('Animes Recommendations')

st.write("\n\n")

st.sidebar.title('MyAnimeList')
st.sidebar.markdown("[MyAnimeList](https://myanimelist.net/)")

st.sidebar.title('Crunchyroll')
st.sidebar.markdown("[Crunchyroll](https://www.crunchyroll.com/)")

st.sidebar.subheader('Personal Recommendations')
st.sidebar.markdown("[Neon Genesis Evangelion](https://myanimelist.net/anime/30/Shinseiki_Evangelion?q=neon%20genesis&cat=anime)")
st.sidebar.markdown("[Hunter x Hunter](https://myanimelist.net/anime/11061/Hunter_x_Hunter_2011?q=hunter%20x%20&cat=anime)")
st.sidebar.markdown("[Attack on Titan](https://myanimelist.net/anime/16498/Shingeki_no_Kyojin?q=shingeki&cat=anime)")
st.sidebar.markdown("[Chainsaw Man](https://myanimelist.net/anime/44511/Chainsaw_Man?q=chainsaw%20man&cat=anime)")
st.sidebar.markdown("[One Piece](https://myanimelist.net/anime/21/One_Piece?q=one%20piece&cat=anime)")

st.write('The purpose of this application is to use data about anime containing popular opinion and show things that may be interesting to create new recommendations for those looking for new animes or just want to see some data about animes.')

st.write("\n\n")

eva_url = 'https://rollingstone.uol.com.br/media/_versions/evangelion-3.0-1.0-thrice-upon-a-time-poster_widelg.jpg'
st.image(eva_url, caption='Personal Recommendation - Everything About Evangelion (Anime, Movies and Manga)')

st.write("\n\n")

st.subheader("First let's see something interesting")

appreciation_button = st.button('Show', key='appreciation_button')
if appreciation_button:
    animes_df_copy = animes_df.copy()
    animes_df_copy['Genres'] = animes_df_copy['Genres'].str.split(', ')
    unique_genres = sorted(set(animes_df_copy['Genres'].explode()))
    fig1 = px.histogram(animes_df_copy.explode('Genres'), x='Appreciation', color='Genres', category_orders={'Genres': unique_genres}, title='Appreciation by Genre', 
                    color_discrete_map={'Action': 'DeepSkyBlue', 'Adventure': 'DodgerBlue', 'Cars': 'RoyalBlue', 'Comedy': 'Blue', 
                                        'Dementia': 'DarkBlue', 'Demons': 'MidnightBlue', 'Drama': 'SlateBlue', 'Ecchi': 'Cyan', 
                                       'Fantasy': 'Turquoise', 'Game': 'DarkCyan', 'Harem': 'MediumAquamarine', 'Hentai': 'MediumSpringGreen', 
                                       'Historical': 'SpringGreen', 'Horror': 'LimeGreen', 'Josei': 'Green', 'Kids': 'DarkGreen', 
                                       'Magic': 'YellowGreen', 'Martial Arts': 'GreenYellow', 'Mecha': 'Goldenrod', 'Military': 'DarkGoldenrod', 
                                       'Music': 'SandyBrown', 'Mystery': 'Peru', 'Parody': 'Chocolate', 'Police': 'LightPink', 
                                       'Psychological': 'LightCoral', 'Romance': 'Crimson', 'Samurai': 'DarkRed', 'School': 'Red', 
                                       'Sci-Fi': 'Tomato', 'Seinen': 'OrangeRed', 'Shoujo': 'DarkOrange', 'Shoujo Ai': 'Orange', 
                                       'Shounen': 'Gold', 'Shounen Ai': 'Yellow', 'Slice of Life': 'Khaki', 'Space': 'LightGoldenrodYellow', 
                                       'Sports': 'PaleGoldenrod', 'Super Power': 'LightCyan', 'Supernatural': 'PowderBlue',
                                        'Thriller': 'PaleTurquoise', 'Unknown': 'MintCream', 'Vampire': 'Seashell', 'Yaoi': 'OldLace', 
                                       'Yuri': 'Beige'})
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown('Excellent Animes: Score greater than 9\n\nGood Animes: Score between 6 and 8.99\n\nBad Animes: Score between 3 and 5.99\n\nTerrible Animes: Score less than 3')
    st.write("\n\n")
    st.write('Wow, most animes are rated higher than 6. That is good.')
    st.write('And we can see that there are very few excellent animes. How about taking a look at them?')

st.write("\n\n")
st.write("\n\n")
st.write("\n\n")
st.write("\n\n")

st.write('Now take a look at the data we prepared below, I bet you will find some interesting animes.')

st.write("\n\n")
st.write("\n\n")

st.subheader('Excellent Animes')
ex_button = st.button('Show', key='ex_button')
if ex_button:
    ex_cols = ['Name', 'Score', 'Genres', 'Type', 'Episodes', 'Appreciation']
    excellents = animes_df[animes_df['Appreciation'] == 'Excellent'][ex_cols]
    excellents = excellents.sort_values(by='Score', ascending=False)
    st.dataframe(excellents)
    st.write('These are all the animes with a rating higher than 9. There are really few of them, I think they all must be amazing.')
    fmb_url = 'https://imgsrv.crunchyroll.com/cdn-cgi/image/format=auto,fit=contain,width=1200,height=675,quality=85/catalog/crunchyroll/ac0052958fa876ed2ef926920a88ec75.jpe'
    st.image(fmb_url, caption='Fullmetal Alchemist: Brotherhood - Anime with the highest score')

st.write("\n\n")
st.write("\n\n")

st.subheader('Most Completed Animes')
comp_button = st.button('Show', key='comp_button')
if comp_button:
    comp_cols = ['Name', 'Score', 'Genres', 'Type', 'Episodes', 'Completed', 'Appreciation']
    most_completed = animes_df.sort_values(by='Completed', ascending=False)[comp_cols]
    most_completed = most_completed.head(10)
    st.dataframe(most_completed)
    st.write('These are the 10 most watched animes. A lot of people saw Shingeki no Kyojin huh. I bet they are all worth watching.')
    snk_url = 'https://i2.wp.com/attackongeek.com/wp-content/uploads/2017/08/attack-on-titan-ss2-wallpaper-backgrounds-hd-08.jpg?resize=768%2C474&ssl=1'
    st.image(snk_url, caption='Attack on Titan Season 1 - Anime with the most completed episodes')

st.write("\n\n")
st.write("\n\n")

st.subheader('Most Dropped Animes')
drop_button = st.button('Show',  key='drop_button')
if drop_button:
    drop_cols = ['Name', 'Score', 'Genres', 'Type', 'Episodes', 'Dropped', 'Appreciation']
    most_dropped = animes_df.sort_values(by='Dropped', ascending=False)[drop_cols]
    most_dropped = most_dropped.head(10)
    st.dataframe(most_dropped)
    st.write('These are the 10 most dropped animes, there are a lot of anime with good appreciation here. I wonder why did so many people drop it.') 
    bleach_url = 'https://d17lbu6bbzbdc8.cloudfront.net/wp-content/uploads/2023/07/11083856/por-que-o-anime-bleach-foi-cancelado-1024x631.webp'
    st.image(bleach_url, caption='Bleach - Anime with the most dropped episodes')

st.write("\n\n")
st.write("\n\n")

st.subheader('Most Favorite Anime')
fav_button = st.button('Show', key='fav_button')
if fav_button:
    fav_cols = ['Name', 'Score', 'Genres', 'Type', 'Episodes', 'Favorites', 'Appreciation']
    most_favorite = animes_df.sort_values(by='Favorites', ascending=False)[fav_cols]
    most_favorite = most_favorite.head(10)
    st.dataframe(most_favorite)
    st.write('Would these be the 10 animes most loved by fans? Its worth giving such beloved animes a chance')
    fmb_url = 'https://imgsrv.crunchyroll.com/cdn-cgi/image/format=auto,fit=contain,width=1200,height=675,quality=85/catalog/crunchyroll/ac0052958fa876ed2ef926920a88ec75.jpe'
    st.image(fmb_url, caption='Fullmetal Alchemist Brotherhood - Anime with the most favorites')

st.write("\n\n")
st.write("\n\n")

st.subheader('Animes with the most 10 ratings')
score10_button = st.button('Show', key='score10_button')
if score10_button:
    s10_cols = ['Name', 'Score', 'Genres', 'Type', 'Episodes', 'Score-10', 'Appreciation']
    most_score_10 = animes_df.sort_values(by='Score-10', ascending=False)[s10_cols]
    most_score_10 = most_score_10.head(10)
    st.dataframe(most_score_10)
    st.write('These are the animes with the most votes out of 10. I bet these are animes that had a huge impact on all these people.')
    fmb_url = 'https://imgsrv.crunchyroll.com/cdn-cgi/image/format=auto,fit=contain,width=1200,height=675,quality=85/catalog/crunchyroll/ac0052958fa876ed2ef926920a88ec75.jpe'
    st.image(fmb_url, caption='Fullmetal Alchemist Brotherhood - Anime with the most 10 Scores')

st.write("\n\n")
st.write("\n\n")

st.subheader('Animes with the most 1 ratings')
score1_button = st.button('Show', key='score1_button')
if score1_button:
    s1_cols = ['Name', 'Score', 'Genres', 'Type', 'Episodes', 'Score-1', 'Appreciation']
    most_score_1 = animes_df.sort_values(by='Score-1', ascending=False)[s1_cols]
    most_score_1 = most_score_1.head(10)
    st.dataframe(most_score_1)
    st.write('These are the animes with the most votes out of 1. I bet these are animes that had a huge impact on all these people... but in the bad way.')
    st.write('No image here okay.')

st.write("\n\n")
st.write("\n\n")
st.write("\n\n")
st.write("\n\n")

st.write('If this were a competition Fullmetal Alchemist Brotherhood would be winning by far.')

st.write("\n\n")
st.write("\n\n")
st.write("\n\n")
st.write("\n\n")

st.subheader('We have some graphs with interesting data of those animes')

st.write("\n\n")

hist_button = st.button('Distribution of Anime Score')
if hist_button:
    animes_df_copy = animes_df.copy()
    animes_df_copy['Genres'] = animes_df_copy['Genres'].str.split(', ')
    unique_genres = sorted(set(animes_df_copy['Genres'].explode()))
    fig2 = px.histogram(animes_df_copy.explode('Genres'), x='Score', color='Genres', category_orders={'Genres': unique_genres}, title='Distribution of Anime Score', 
                   color_discrete_map={'Action': 'DeepSkyBlue', 'Adventure': 'DodgerBlue', 'Cars': 'RoyalBlue', 'Comedy': 'Blue', 
                                        'Dementia': 'DarkBlue', 'Demons': 'MidnightBlue', 'Drama': 'SlateBlue', 'Ecchi': 'Cyan', 
                                       'Fantasy': 'Turquoise', 'Game': 'DarkCyan', 'Harem': 'MediumAquamarine', 'Hentai': 'MediumSpringGreen', 
                                       'Historical': 'SpringGreen', 'Horror': 'LimeGreen', 'Josei': 'Green', 'Kids': 'DarkGreen', 
                                       'Magic': 'YellowGreen', 'Martial Arts': 'GreenYellow', 'Mecha': 'Goldenrod', 'Military': 'DarkGoldenrod', 
                                       'Music': 'SandyBrown', 'Mystery': 'Peru', 'Parody': 'Chocolate', 'Police': 'LightPink', 
                                       'Psychological': 'LightCoral', 'Romance': 'Crimson', 'Samurai': 'DarkRed', 'School': 'Red', 
                                       'Sci-Fi': 'Tomato', 'Seinen': 'OrangeRed', 'Shoujo': 'DarkOrange', 'Shoujo Ai': 'Orange', 
                                       'Shounen': 'Gold', 'Shounen Ai': 'Yellow', 'Slice of Life': 'Khaki', 'Space': 'LightGoldenrodYellow', 
                                       'Sports': 'PaleGoldenrod', 'Super Power': 'LightCyan', 'Supernatural': 'PowderBlue',
                                        'Thriller': 'PaleTurquoise', 'Unknown': 'MintCream', 'Vampire': 'Seashell', 'Yaoi': 'OldLace', 
                                       'Yuri': 'Beige'})
    st.plotly_chart(fig2, use_container_width=True)

st.write("\n\n")

scatter_button = st.button('Relation Between Score and Favorites')
if scatter_button:
    fig3 = px.scatter(animes_df, x='Score', y='Favorites', title='Relation Between Score and Favorites', color='Type', 
                 color_discrete_map={'TV': 'DeepSkyBlue', 'Movie': 'DodgerBlue', 'OVA': 'RoyalBlue', 'Special': 'Turquoise', 
                                     'ONA': 'LimeGreen', 'Music': 'DarkGreen', 'Unknown': 'Goldenrod'})
    st.plotly_chart(fig3, use_container_width=True)

st.write("\n\n")

bar_button = st.button('Number of Animes by Genre')
if bar_button:
    df_copy = animes_df.copy()
    df_copy['Genres'] = df_copy['Genres'].str.split(', ')
    df_copy = df_copy.explode('Genres')
    genre_counts = df_copy['Genres'].value_counts()
    fig4 = px.bar(x=genre_counts.index, y=genre_counts.values, labels={'x': 'Genre', 'y': 'Count'}, 
             title='Number of Animes by Genre', color_discrete_sequence=['#386df9'])
    st.plotly_chart(fig4)

st.write("\n\n")

mean_button = st.button('Average Score by Genre')
if mean_button:
    df_copy = animes_df.copy()
    df_copy['Genres'] = df_copy['Genres'].str.split(', ')
    df_copy = df_copy.explode('Genres')
    genre_mean_score = df_copy.groupby('Genres')['Score'].mean().reset_index()
    fig5 = px.bar(genre_mean_score, x='Genres', y='Score', title='Average Score by Genre', 
              color_discrete_sequence=['#386df9'] * len(genre_mean_score))
    st.plotly_chart(fig5)

st.write("\n\n")

type_button = st.button('Distribution of Animes by Type')
if type_button:
    type_counts = animes_df['Type'].value_counts().reset_index()
    type_counts.columns = ['Type', 'Count']
    fig6 = px.bar(type_counts, x='Type', y='Count', title='Distribution of Animes by Type', 
             color_discrete_sequence=['#386df9'])
    st.plotly_chart(fig6)

st.write("\n\n")
st.write("\n\n")
st.write("\n\n")
st.write("\n\n")

# Footer
footer_html = """
<footer style="text-align:center; padding-top:10px;">
This app was created by <a href="https://github.com/GuiMoser">@GuiMoser</a>.
And uses data from the year 2020 from the MyAnimeList website.
</footer>
"""
st.write(footer_html, unsafe_allow_html=True)
