class Libro:

    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.genres = list()

    def add_genre(self, genre):

        self.genres.append(genre)

    def show_genres(self):
        print(self.genres)


harry = Libro('Harry Potter', 'JkRowling')

harry.add_genre('fantasia')
harry.add_genre('juvenil')


harry.show_genres()

print(harry.name)

kimetsu = Libro('Kimetsu no yaiba', 'UneJapo')

kimetsu.add_genre('shonen')
print(kimetsu.name)
kimetsu.show_genres()

