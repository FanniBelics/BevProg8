
def main():
    title = "Howl's Moving Castle"
    genre = 'Japanese Animation'
    author = 'Miyazaki Hayao'
    year = 2004
    imdb = 8.2
    mainC = 'Sophie'
    mins = 119
    originalLang = 'Japanese'
    job = 'hatmaker'
    text = """    Howl's moving Castle is a {genre} film, written by {author}.
    The film was produced in {year}. It's IMDB rating is {imdb}.
    The main character's name {name} is  who is a {job}.
    The film is {mins} mins long. The original language is {lang}."""

    print(text.format(title = title, genre = genre, author = author, year = year, imdb = imdb, name = mainC, job = job, mins = mins, lang = originalLang))

if __name__ == "__main__":
    main()