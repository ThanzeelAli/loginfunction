from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def login(url, valid_usernames, valid_passwords, invalid_usernames, invalid_passwords):
    driver = webdriver.Chrome("C:\chromedriver_win32 (2)\chromedriver.exe")
    driver.get("https://app.vwo.com/#/login")

#login with valid credentials
    for i in range(len(valid_usernames)):
        try:
            username_field = driver.find_element(By.ID,"login-username")
            password_field = driver.find_element(By.ID,"login-password")
            username_field.send_keys(valid_usernames[i])
            password_field.send_keys(valid_passwords[i])
            driver.find_element(By.XPATH,"//button[@type='submit']").click()

            driver.implicitly_wait(10)

            # Verify the login was successful
            if driver.current_url == "https://app.vwo.com/#/login":
                # Login successful
                print(f"Login successful with valid credentials: {valid_usernames[i]} / {valid_passwords[i]}")
            else:
                # Login failed
                print(f"Login failed with valid credentials: {valid_usernames[i]} / {valid_passwords[i]}")

        except NoSuchElementException:
            # Login form not found
            print("Login form not found.")

        finally:
            # Go back to the login page
            driver.get("https://app.vwo.com/#/login")

#login with invalid credentials
    for i in range(len(invalid_usernames)):
        try:
            # Enter the invalid username and password in the login form
            username_field = driver.find_element(By.NAME,"username")
            password_field = driver.find_element(By.NAME,"password")
            username_field.send_keys(invalid_usernames[i])
            password_field.send_keys(invalid_passwords[i])

            driver.find_element(By.XPATH,"//button[@type='submit']").click()

            driver.implicitly_wait(10)

            # Verify the login failed
            if driver.current_url == "https://app.vwo.com/#/login":
                # Login failed
                print(f"Login failed with invalid credentials: {invalid_usernames[i]} / {invalid_passwords[i]}")
            else:
                # Login successful
                print(f"Login successful with invalid credentials: {invalid_usernames[i]} / {invalid_passwords[i]}")

        except NoSuchElementException:
            # Login form not found
            print("Login form not found.")

        finally:
            driver.get("https://app.vwo.com/#/login")

    driver.quit()
