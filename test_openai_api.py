import unittest
from unittest.mock import patch
from openai_api import query_openai

class TestOpenAIAPIModule(unittest.TestCase):

    @patch('openai.Completion.create')
    def test_query_openai_success(self, mock_openai_completion):
        # Mock the API response
        mock_response = {
            'choices': [
                {
                    'text': 'Paris'
                }
            ]
        }
        mock_openai_completion.return_value = mock_response

        # Call the function with a test prompt
        result = query_openai("What is the capital of France?")
        self.assertEqual(result, 'Paris')

    @patch('openai.Completion.create')
    def test_query_openai_openai_error(self, mock_openai_completion):
        # Mock an OpenAIError
        mock_openai_completion.side_effect = openai.error.OpenAIError("Test OpenAI Error")

        # Call the function and check for None response due to error
        result = query_openai("What is the capital of France?")
        self.assertIsNone(result)

    @patch('openai.Completion.create')
    def test_query_openai_unexpected_error(self, mock_openai_completion):
        # Mock an unexpected error
        mock_openai_completion.side_effect = Exception("Test Unexpected Error")

        # Call the function and check for None response due to error
        result = query_openai("What is the capital of France?")
        self.assertIsNone(result)

    # Add more tests if necessary

if __name__ == '__main__':
    unittest.main()
