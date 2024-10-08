from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)
    API_KEY: str

    MIN_AVAILABLE_ENERGY: int = 100
    SLEEP_BY_MIN_ENERGY: list[int] = [1000, 1800]

    ACTIVATE_TURBO_TAPS: bool = True
    ADD_TAPS_ON_TURBO: int = 2500

    AUTO_UPGRADE: bool = True
    MAX_LEVEL: int = 26

    BALANCE_TO_SAVE: int = 1000000
    UPGRADES_COUNT: int = 10

    APPLY_DAILY_ENERGY: bool = True
    APPLY_DAILY_TURBO: bool = True

    RANDOM_TAPS_COUNT: list[int] = [10, 50]
    SLEEP_BETWEEN_TAP: list[int] = [10, 25]
    
    MAX_AUTO_UPGRADE_BOOST: int = 20

    USE_RANDOM_USERAGENT: bool = False

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()
