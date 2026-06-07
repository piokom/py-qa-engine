def build_clean_url(base_url: str, endpoint: str) -> str:
    """
    Helper function to safely join base URL with API endpoint.
    """
    clean_base = base_url.strip("/")
    clean_endpoint = endpoint.strip("/")

    return f"{clean_base}/{clean_endpoint}"