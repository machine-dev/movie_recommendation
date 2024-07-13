import pandas as pd
from data_loader import load_data
from preprocess import preprocess_data

def calculate_similarity(tags1, tags2):
    tags1_set = set(tags1.split())
    tags2_set = set(tags2.split())
    return len(tags1_set.intersection(tags2_set)) / len(tags1_set.union(tags2_set))

def recommend_movies(df, movie_title, num_recommendations=5):
    if movie_title not in df['映画タイトル'].values:
        return "Movie not found in database."

    # レコメンド対象の映画のタグを取得
    target_tags = df[df['映画タイトル'] == movie_title]['tags'].values[0]
    
    # 類似度を計算
    df['similarity'] = df['tags'].apply(lambda x: calculate_similarity(target_tags, x))
    
    # 自分自身を除外して上位の映画を推薦
    recommendations = df[df['映画タイトル'] != movie_title].sort_values(by='similarity', ascending=False)
    
    return recommendations[['映画タイトル', 'ジャンル', '評価', '公開日', '監督']].head(num_recommendations)

if __name__ == "__main__":
    file_path = '../data/movie_data.xlsx'
    df = load_data(file_path)
    df = preprocess_data(df)
    movie_title = 'Rising Thunder'
    recommendations = recommend_movies(df, movie_title)
    print("Recommended movies:")
    print(recommendations)