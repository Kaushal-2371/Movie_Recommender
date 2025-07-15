
from recommender.movie_recommender import MovieRecommender

def main():
    recommender = MovieRecommender("data/movies.csv")
    print("Recommendations for genre='comedy', mood='fun':")
    print(recommender.recommend(genre='comedy', mood='fun'))

if __name__ == "__main__":
    main()
