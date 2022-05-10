class Programa: #mother class
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas ):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'

#Filme e Serie utilizam herança (classe Programa)- diminuição do código - sobrescrita de métodos (polimorfismo)

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

#Playlist não utiliza henrança - composição - comporta-se como um iterável - 'magic methods' - duck typing

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
panico = Filme ('todo mundo em panico', 1999, 100)
heatrstopper = Serie('heartstopper', 2022, 1)

panico.dar_likes()
panico.dar_likes()
heatrstopper.dar_likes()
heatrstopper.dar_likes()
heatrstopper.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta, heatrstopper, panico]
maratona = Playlist('Maratona', filmes_e_series)

print(f'Tamanho da playlist: {len(maratona)}')


for programa in maratona.listagemPlaylist:
    print(programa)

