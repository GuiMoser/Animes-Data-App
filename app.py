import pandas as pd
import streamlit as st
import plotly.express as px

animes_df = pd.read_csv('anime.csv')

# Converting the Score, Score-10 and Score-1 columns to float
animes_df['Score'] = pd.to_numeric(animes_df['Score'], errors='coerce')
animes_df['Score-10'] = pd.to_numeric(animes_df['Score-10'], errors='coerce')
animes_df['Score-1'] = pd.to_numeric(animes_df['Score-1'], errors='coerce')

# Converting the Score-10 and Score-1 columns to int
animes_df['Score-10'] = animes_df['Score-10'].fillna(0).astype(int)
animes_df['Score-1'] = animes_df['Score-1'].fillna(0).astype(int)

# Defining a function to classify animes according to their score
def find_rating(score):
    if score == 'Unknown':
        return 'Unknown'
        
    try:
        score = float(score)
        if score >= 9:
            return 'Excellent'
        elif score >= 6:
            return 'Good'
        elif score >= 3:
            return 'Bad'
        else:
            return 'Terrible'
    except ValueError:
        return 'Unknown'
    
# Using the function to create a column with the anime appreciation level
animes_df['Appreciation'] = animes_df['Score'].apply(find_rating)

# Copying the df so we don't modify the original.
animes_df_copy = animes_df.copy()
# Dividing genres into separate lists.
animes_df_copy['Genres'] = animes_df_copy['Genres'].str.split(', ')
# Extracting all unique genres present in the data.
unique_genres = sorted(set(animes_df_copy['Genres'].explode()))

# Copying the df so we don't modify the original.
df_copy = animes_df.copy()
# Dividing genres into separate lists.
df_copy['Genres'] = df_copy['Genres'].str.split(', ')
# Dividing the genre lists into separate lines.
df_copy = df_copy.explode('Genres')
# Anime count by genre
genre_counts = df_copy['Genres'].value_counts()
# Calculating the average score for each gender
genre_mean_score = df_copy.groupby('Genres')['Score'].mean().reset_index()

# Counting the number of each type of anime
type_counts = animes_df['Type'].value_counts().reset_index()
# Renaming the columns
type_counts.columns = ['Type', 'Count']

st.title('Animes Recommendations App')

st.write('The purpose of this application is to use data about anime containing popular opinion and show things that may be interesting to create new recommendations for those looking for new animes.')

st.write("\n\n")

eva_url = 'https://rollingstone.uol.com.br/media/_versions/evangelion-3.0-1.0-thrice-upon-a-time-poster_widelg.jpg'

st.image(eva_url, caption='Personal Recommendation - Everything about Evangelion (Anime, Movies and Manga)')

st.write("\n\n")

st.subheader('First I would like to show you something interesting')

appreciation_button = st.button('Show', key='appreciation_button')
if appreciation_button:
    st.markdown('Excellent Animes: Score greater than 9\n\nGood Animes: Score between 6 and 8.99\n\nBad Animes: Score between 3 and 5.99\n\nTerrible Animes: Score less than 3')
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
    st.write('We can see that there are very few excellent animes. How about taking a look at them?')

st.write("\n\n")
st.write("\n\n")

st.write('Now take a look at the data we prepared below, I bet you will find some interesting animes.')

st.write("\n\n")

st.subheader('Excellent Animes')
ex_button = st.button('Show', key='ex_button')
if ex_button:
    # Defining the columns
    ex_cols = ['Name', 'Score', 'Genres', 'Type', 'Episodes', 'Appreciation']
    # Extracting only the excellent animes
    excellents = animes_df[animes_df['Appreciation'] == 'Excellent'][ex_cols]
    # Sorting based on score
    excellents = excellents.sort_values(by='Score', ascending=False)
    st.dataframe(excellents)
    st.write('These are all the animes with a rating higher than 9. There are really few of them, I think they all must be amazing.')

st.write("\n\n")

st.subheader('Most Completed Animes')
comp_button = st.button('Show', key='comp_button')
if comp_button:
    comp_cols = ['Name', 'Score', 'Genres', 'Type', 'Episodes', 'Completed', 'Appreciation']
    most_completed = animes_df.sort_values(by='Completed', ascending=False)[comp_cols]
    most_completed = most_completed.head(10)
    st.dataframe(most_completed)
    st.write('These are the 10 most watched animes. A lot of people saw Shingeki no Kyojin huh. I bet they are all worth watching.')

st.write("\n\n")

st.subheader('Most Dropped Animes')
drop_button = st.button('Show',  key='drop_button')
if drop_button:
    drop_cols = ['Name', 'Score', 'Genres', 'Type', 'Episodes', 'Dropped', 'Appreciation']
    most_dropped = animes_df.sort_values(by='Dropped', ascending=False)[drop_cols]
    most_dropped = most_dropped.head(10)
    st.dataframe(most_dropped)
    st.write('These are the 10 most dropped animes, there are a lot of anime with good appreciation here. I wonder why did so many people drop it.') 

st.write("\n\n")

st.subheader('Most Favorite Anime')
fav_button = st.button('Show', key='fav_button')
if fav_button:
    fav_cols = ['Name', 'Score', 'Genres', 'Type', 'Episodes', 'Favorites', 'Appreciation']
    most_favorite = animes_df.sort_values(by='Favorites', ascending=False)[fav_cols]
    most_favorite = most_favorite.head(10)
    st.dataframe(most_favorite)
    st.write('Would these be the 10 animes most loved by fans? Its worth giving such beloved animes a chance')

st.subheader('Animes with the most 10 ratings')
score10_button = st.button('Show', key='score10_button')
if score10_button:
    s10_cols = ['Name', 'Score', 'Genres', 'Type', 'Episodes', 'Score-10', 'Appreciation']
    most_score_10 = animes_df.sort_values(by='Score-10', ascending=False)[s10_cols]
    most_score_10 = most_score_10.head(10)
    st.dataframe(most_score_10)
    st.write('These are the animes with the most votes out of 10. I bet these are animes that had a huge impact on all these people.')

st.write("\n\n")

st.subheader('Animes with the most 1 ratings')
score1_button = st.button('Show', key='score1_button')
if score1_button:
    s1_cols = ['Name', 'Score', 'Genres', 'Type', 'Episodes', 'Score-1', 'Appreciation']
    most_score_1 = animes_df.sort_values(by='Score-1', ascending=False)[s1_cols]
    most_score_1 = most_score_1.head(10)
    st.dataframe(most_score_1)
    st.write('These are the animes with the most votes out of 1. I bet these are animes that had a huge impact on all these people... but in the bad way.')

st.write("\n\n")
st.write("\n\n")

st.subheader('We have some graphs with interesting data of those animes')

hist_button = st.button('Distribution of Anime Score')
if hist_button:
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

scatter_button = st.button('Relation Between Score and Favorites')
if scatter_button:
    fig3 = px.scatter(animes_df, x='Score', y='Favorites', title='Relation Between Score and Favorites', color='Type', 
                 color_discrete_map={'TV': 'DeepSkyBlue', 'Movie': 'DodgerBlue', 'OVA': 'RoyalBlue', 'Special': 'Turquoise', 
                                     'ONA': 'LimeGreen', 'Music': 'DarkGreen', 'Unknown': 'Goldenrod'})
    st.plotly_chart(fig3, use_container_width=True)

bar_button = st.button('Number of Animes by Genre')
if bar_button:
    fig4 = px.bar(x=genre_counts.index, y=genre_counts.values, labels={'x': 'Genre', 'y': 'Count'}, 
             title='Number of Animes by Genre', color_discrete_sequence=['#386df9'])
    st.plotly_chart(fig4)

mean_button = st.button('Average Score by Genre')
if mean_button:
    fig5 = px.bar(genre_mean_score, x='Genres', y='Score', title='Average Score by Genre', 
              color_discrete_sequence=['#386df9'] * len(genre_mean_score))
    st.plotly_chart(fig5)

type_button = st.button('Distribution of Animes by Type')
if type_button:
    fig6 = px.bar(type_counts, x='Type', y='Count', title='Distribution of Animes by Type', 
             color_discrete_sequence=['#386df9'])
    st.plotly_chart(fig6)

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
