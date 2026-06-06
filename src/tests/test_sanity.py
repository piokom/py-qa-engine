from utils.url_formatter import build_clean_url


def test_url_formatter_helper():
    base: str = "https://api.example.com/"
    endpoint: str = "/v1/users/"

    expected_result: str = "https://api.example.com/v1/users"
    actual_result: str = build_clean_url(base, endpoint)

    assert actual_result == expected_result, \
        f"URL formatting failed! Expected {expected_result}, but got {actual_result}"   