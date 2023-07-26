import os
import unittest
from claude.check_api_keys import check_api_keys


class TestCheckApiKeys(unittest.TestCase):
    def test_check_api_keys():
        # Test case 1: Both API keys are missing
        assert check_api_keys() == False

        # Test case 2: Only OpenAI API key is present
        os.environ["OPENAI_API_KEY"] = "123456"
        assert check_api_keys() == False
        os.environ.pop("OPENAI_API_KEY")

        # Test case 3: Only Anthropoc API key is present
        os.environ["ANTHROPIC_API_KEY"] = "abcdef"
        assert check_api_keys() == "abcdef"
        os.environ.pop("ANTHROPIC_API_KEY")

        # Test case 4: Both API keys are present
        os.environ["OPENAI_API_KEY"] = "123456"
        os.environ["ANTHROPIC_API_KEY"] = "abcdef"
        assert check_api_keys() == "abcdef"
        os.environ.pop("OPENAI_API_KEY")
        os.environ.pop("ANTHROPIC_API_KEY")


if __name__ == "__main__":
    unittest.main()
