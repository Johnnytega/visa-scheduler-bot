# ✈️ Visa & Appointment Scheduler Bot

An automated bot designed to streamline the booking process for high-demand appointment slots (Visas, Medical, Consular services). Built with **Python** and **Selenium WebDriver**.

## ⚡ The Problem
Booking appointments for US/UK visas often requires refreshing the page for hours to catch a cancelled slot. This is inefficient and prone to human error.

## 🤖 The Solution
This bot acts as a "Headless Agent" that:
1.  **Auto-Logins** to the scheduling portal.
2.  **Monitors** availability in real-time.
3.  **Secures** the first available slot in the desired city (e.g., Lagos vs. Abuja).

## 🛠️ Tech Stack
* **Core:** Python 3.10+
* **Automation:** Selenium WebDriver (Chrome)
* **Manager:** `webdriver_manager` (Auto-updates browser drivers)

## 💻 Usage
```python
# Clone the repo
git clone [https://github.com/Johnnytega/visa-scheduler-bot.git](https://github.com/Johnnytega/visa-scheduler-bot.git)

# Install dependencies
pip install selenium webdriver-manager

# Run the bot
python visa_bot.py
