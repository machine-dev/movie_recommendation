import pandas as pd
import unittest
import sys
import os

# src ディレクトリをモジュール検索パスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '/Users/sn/Desktop/for_dev_me/movie_recommendation/src')))


from data_loader import load_data
from preprocess import preprocess_data
from recommender import recommend_movies

class TestRecommender(unittest.TestCase):

    @classmethod

    def setUpClass(cls):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'movie_data.xlsx'))
        cls.df = load_data(file_path)
        cls.df = preprocess_data(cls.df)

    def test_recommend_movies(self):
        movie_title = 'Rising Thunder'
        recommendations = recommend_movies(self.df, movie_title)
        self.assertIsInstance(recommendations, pd.DataFrame)
        self.assertEqual(len(recommendations), 5)

if __name__ == '__main__':
    unittest.main()
