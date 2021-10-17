def currency(directory):
    import pandas as pd

    df = pd.read_csv(directory, parse_dates=True)
    df.drop(columns=['Volume', 'Close','Open'], inplace=True)

    df.dropna()
    df.rename(columns={'Adj Close':'Close'}, inplace=True)

    high_out = print('High median: {}       Mean: {}'.format(df['High'].median(),  df['High'].mean()))
    low_out = print('Low median: {}         Mean: {}'.format(df['Low'].median(), df['Low'].mean()))
    close_out = print('Close median: {}     Mean: {}'.format( df['Close'].median(),  df['Close'].mean()))

    return high_out, low_out, close_out