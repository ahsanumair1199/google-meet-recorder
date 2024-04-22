from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from ..webdriver_config import driver_config
from ...constants.common import (
    GOOGLE_PASSWORD,
    GOOGLE_EMAIL,
    GOOGLE_MEET_LINK,
)
# END IMPORTS


async def join_meeting():
    driver = await driver_config()
    driver.get(GOOGLE_MEET_LINK)
    # SIGNIN FIRST TO GOOGLE ACCOUNT
    sign_in_btn = driver.find_element(
        By.XPATH, '/html/body/div[1]/c-wiz/div/div/div[24]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div/span/span')
    sign_in_btn.click()
    email_field = driver.find_element(By.NAME, "identifier")
    email_field.send_keys(GOOGLE_EMAIL)
    driver.find_element(By.ID, "identifierNext").click()
    while 1:
        try:
            password_field = driver.find_element(By.NAME, "Passwd")
            password_field.click()
            password_field.send_keys(GOOGLE_PASSWORD)
            password_field.send_keys(Keys.RETURN)
            break
        except (NoSuchElementException, ElementNotInteractableException):
            continue
    # GRANT PERMISSIONS TO BOT FROM BROWSER
    driver.execute_cdp_cmd(
        "Browser.grantPermissions",
        {
            "origin": GOOGLE_MEET_LINK,
            "permissions": ["geolocation", "displayCapture"]
        },
    )
    while 1:
        try:
            join_btn = driver.find_element(
                By.XPATH, '/html/body/div[1]/c-wiz/div/div/div[24]/div[3]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/button')
            join_btn.click()
            break
        except NoSuchElementException:
            continue
