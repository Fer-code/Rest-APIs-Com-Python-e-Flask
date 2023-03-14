from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

#Tabelas são classes
class Pessoas(Base):
    __tablename__ = 'Pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    #metodo para consultas/representação
    def __repr__(self):
        return '<Pessoa: {}>'.format(self.nome)
    
    #salvar
    def save(self):
        db_session.add(self)
        db_session.commit()

    #deletar
    def delete(self):
        db_session.delete(self)
        db_session.commit()
#
class Atividades(Base):
     __tablename__ = 'Atividades'
     idativ = Column(Integer, primary_key=True)
     nomeAtiv = Column(String(80))
     pessoaId= Column(Integer, ForeignKey('Pessoas.id'))
     pessoa = relationship('Pessoas')

def init_db():
    Base.metadata.create_all(bind=engine) #esse comando vai criar o bd

#para ninguem poder chamar esse arquivo fora dessa classe e fazer bagunça
if __name__ == '__main__':
    init_db()
