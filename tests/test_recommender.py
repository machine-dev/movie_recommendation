import unittest
from data_loader import load_data
from preprocess import preprocess_data
from recommender import recommend_movies

class TestRecommender(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        file_path = '../data/movie_data.xlsx'
        cls.df = load_data(file_path)
        cls.df = preprocess_data(cls.df)

    def test_recommend_movies(self):
        movie_title = 'Rising Thunder'
        recommendations = recommend_movies(self.df, movie_title)
        self.assertIsInstance(recommendations, pd.DataFrame)
        self.assertEqual(len(recommendations), 5)

if __name__ == '__main__':
    unittest.main()