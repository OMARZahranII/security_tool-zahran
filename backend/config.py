# backend/config.py

class Config:
    """Centralized configuration settings."""

    # Database settings
    DATABASE_URI = "postgresql://user:password@localhost:5432/security_db"

    # Service endpoints
    NETWORK_SCANNER_URL = "http://network_scanner:8001/scan"
    WEB_SCANNER_URL = "http://web_scanner:8002/scan"
    CLOUD_SCANNER_URL = "http://cloud_scanner:8003/scan"
    SERVER_SCANNER_URL = "http://server_scanner:8004/scan"

    # Security settings
    SECRET_KEY = "your-secret-key-here"
    TOKEN_EXPIRATION = 3600  # in seconds

config = Config()
