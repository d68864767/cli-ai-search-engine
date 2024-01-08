import unittest
from unittest.mock import mock_open, patch
from utils import load_config, save_config, sanitize_query

class TestUtils(unittest.TestCase):

    def test_load_config_success(self):
        """Test loading of a valid config file."""
        test_config = {
            "api_key": "your_api_key_here",
            "search_engine_name": "AI-Powered Search Engine"
        }
        with patch('builtins.open', mock_open(read_data=json.dumps(test_config))):
            config = load_config()
        self.assertEqual(config, test_config)

    def test_load_config_file_not_found(self):
        """Test loading of a config file that does not exist."""
        with patch('builtins.open', side_effect=FileNotFoundError):
            config = load_config('nonexistent_config.json')
        self.assertIsNone(config)

    def test_load_config_json_decode_error(self):
        """Test loading of a config file with invalid JSON."""
        with patch('builtins.open', mock_open(read_data='invalid_json')):
            config = load_config()
        self.assertIsNone(config)

    def test_load_config_unexpected_error(self):
        """Test loading of a config file with an unexpected error."""
        with patch('builtins.open', side_effect=Exception('Unexpected error')):
            config = load_config()
        self.assertIsNone(config)

    def test_save_config(self):
        """Test saving a config dictionary to a file."""
        test_config = {
            "api_key": "your_new_api_key_here",
            "search_engine_name": "AI-Powered Search Engine"
        }
        with patch('builtins.open', mock_open()) as mocked_file:
            save_config(test_config)
            mocked_file.assert_called_once_with('config.json', 'w')
            mocked_file().write.assert_called_once_with(json.dumps(test_config, indent=4))

    def test_sanitize_query(self):
        """Test the sanitization of a search query."""
        test_query = "This is a test query\nwith a newline."
        expected_sanitized_query = "This is a test query with a newline."
        sanitized_query = sanitize_query(test_query)
        self.assertEqual(sanitized_query, expected_sanitized_query)

if __name__ == '__main__':
    unittest.main()
