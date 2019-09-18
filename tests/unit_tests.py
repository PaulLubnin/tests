import unittest
import json
import os
from ADPY4.tests.app import check_document_existance, get_all_doc_owners_names, \
    append_doc_to_shelf


def json_load(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

class TestSecretaryAssistant(unittest.TestCase):
    def setUp(self) -> None:
        directories_path = os.path.join('fixtures', 'directories.json')
        documents_path = os.path.join('fixtures', 'documents.json')
        self.directories = json_load(directories_path)
        self.documents = json_load(documents_path)

    def test_documents(self):
        self.assertTrue((type(self.documents) == list), 'Check loaded documents data')

    def test_directories(self):
        self.assertTrue((type(self.directories) == dict), 'Check loaded directories data')

    def test_check_document_existence_success(self):
        self.assertTrue(check_document_existance('11-2'))

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(get_all_doc_owners_names(), set)
        self.assertEqual(len(get_all_doc_owners_names()), len(self.documents))

    def test_append_doc_to_shelf(self):
        doc_number = '3'
        shelf_number = '1'
        append_doc_to_shelf(doc_number, shelf_number)
        self.assertGreater(doc_number, shelf_number)


if __name__ == '__main__':
    unittest.main()
