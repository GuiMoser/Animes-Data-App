import pandas as pd

def split_genres(df):
    df = df.copy()
    df['Genres'] = df['Genres'].str.split(', ')
    return df

def get_genres(df):
    df = df.copy()
    df['Genres'] = df['Genres'].str.split(', ')
    unique_genres = sorted(set(df['Genres'].explode()))
    return unique_genres

def explode_genres(df):
    df = df.copy()
    df['Genres'] = df['Genres'].str.split(', ')
    df = df.explode('Genres')
    return df