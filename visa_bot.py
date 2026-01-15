import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# --- CONFIGURATION ---
# We use a demo appointment site for this portfolio project.
# In a real scenario, you would swap this for the actual Visa Portal URL.
TARGET_URL = "https://katalon-demo-cura.herokuapp.com/" 
DESIRED_CENTER = "Hongkong CURA Healthcare Center" # Simulating "Lagos Visa Center"

def start_bot():
    print("🤖 Visa/Appointment Bot Initialized...")
    print("---------------------------------------")
    
    # Setup Chrome Options (Keeps the browser open after script finishes)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # Automatically install/update the Chrome Driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        # 1. Navigate to the Portal
        print(f"network_log: Navigating to {TARGET_URL}")
        driver.get(TARGET_URL)
        time.sleep(2) # Wait for page load

        # 2. Click "Make Appointment"
        print("action: Clicking 'Make Appointment' button...")
        btn = driver.find_element(By.ID, "btn-make-appointment")
        btn.click()
        
        # 3. Handle Login (Using Demo Credentials)
        print("action: Entering Secure Credentials...")
        time.sleep(1)
        driver.find_element(By.ID, "txt-username").send_keys("John Doe")
        driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
        driver.find_element(By.ID, "btn-login").click()
        
        # 4. Check for Availability (Dropdown Selection)
        print("status: Checking Appointment Slots...")
        time.sleep(2)
        
        # Select the specific facility (Simulates choosing "Lagos" vs "Abuja")
        facility_dropdown = driver.find_element(By.ID, "combo_facility")
        facility_dropdown.send_keys(DESIRED_CENTER)
        
        # 5. Select Options (Simulating 'Apply for Readmission')
        driver.find_element(By.ID, "chk_hospotal_readmission").click()
        
        # 6. Success Message
        print(f"✅ SUCCESS: Slot found for {DESIRED_CENTER}!")
        print("action: Bot is holding the page open for user review.")

    except Exception as e:
        print(f"❌ Error: {e}")
        # driver.quit() # Uncomment this if you want it to close automatically on error

if __name__ == "__main__":
    # Interactive Loop
    while True:
        user_input = input("\nType 'run' to start the bot (or 'q' to quit): ")
        if user_input.lower() == 'run':
            start_bot()
        elif user_input.lower() == 'q':
            print("Exiting Bot. Goodbye.")
            break
