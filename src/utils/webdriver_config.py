import undetected_chromedriver as uc
from ..constants.common import WEBDRIVER_LOG_PATH
# END IMPORTS


async def driver_config():
    # WEBDRIVER CONFIGURATION
    options = uc.ChromeOptions()
    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-application-cache')
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = uc.Chrome(service_log_path=WEBDRIVER_LOG_PATH,
                       use_subprocess=False, options=options, version_main=120)
    return driver
