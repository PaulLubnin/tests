import unittest
import json
import os
from ADPY4.tests.app import check_document_existance, get_all_doc_owners_names, \
    append_doc_to_shelf, remove_doc_from_shelf, documents, directories


# def json_load(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         return json.load(file)

class TestSecretaryAssistant(unittest.TestCase):
    def setUp(self) -> None:
        # directories_path = os.path.join('fixtures', 'directories.json')
        # documents_path = os.path.join('fixtures', 'documents.json')
        # self.directories = json_load(directories_path)
        # self.documents = json_load(documents_path)
        self.test_doc = '11-2'
        self.test_shelf = '1'
        self.test_add_new_doc = '3'

    # def test_documents(self):
    #     self.assertTrue((type(self.documents) == list), 'Check loaded documents data')
    #
    # def test_directories(self):
    #     self.assertTrue((type(self.directories) == dict), 'Check loaded directories data')

    def test_check_document_existence_success(self):
        self.assertTrue(check_document_existance(self.test_doc))

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(get_all_doc_owners_names(), set)
        working_function = len(get_all_doc_owners_names())
        used_document = len(documents)
        self.assertEqual(working_function, used_document)

    def test_append_doc_to_shelf(self):
        before_append = len(directories[self.test_shelf])
        append_doc_to_shelf(self.test_add_new_doc, self.test_shelf)
        after_append = len(directories[self.test_shelf])
        self.assertGreater(after_append, before_append)

    def test_remove_doc_from_shelf(self):
        before_del = len(directories[self.test_shelf])
        remove_doc_from_shelf(self.test_doc)
        after_del = len(directories[self.test_shelf])
        self.assertGreater(before_del, after_del)


if __name__ == '__main__':
    unittest.main()
