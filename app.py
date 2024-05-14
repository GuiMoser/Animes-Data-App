import pandas as pd
import streamlit as st
import plotly.express as px
from src.data import eda_func as fc
from src.data import px_func as pc

animes_df = pd.read_csv('anime.csv')

# Converting the Score, Score-10 and Score-1 columns to float
fc.convert_scores(animes_df)
# Function to classify animes according to their score
animes_df['Appreciation'] = animes_df['Score'].apply(fc.find_rating)

st.set_page_config(layout="wide")

st.title('Animes Data Analysis')

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

st.sidebar.title('Informations')
st.sidebar.markdown('Excellent Animes: Score greater than 9')
st.sidebar.markdown('Good Animes: Score between 6 and 8.9')
st.sidebar.markdown('Bad Animes: Score between 3 and 5.9')
st.sidebar.markdown('Terrible Animes: Score less than 3')
st.write("\n\n")
st.sidebar.markdown('Animes with 0 in the Episodes column are animes that are still being broadcast')

st.write('The purpose of this application is to use data about anime containing popular opinion and show things that may be interesting to create new recommendations for those looking for new animes and get conclusions about anime data.')

st.write("\n\n")

eva_url = 'https://rollingstone.uol.com.br/media/_versions/evangelion-3.0-1.0-thrice-upon-a-time-poster_widelg.jpg'
st.image(eva_url, caption='Personal Recommendation - Everything About Evangelion (Anime, Movies and Manga)')

st.write("\n\n")

st.subheader("First let's see something interesting")

appreciation_button = st.button('Show', key='appreciation_button')
if appreciation_button:
    # Using the get_genres functions to split the Genres column and get unique_genres.
    df_copy = pc.split_genres(animes_df)
    unique_genres = pc.get_genres(animes_df)
    order = ['Excellent', 'Good', 'Bad', 'Terrible']
    fig1 = px.histogram(df_copy.explode('Genres'), x='Appreciation', color='Genres', category_orders={'Genres': unique_genres}, title='Appreciation by Genre', 
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
                                       'Yuri': 'Beige'}, )
    fig1.update_xaxes(categoryorder='array', categoryarray=order)
    st.plotly_chart(fig1, use_container_width=True)
    st.write('Wow, most animes are rated higher than 6. That is good.')
    st.write('And we can see that there are very few excellent animes. How about taking a look at them?')

st.write("\n\n")
st.write("\n\n")
st.write("\n\n")
st.write("\n\n")

st.write('Take a look at the prepared data below, You will find some interesting animes and data.')

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
    st.image(snk_url, caption='Attack on Titan Season 1 - Most watched anime')

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
    st.image(bleach_url, caption='Bleach - Most dropped anime')

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
    st.write('These are the animes with the most votes out of 10. These are animes that had a huge impact on all these people.')
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
    st.write('These are the animes with the most votes out of 1. These are animes that had a huge impact on all these people... but in the bad way.')
    st.write('No image here okay.')

st.write("\n\n")
st.write("\n\n")
st.write("\n\n")
st.write("\n\n")

st.write('If this were a competition Fullmetal Alchemist Brotherhood would be winning by far for best anime.')

st.write("\n\n")
st.write("\n\n")
st.write("\n\n")
st.write("\n\n")

st.subheader('Here are some graphs with interesting data all animes')

st.write("\n\n")

hist_button = st.button('Distribution of Anime Score')
if hist_button:
    # Using the get_genres functions to split the Genres column and get unique_genres.
    df_copy = pc.split_genres(animes_df)
    unique_genres = pc.get_genres(animes_df)
    fig2 = px.histogram(df_copy.explode('Genres'), x='Score', color='Genres', category_orders={'Genres': unique_genres}, title='Distribution of Anime Score', 
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

bar_button = st.button('Number of Animes by Genre')
if bar_button:
    # Using the explode_genres function to split and explode the Genres column and get the genre_counts.
    df_copy = pc.explode_genres(animes_df)
    genre_counts = df_copy['Genres'].value_counts()
    fig3 = px.bar(x=genre_counts.index, y=genre_counts.values, labels={'x': 'Genre', 'y': 'Count'}, 
             title='Number of Animes by Genre', color_discrete_sequence=['#386df9'])
    st.plotly_chart(fig3)

st.write("\n\n")

best_genres_button = st.button('Most Wathed Genres')
if best_genres_button:
    # Using the explode_genres function to split and explode the Genres column.
    df_copy = pc.explode_genres(animes_df)
    # Grouping by genres and adding completed animes.
    completed_genres = df_copy.groupby('Genres')['Completed'].sum().reset_index()
    completed_genres = completed_genres.sort_values(by='Completed', ascending=False)
    fig4 = px.bar(completed_genres, x='Genres', y='Completed', title='Most Watched Genres', 
              color_discrete_sequence=['#386df9'])
    st.plotly_chart(fig4)

st.write("\n\n")

mean_button = st.button('Average Score by Genre')
if mean_button:
    # Using the explode_genres function to split and explode the Genres column
    df_copy = pc.explode_genres(animes_df)
    # Calculating the average score for each gender
    genre_mean_score = df_copy.groupby('Genres')['Score'].mean().reset_index()
    fig5 = px.bar(genre_mean_score, x='Genres', y='Score', title='Average Score by Genre', 
              color_discrete_sequence=['#386df9'] * len(genre_mean_score))
    st.plotly_chart(fig5)

st.write("\n\n")

scatter_button = st.button('Relation Between Score and Favorites')
if scatter_button:
    fig6 = px.scatter(animes_df, x='Score', y='Favorites', title='Relation Between Score and Favorites', 
                      color_discrete_sequence=['#386df9'])
    st.plotly_chart(fig6, use_container_width=True)

st.write("\n\n")

type_button = st.button('Distribution of Animes by Type')
if type_button:
    type_counts = animes_df['Type'].value_counts().reset_index()
    type_counts.columns = ['Type', 'Count']
    fig7 = px.bar(type_counts, x='Type', y='Count', title='Distribution of Animes by Type', 
             color_discrete_sequence=['#386df9'])
    st.plotly_chart(fig7)

st.write("\n\n")
st.write("\n\n")
st.write("\n\n")
st.write("\n\n")

st.subheader('Conclusions')
st.write('After separating the animes by scores, we see that the majority of animes are considered good (Score greater than 6), but only 11 animes are considered excellent (Score greater than 9). Of these 11 excellent animes, 7 of them are in the action genre, 9 of them are in the TV genre, and 8 of them have 51 or fewer episodes.\n\n', 
         'In the 10 most watched animes we see that only one of them has a score higher than 9, but the minimum score among them is 7.25, we see the action genre present in 7 animes, and we also see 8 animes with 37 or fewer episodes. We can already see great relevance in the action genre and in animes with few episodes.\n\n', 
         'In the most dropped animes we see that 9 of the 10 have a score greater than 7, and that 7 of these animes have many episodes (between 170 and 500), 2 of them are still being broadcast, we can conclude that animes the public has a greater tendency to drop animes with many episodes.\n\n', 
         'In the 10 animes with the most favorites, we maintain the trend with 7 animes having the action genre and having few episodes, however we found some exceptions, such as an anime with a score of 9.11 having a thriller and scifi genre, an anime with 500 episodes, and also an anime still broadcasting.\n\n', 
         'In animes with more 10-Score we maintain the trend of the action genre and few episodes, but with more exceptions in the genre, such as mystery, romance, drama, school, and thriller.\n\n', 
         'When analyzing the distribution of scores, we noticed that most scores are between 6 and 7.5.\n\n', 
         'Analyzing the most watched genres, we noticed a great advantage in action and comedy, which are also the genres that appear the most. We noticed some other popular genres as well, such as Shonen, Drama, Romance and Fantasy.\n\n', 
         'However, when analyzing the average score for each genre, we noticed all genres with a very similar average ranging between 6 and 7.')

st.write("\n\n")
st.write("\n\n")

st.subheader('Final Conclusions')
st.write('After all the analysis, we can conclude that the best safe choices to launch or announce a new anime are animes containing the Action or Comedy genre, which may contain subgenres such as Shonen or Drama, and have few episodes so that more people can watch. If you are working with films, Romance and Drama films are best rated. Some more distinct genres can also be successful, such as Thriller, Scifi and Mystery, as well as long animes can also be exceptions, being in the Shonen genre.')

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
