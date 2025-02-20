def date_to_year(df):
    df['year'] = df['date'].str[:4]
    return df