import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

# CONFIGURATION
# For this demo, we use a practice automation site
TARGET_URL = "https://katalon-demo-cura.herokuapp.com/"
DESIRED_CITY = "Hongkong CURA Healthcare Center"  # The "Appointment" we want


def start_bot():
    print("🤖 Visa/Appointment Bot Initialized...")

    # Setup Chrome Options (Keep browser open after script ends)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # Automatically install/update the Chrome Driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # 1. Go to the Website
        print(f"network_log: Navigating to {TARGET_URL}")
        driver.get(TARGET_URL)
        time.sleep(2)  # Wait for load

        # 2. Click "Make Appointment"
        print("clicking: 'Make Appointment' button...")
        btn = driver.find_element(By.ID, "btn-make-appointment")
        btn.click()

        # 3. Handle Login (Demo Credentials)
        print("action: Entering Credentials...")
        time.sleep(1)
        driver.find_element(By.ID, "txt-username").send_keys("John Doe")
        driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
        driver.find_element(By.ID, "btn-login").click()

        # 4. Check for Availability (Dropdown Selection)
        print("status: Checking Appointment Slots...")
        time.sleep(2)

        # We select a facility (Simulating choosing "Lagos" vs "Abuja")
        facility_dropdown = driver.find_element(By.ID, "combo_facility")
        facility_dropdown.send_keys(DESIRED_CITY)

        # 5. Check "Apply for Readmission" (Simulating a visa option)
        driver.find_element(By.ID, "chk_hospotal_readmission").click()

        print(f"✅ SUCCESS: Slot found for {DESIRED_CITY}!")
        print("action: Bot is holding the page open for you.")

    except Exception as e:
        print(f"❌ Error: {e}")
        # driver.quit() # Uncomment to close on error


if __name__ == "__main__":
    while True:
        user_input = input("Type 'run' to start the bot (or 'q' to quit): ")
        if user_input.lower() == 'run':
            start_bot()
        elif user_input.lower() == 'q':
            break