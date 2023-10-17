import os
from zipfile import ZipFile
import pytest
import shutil


@pytest.fixture(scope='session', autouse=True)
def test_create_archive():
    with ZipFile('files.zip', 'w') as file:
        file.write(os.path.abspath('resources/report_orders.xlsx'), os.path.basename('resources/report_orders.xlsx'))
        file.write(os.path.abspath('resources/delivered_not_payed.xls'),
                   os.path.basename('resources/delivered_not_payed.xls'))
        file.write(os.path.abspath('resources/test.txt'), os.path.basename('resources/test.txt'))
        file.write(os.path.abspath('resources/tickets.pdf'), os.path.basename('resources/tickets.pdf'))

    if not os.path.exists('tmp'):
        os.mkdir('tmp')

    if os.path.exists('tmp/files.zip'):
        os.remove('tmp/files.zip')
    os.rename('files.zip', 'tmp/files.zip')

    yield

    shutil.rmtree('tmp', ignore_errors=True)
