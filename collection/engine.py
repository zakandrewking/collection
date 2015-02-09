# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData
from configparser import ConfigParser
from os.path import join

from collection import root_directory

# get the settings
config = ConfigParser()
config.add_section('DATABASE')
config.set('DATABASE', 'postgres_host', 'localhost:5432')
config.set('DATABASE', 'postgres_database', 'collection')
config.set('DATABASE', 'postgres_user', '')
config.set('DATABASE', 'postgres_password', '')
config.set('DATABASE', 'server_port', '8001')
config.read(join(root_directory, 'settings.ini'))

engine = (create_engine("postgresql://%s:%s@%s/%s" %
                        (config.get('DATABASE', 'postgres_user'),
                         config.get('DATABASE', 'postgres_password'),
                         config.get('DATABASE', 'postgres_host'),
                         config.get('DATABASE', 'postgres_database'))))
Session = sessionmaker(bind=engine)
