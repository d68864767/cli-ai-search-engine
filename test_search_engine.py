import unittest
from unittest.mock import patch
from search_engine import search

class TestSearchEngine(unittest.TestCase):

    @patch('search_engine.query_openai')
    def test_search_valid_response(self, mock_query_openai):
        # Mock the OpenAI API response
        mock_query_openai.return_value = "Article 1\nArticle 2\nArticle 3"

        # Perform a search using the search function
        results = search("test query")

        # Check that the results are as expected
        self.assertEqual(len(results), 3)
        self.assertIn("Article 1", results)
        self.assertIn("Article 2", results)
        self.assertIn("Article 3", results)

    @patch('search_engine.query_openai')
    def test_search_no_response(self, mock_query_openai):
        # Mock the OpenAI API response to return None
        mock_query_openai.return_value = None

        # Perform a search using the search function
        results = search("test query")

        # Check that the results list is empty
        self.assertEqual(len(results), 0)

    @patch('search_engine.query_openai')
    def test_search_result_limit(self, mock_query_openai):
        # Mock the OpenAI API response with more articles than the result limit
        mock_query_openai.return_value = "Article 1\nArticle 2\nArticle 3\nArticle 4\nArticle 5"

        # Perform a search using the search function with a result limit of 3
        results = search("test query", result_limit=3)

        # Check that the number of results does not exceed the limit
        self.assertEqual(len(results), 3)

    @patch('search_engine.query_openai')
    def test_search_language_specification(self, mock_query_openai):
        # Mock the OpenAI API response
        mock_query_openai.return_value = "Artículo 1\nArtículo 2"

        # Perform a search using the search function with a specified language
        results = search("consulta de prueba", language="es")

        # Check that the results are in the specified language
        self.assertIn("Artículo 1", results)
        self.assertIn("Artículo 2", results)

if __name__ == '__main__':
    unittest.main()
