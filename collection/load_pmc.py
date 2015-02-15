from configparser import ConfigParser
from os.path import join, exists
import subprocess
import logging
import sys
import re

from collection import root_directory

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

# get the settings
config = ConfigParser()
config.add_section('DATA')
config.set('DATA', 'data_directory', join(root_directory, 'data'))
config.read(join(root_directory, 'settings.ini'))

def execute(command):    
    """Run a command and pipe stdout to logger."""
    popen = subprocess.Popen(command, stdout=subprocess.PIPE)
    lines_iterator = iter(popen.stdout.readline, b'')
    for line in lines_iterator:
        logging.debug(line)

def download(fname, source_directory, target_directory):
    source_file = source_directory.rstrip('/') + '/' + fname
    target_file = join(target_directory, fname)
    if exists(target_file):
        logging.info('File already downloaded: %s' % target_file)
        return
    logging.info('Downloading %s to %s' % (source_file, target_file))
    execute(['curl', source_file, '-o', target_file])

# download the PDF file list(s)
data_dir = config.get('DATA', 'data_directory')
source_dir = 'ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/'
pdf_fname = 'file_list.pdf.txt'
download(pdf_fname, source_dir, data_dir)
fname = 'file_list.txt'
download(fname, source_dir, data_dir)

# get a PDF
pmcid = 'PMC4177180'
popen = subprocess.Popen(['ag', '--nogroup', '--no-numbers', pmcid,
                          join(data_dir, pdf_fname)], stdout=subprocess.PIPE)
results = iter(popen.stdout.readline, b'')
urls = [result.decode('utf8').split('\t')[0] for result in results]

dir_part, fname = urls[0].rsplit('/', 1)
logging.info('Found %d files. Downloading the first one: %s.' % (len(urls), fname))
download(fname, source_dir.rstrip('/') + '/' + dir_part, join(data_dir, 'pdfs'))

