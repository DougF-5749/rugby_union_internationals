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

def sd_tp_filter(df, one_score_val, no_dg_value, high_scoring_val):
    one_score_mask = (df['score_difference'] < one_score_val) | (df['score_difference'] > -one_score_val)
    no_dg_mask = (df['score_difference'] > no_dg_value) | (df['score_difference'] < -no_dg_value)
    high_scoring_mask = df['total_points'] > high_scoring_val

    return df[one_score_mask & no_dg_mask & high_scoring_mask]