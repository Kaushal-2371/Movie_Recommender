
from recommender.movie_recommender import MovieRecommender

def main():
    recommender = MovieRecommender("data/movies.csv")
    print("Recommendations for genre='comedy', occasion='fun':")
    print(recommender.recommend(genre='comedy', occasion='fun'))

if __name__ == "__main__":
    main()
