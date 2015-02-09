# -*- coding: utf-8 -*-

from collection.engine import engine

from sqlalchemy import Column, String, Integer, ForeignKey, LargeBinary
from sqlalchemy.schema import Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(bind=engine)

class Document(Base):
    __tablename__ = 'document'
    id = Column(Integer, Sequence('wids'), primary_key=True)
    title = Column(String, nullable=False)
    type = Column(String(50))

    __mapper_args__ = {'polymorphic_identity': 'document',
                       'polymorphic_on': type}

class JournalArticle(Document):
    __tablename__ = 'journal_article'
    id = Column(Integer, ForeignKey(Document.id), primary_key=True)
    journal = Column(String, nullable=False)

    __mapper_args__ = {'polymorphic_identity': 'journal_article'}

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, Sequence('wids'), primary_key=True)
    first_names = Column(String)
    last_name = Column(String, nullable=False)

class DocumentAuthor(Base):
    __tablename__ = 'document_author'
    id = Column(Integer, Sequence('wids'), primary_key=True)
    document_id = Column(Integer, ForeignKey(Document.id), nullable=False)
    author_id = Column(Integer, ForeignKey(Author.id), nullable=False)
    position = Column(Integer, nullable=False)

class Citation(Base):
    __tablename__ = 'citation'
    id = Column(Integer, Sequence('wids'), primary_key=True)
    document_id = Column(Integer, ForeignKey(Document.id), nullable=False)
    citation_number_in_document = Column(Integer)
    citation_text = Column(String)
    citation_location_page = Column(Integer)
    snippet = Column(LargeBinary)
    
class DocumentCitation(Base):
    __tablename__ = 'document_citation'
    id = Column(Integer, Sequence('wids'), primary_key=True)
    document_id = Column(Integer, ForeignKey(Document.id), nullable=False)
    citation_id = Column(Integer, ForeignKey(Citation.id), nullable=False)

class LinkOutTypes(Base):
    __tablename__ = 'link_out_types'
    id = Column(Integer, Sequence('wids'), primary_key=True)
    type = Column(String(50))
    url = Column(String)
    
class LinkOut(Base):
    __tablename__ = 'link_out'
    id = Column(Integer, Sequence('wids'), primary_key=True)
    document_id = Column(Integer, ForeignKey(Document.id), nullable=False)
    link_out_type_id = Column(Integer, ForeignKey(LinkOutTypes.id), nullable=False)
    value = Column(String)
