import unittest
from unittest.mock import patch
from main import main

class TestMain(unittest.TestCase):

    @patch('main.parse_arguments')
    @patch('main.run_search_engine')
    def test_main(self, mock_run_search_engine, mock_parse_arguments):
        # Mock the arguments that would be parsed from the command line
        mock_args = mock_parse_arguments.return_value
        mock_args.query = "test query"
        
        # Call the main function
        main()
        
        # Check if parse_arguments was called
        mock_parse_arguments.assert_called_once()
        
        # Check if run_search_engine was called with the correct query
        mock_run_search_engine.assert_called_once_with("test query")

if __name__ == '__main__':
    unittest.main()
