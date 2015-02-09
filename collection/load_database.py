# -*- coding: utf-8 -*-

from collection.models import *
from collection import root_directory
from collection.engine import Session

import os
from os import listdir
from os.path import join
import tempfile
import subprocess
import shutil

def load_pdf(session, pdf_path):
    # info
    info = subprocess.check_output(['pdfinfo', '-meta', pdf_path],
                                   universal_newlines=True)
    info_dict = {}
    for line in info.split('\n'):
        sp = [x for x in line.split(':   ') if x != '']
        if len(sp) >= 2:
            info_dict[sp[0].strip()] = sp[1].strip()
    start_str = '<?xpacket'
    end_str = '<?xpacket end="w"?>'
    xml_string = info[info.index(start_str):info.index(end_str) + len(end_str)]

    doc = Document(title=info_dict['Title'])
    session.add(doc)
    session.commit()

    # images
    subprocess.call(['pdftoppm', pdf_path, ppm_dir + '/'])
    ppms = listdir(ppm_dir)
    # remove the files
    shutil.rmtree(ppm_dir)
    import ipdb; ipdb.set_trace()


if __name__=='__main__':
    Base.metadata.drop_all()
    Base.metadata.create_all()
    session = Session()

    test_dir = join(root_directory, 'test_data')
    ppm_dir = tempfile.mkdtemp()
    for file_name in listdir(test_dir):
        if file_name.endswith('.pdf'):
            load_pdf(session, join(test_dir, file_name))
        break

    session.close()
