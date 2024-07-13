import pandas as pd

def preprocess_data(df):
    # 公開日を datetime に変換
    df['公開日'] = pd.to_datetime(df['公開日'])

    # タグの作成（タイトルとジャンルを結合）
    df['tags'] = df['映画タイトル'] + ' ' + df['ジャンル']
    return df