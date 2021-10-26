from config import *

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    autor = db.Column(db.String(20))
    livro = db.Column(db.String(20))
    sessao = db.Column(db.String(10))

    def __str__(self) -> str:
        return f'(id={self.id}) {self.autor}, '+ f'{self.livro}, {self.sessao}'
    
    def json(self):
        return {
            "id": self.id,"autor": self.autor,"livro": self.livro,"sessao": self.sessao
        }

if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    db.create_all()
    livro = Contato(autor="William Gibson", livro="Neuromancer", sessao="Ficcao")
    livro_1 = Contato(autor="William Gibson", livro="Count Zero", sessao="Ficcao")
    livro_2 = Contato(autor="William Gibson", livro="Mona Lisa Overdrive", sessao="Ficcao")
    livro_3 = Contato(autor="H. P. Lovecraft", livro="The Dunwich Horror", sessao="Ficcao")
    livro_4 = Contato(autor="H. P. Lovecraft", livro="At the Mountains of Madness", sessao="Ficcao")
    livro_5 = Contato(autor="Edgar Allan Poe", livro="The Raven", sessao="Ficcao")

    db.session.add(livro)
    db.session.add(livro_1)
    db.session.add(livro_2)
    db.session.add(livro_3)
    db.session.add(livro_4)
    db.session.add(livro_5)
    db.session.commit()

    print(livro)
    print(livro_1)
    print(livro_5)
    print(livro_3)