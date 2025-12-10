# Write your solution here:
class Series:


    def __init__(self, series_name: str, seasons: int, genres: list[str]) -> None:
        self.title = series_name
        self.seasons = seasons
        self.genres = genres
        self.ratings = []


    def rate(self, rating: int) -> None:
        if 0 > rating or rating > 5:
            raise ValueError
        else:
            self.ratings.append(rating)

    
    def __str__(self) -> str:

        if len(self.ratings):
            num_of_rates = len(self.ratings)
            avg_of_rates = sum(self.ratings)/num_of_rates
            return f"{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)}\n{num_of_rates} ratings, average {avg_of_rates:.1f} points"
        
        return f"{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)}\nno ratings"


def minimum_grade(rating: float, series_list: list) -> list[Series]:
    return [series for series in series_list if rating <= sum(series.ratings)/len(series.ratings)]


def includes_genre(genre: str, series_list: list[Series]) -> list[Series]:
    return [series for series in series_list if genre in series.genres]
        

if __name__ == "__main__":
    
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    minimum_grade(4, series_list)

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)

