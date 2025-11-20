from pydantic_settings import BaseSettings
from typing import Dict, Optional, Union, List
import json
import os
import logging

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    # Supabase Configuration
    supabase_url: str
    supabase_service_role_key: str
    supabase_anon_key: str
    supabase_jwt_secret: Optional[str] = None
    supabase_tenant_jwt_secret: Optional[str] = None
    
    def __init__(self, **kwargs):
        """Initialize settings with debug logging"""
        logger.info("🔧 SETTINGS INITIALIZATION DEBUG")
        logger.info("=" * 50)
        
        # Log environment variable availability before Pydantic processing
        critical_env_vars = {
            'TOKEN_ENCRYPTION_KEY': os.getenv('TOKEN_ENCRYPTION_KEY'),
            'SUPABASE_URL': os.getenv('SUPABASE_URL'), 
            'SUPABASE_SERVICE_ROLE_KEY': os.getenv('SUPABASE_SERVICE_ROLE_KEY'),
            'SUPABASE_JWT_SECRET': os.getenv('SUPABASE_JWT_SECRET'),
            'SECRET_KEY': os.getenv('SECRET_KEY')
        }
        
        for var_name, value in critical_env_vars.items():
            if value:
                preview = value[:15] + "..." if len(value) > 15 else value
                logger.info(f"✅ ENV {var_name}: {preview} (len: {len(value)})")
            else:
                logger.info(f"❌ ENV {var_name}: NOT SET")
        
        # Call parent constructor
        super().__init__(**kwargs)
        
        # Log what Pydantic actually loaded
        logger.info("📊 PYDANTIC LOADED VALUES:")
        loaded_values = {
            'token_encryption_key': getattr(self, 'token_encryption_key', None),
            'supabase_url': getattr(self, 'supabase_url', None),
            'supabase_service_role_key': getattr(self, 'supabase_service_role_key', None),
            'supabase_jwt_secret': getattr(self, 'supabase_jwt_secret', None),
            'secret_key': getattr(self, 'secret_key', None)
        }
        
        for field_name, value in loaded_values.items():
            if value:
                preview = str(value)[:15] + "..." if len(str(value)) > 15 else str(value)
                logger.info(f"✅ LOADED {field_name}: {preview} (len: {len(str(value))})")
            else:
                logger.info(f"❌ LOADED {field_name}: NOT SET")
        
        logger.info("=" * 50)
        logger.info("🏁 SETTINGS INITIALIZATION COMPLETE")

    # Hostaway API Tokens (JSON string) - DEPRECATED, using Token Management now
    hostaway_tokens: Optional[str] = None

    # Application Settings
    app_name: str = "Flex PMS Backend"
    debug: bool = False
    frontend_url: str = "http://localhost:5173"  # Frontend URL for emails and links
    backend_url: str = "http://localhost:8000"  # Backend URL for internal API calls
    cors_origins: List[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:5173",
        "http://localhost:5174",
        "https://new-pms.netlify.app",
        "https://pms.theflex.global",
        "https://new-pms.theflex.global/",
    ]

    # Security
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 10080  # 7 days in minutes (7 * 24 * 60)
    
    # Token Encryption
    token_encryption_key: str

    # SendGrid Configuration (add these lines)
    sendgrid_api_key: Optional[str] = None
    sendgrid_from_email: Optional[str] = None

    # Cron job security
    cron_secret: Optional[str] = None

    # N8N Configuration
    n8n_webhook_url: Optional[str] = (
        "https://n8n.theflex.global/webhook/2b770e31-cedd-408f-ae28-afa8b23c598d"
    )
    n8n_checkin_crisis_webhook_url: Optional[str] = None

    @property
    def CRON_SECRET(self) -> str:
        """Get the cron secret for easy access"""
        return self.cron_secret or "dev-secret"

    # Environment indicator
    environment: str

    # n8n Integration
    n8n_verification_webhook_url: str
    n8n_webhook_secret: Optional[str] = None

    # OpenAI Configuration
    openai_api_key: str

    # Stripe Configuration
    stripe_secret_key: Optional[str] = None
    stripe_publishable_key: Optional[str] = None
    stripe_webhook_secret: Optional[str] = None

    # Google Maps Configuration
    google_maps_api_key: Optional[str] = None

    # Supabase Storage
    supabase_storage_bucket: str = "verification-images"
    supabase_upsell_storage_bucket: str = "upsell-images"

    # Database Connection Pool Configuration
    database_pool_size: int = 20  # Base connection pool size
    database_max_overflow: int = 30  # Additional connections when needed
    database_pool_timeout: int = 30  # Connection timeout in seconds
    database_pool_recycle: int = 3600  # Recycle connections every hour
    database_max_retries: int = 3  # Max retry attempts for failed connections
    database_retry_delay: float = 0.5  # Base delay between retries (exponential backoff)
    
    # Supabase Connection Management
    supabase_max_concurrent_connections: int = 150  # Max concurrent Supabase connections (increased for performance)
    supabase_connection_timeout: float = 30.0  # Request timeout
    supabase_pool_recycle_interval: int = 1800  # 30 minutes
    
    # Redis Configuration
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0
    redis_password: Optional[str] = None
    redis_url: Optional[str] = None  # Alternative: full Redis URL

    model_config = {"env_file": ".env", "case_sensitive": False, "extra": "allow"}

    def get_hostaway_tokens(self) -> Dict[str, str]:
        """Parse Hostaway tokens from JSON string or fallback to space-separated format"""
        try:
            if not self.hostaway_tokens:
                logger.warning(
                    "HOSTAWAY_TOKENS environment variable is empty or not set"
                )
                return {}

            logger.debug(f"HOSTAWAY_TOKENS length: {len(self.hostaway_tokens)}")
            logger.debug(f"HOSTAWAY_TOKENS preview: {self.hostaway_tokens[:100]}...")

            # First try to parse as JSON
            try:
                tokens = json.loads(self.hostaway_tokens)
                logger.debug(
                    f"Successfully parsed {len(tokens)} tokens as JSON: {list(tokens.keys())}"
                )
                return tokens
            except json.JSONDecodeError:
                logger.debug(
                    "Failed to parse as JSON, trying space-separated format..."
                )

                # Fallback: try to parse space-separated format
                # Format: "HOSTAWAY_API_LONDON:token HOSTAWAY_API_PARIS:token ..."
                tokens = {}
                parts = self.hostaway_tokens.strip().split(" ")

                for part in parts:
                    if ":" in part:
                        key, value = part.split(":", 1)
                        tokens[key] = value

                if tokens:
                    logger.debug(
                        f"Successfully parsed {len(tokens)} tokens from space-separated format: {list(tokens.keys())}"
                    )
                    return tokens
                else:
                    logger.error("Could not parse tokens in any known format")
                    return {}

        except Exception as e:
            logger.error(f"Unexpected error parsing HOSTAWAY_TOKENS: {e}")
            logger.error(f"Raw value: {self.hostaway_tokens}")
            return {}

    def get_hostaway_token_for_city(self, city: str) -> Union[str, None]:
        """
        Get Hostaway token for specific city
        This method is now DEPRECATED - use TokenService instead
        Kept for backward compatibility but will use Token Management system
        """
        import asyncio
        from app.core.token_service import get_token_service

        # Use the new token service
        token_service = get_token_service()

        # Run async method in sync context
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # If we're already in an async context, create a task
                import concurrent.futures

                with concurrent.futures.ThreadPoolExecutor() as executor:
                    future = executor.submit(
                        asyncio.run, token_service.get_hostaway_token_for_city(city)
                    )
                    return future.result()
            else:
                # If no loop is running, we can use asyncio.run
                return asyncio.run(token_service.get_hostaway_token_for_city(city))
        except Exception as e:
            print(f"ERROR: Failed to get token from Token Management: {str(e)}")

            # Fallback to old method if Token Management fails
            tokens = self.get_hostaway_tokens()
            if not tokens:
                return None

            token_key = f"HOSTAWAY_API_{city.upper()}"

        print(
            f"DEBUG: Looking for token key '{token_key}' in available keys: {list(tokens.keys())}"
        )

        token = tokens.get(token_key)
        if token:
            print(f"DEBUG: Found token for {city} (length: {len(token)})")
        else:
            print(f"WARNING: No token found for city '{city}' with key '{token_key}'")
            print(f"WARNING: Available token keys are: {list(tokens.keys())}")

        return token


# Global settings instance
settings = Settings()
