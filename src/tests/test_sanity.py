from utils.url_formatter import build_clean_url


def test_url_formatter_helper():
    base: str = "https://api.example.com/"
    endpoint: str = "/v1/users/"

    expected_result: str = "https://api.example.com/v1/users"
    actual_result: str = build_clean_url(endpoint = endpoint, base_url = base)

    assert actual_result == expected_result, \
        f"URL formatting failed! Expected {expected_result}, but got {actual_result}"   

def configure_api_headers(environment: str, *, auth_type: str = "Bearer", token: str) -> dict:
    """
    Generate a professional header dictionary for API calls. 
    Forces the user to pass 'auth_type' and 'token' as keyword-only arguments.
    """
    return {
        "X-Environment": environment,
        "Authorization": f"{auth_type} {token}"
    }

def test_api_headers_configuration():
    headers = configure_api_headers("production", token = "secret_token_abc")

    expected_headers = {
        "X-Environment": "production",
        "Authorization": "Bearer secret_token_abc"
    }

    assert headers == expected_headers, f"Headers mismatch! Got: {headers}"