# Automated Testing Samples: Python + Selenium  
**A collection of practical examples for web automation testing using Selenium WebDriver and Python.**  

## Technologies  
- **Language:** Python 3.13  
- **Framework:** Selenium WebDriver  
- **Package Management:** `requirements.txt`  
- **Virtual Environment:** [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)  (recommended)

## Project Structure  

| Folder | Description | Link |  
|--------|-------------|------|  
| **Browser Navigation** | Examples of browser navigation (back, forward, refresh). | [View Folder](./browser_navigation_control) |  
| **Browser Options** | Configuring Chrome options and page load strategies. | [View Folder](./browser_options_and_page_loading_strategy) |  
| **Waits & Expectations** | Implicit/Explicit waits and synchronization. | [View Folder](./explicit_and_implicit_expectations) |  
| **Data Validation** | Extracting and validating browser data. | [View Folder](./getting_data_from_the_browser_and_validating_it) |  
| **ChromeDriver Setup** | ChromeDriver initialization examples. | [View Folder](./initializing_Chrome_driver) |  
| **Element Locators** | Finding elements using various methods. | [View Folder](./search_web_elements) |  
| **File Handling** | Uploading/downloading files with Selenium. | [View Folder](./uploading_and_downloading_files) |  
| **Input Fields** | Working with forms and input elements. | [View Folder](./working_with_input_fields) |  
| **XPath Locators** | Advanced element location using XPath. | [View Folder](./Xpath_locators) |  

## Setup Instructions  

### 1. Clone the Repository  
```bash
git clone https://github.com/MarinaTomenko/automated-testing-samples-python-selenium.git
```
### 2. Set Up Virtual Environment
```bash
cd automated-testing-samples-python-selenium
python -m venv venv
# For Linux/Mac:
source venv/bin/activate
# For Windows:
.\venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run Tests
Example for input fields tests:
```bash
cd working_with_input_fields
python click_example.py
```
## Useful Links  
- [Selenium Python Documentation](https://selenium-python.readthedocs.io/)  
- [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)  
 