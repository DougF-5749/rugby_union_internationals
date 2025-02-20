def date_to_year(df):
    df['year'] = df['date'].str[:4]
    return df

def group_by_year_mean_score_diff_mean_total_points(df):
    df = df.groupby('year').agg(
        {
            'score_difference': 'mean', 
            'total_points': 'mean'
        }).reset_index()
    
    df['score_difference'] = df['score_difference'].round(decimals=2)
    df['total_points'] = df['total_points'].round(decimals=2)
    return df