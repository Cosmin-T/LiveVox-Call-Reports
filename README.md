# LiveVox-Call-Reports

**IMPORTANT:** This serves as an informative repository with no need for installation, as there is no `config.ini` file, and the automation is designed for a specific website inaccessible to anyone.

## Description

This Python script automates the process of retrieving and processing inventory data from a website using Selenium WebDriver and Excel.

## Modules

### util.py

- Contains various constants and utility functions used throughout the script.
- Defines constants for URLs, file paths, and other configuration parameters.

### webdriver.py

- Initializes a headless Chrome WebDriver using Selenium.
- Navigates to a specified URL.
- Handles exceptions and logs errors.
- Returns the WebDriver instance for further use.

### login.py

- Provides functions for logging into the website.
- Uses Selenium to fill in login credentials and click the login button.
- Logs login-related actions and errors.

### dates.py

- Manipulates dates and updates date fields on the website.
- Retrieves the current date and manipulates it.
- Logs date-related actions and errors.

### navigation.py

- Implements navigation and data retrieval functions.
- Uses Selenium to interact with web elements and retrieve data.
- Defines variables and XPaths for data processing.
- Logs navigation-related actions and errors.

### downloads.py

- Handles the download of files from the website.
- Uses Selenium to locate and click the download button.
- Logs download-related actions and errors.

### process.py

- Processes the downloaded data and generates reports.
- Reads data from downloaded text files.
- Filters and exports data to Excel files.
- Logs processing actions and errors.

### send_email.py

- Sends email notifications with attached reports.
- Configures email content and attachments.
- Sends emails using SMTP.
- Logs email sending actions and errors.

### logs.py

- Configures and initializes the logging system.
- Sets the log level, format, and log file path.
- Used to log actions and errors throughout the script.

### config_ini.py

- Reads configuration settings from an INI file.
- Provides a function to access the configuration settings.

## Main Script

### main.py

- Orchestrates the execution of the script.
- Imports and utilizes modules to perform the following tasks:
  1. Initializes the Chrome WebDriver.
  2. Logs into the website.
  3. Navigates to the relevant web pages.
  4. Retrieves and updates inventory data.
  5. Closes the WebDriver.

## Configuration

The script relies on configuration settings stored in an INI file (`config.ini`). The configuration includes:

- URL for the website.
- Chrome WebDriver executable path.
- Login credentials.
- XPaths for login elements.
- XPaths for navigation elements.
- File paths for reports.
- Logging settings (log level and log file path).
