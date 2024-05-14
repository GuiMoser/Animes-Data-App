import pandas as pd

def convert_scores(df):
    df['Score'] = pd.to_numeric(df['Score'], errors='coerce')
    df['Score-10'] = pd.to_numeric(df['Score-10'], errors='coerce')
    df['Score-1'] = pd.to_numeric(df['Score-1'], errors='coerce')
    df['Episodes'] = pd.to_numeric(df['Episodes'], errors='coerce')

    df['Score-10'] = df['Score-10'].fillna(0).astype(int)
    df['Score-1'] = df['Score-1'].fillna(0).astype(int)
    df['Episodes'] = df['Episodes'].fillna(0).astype(int)
    return df

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