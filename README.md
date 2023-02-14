# printmail
Automation Script to Login, Navigate, Take Screenshot and Send Email

This script automates the process of logging into a web platform, navigating to a specific page, taking a screenshot, and sending the screenshot via email.

Requirements
- Selenium
- Win32com
- Python 3
- Dotenv

Usage
- Clone or download this repository.
- Create a .env file in the root directory and add the following information:
    LOGIN=<Your Web Platform Login>
    PASSWORD=<Your Web Platform Password>
    SENDMAIL=<Email to send the screenshot to>
- Fill in the necessary information in the code, including the web platform link, login ID, password ID, page URL, screenshot folder path, email subject, email body, and success message.
- Install the necessary packages with pip install -r requirements.txt.
- Run the script with prefered tool.

Explanation
 - The script starts by loading the environment variables from the .env file using the load_dotenv() function from the dotenv library. The environment variables are then used to store the login credentials, email address, and other information required for the script.
 - Next, the script opens the web driver using the webdriver.Edge() function from the selenium library and navigates to the web platform using the driver.get() function. It then waits for the login input to load and fills in the login and password information.
 - After logging in, the script navigates to the desired page and takes a screenshot using the driver.save_screenshot() function. The screenshot is then attached to an email using the win32com library and sent to the specified recipient.
 - Finally, the script closes the web driver and prints a success message.

Note
This script is written using the Edge web driver and Microsoft Outlook. If you're using a different web driver or email client, you'll need to make appropriate changes to the code.
