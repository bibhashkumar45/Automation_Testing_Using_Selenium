Automation Testing Using Selenium

Automated test scripts for the OrangeHRM demo login page using Python and Selenium WebDriver. The tests run on a single browser and across multiple browsers (Chrome, Firefox, Edge) to check cross-browser behavior.

Site under test: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

Test Scenarios
#	Scenario	Expected Result
1	Login with valid username and password	User is redirected to the Dashboard
2	Login with invalid username and/or password	"Invalid credentials" error is shown
3	Login with empty username and/or password	"Required" message is shown under the empty field(s)
4	Click the "Forgot your password?" link	Reset Password page opens
Cross-Browser Testing

The script cross_browser.py runs the same login test scenarios on multiple browsers one after another, to make sure the login page behaves the same everywhere.

Browser	Status
Google Chrome	Tested
Mozilla Firefox	Tested
Microsoft Edge	Tested
The same test steps are reused for every browser, only the WebDriver changes.
Each browser run checks: valid login, invalid login, empty fields and the Forgot Password link.
Any difference in behavior between browsers (page load, error messages, layout) is noted as a cross-browser issue.
Tech Stack
Python 3.x
Selenium WebDriver
Browsers: Google Chrome, Mozilla Firefox, Microsoft Edge
Project Structure
Automation_Testing_Using_Selenium/
├── main.py            # Main script - runs the login tests on a single browser
├── test.py            # Test cases for the login page
├── testing.py         # Additional test script / practice tests
├── cross_browser.py   # Runs the login tests on Chrome, Firefox and Edge
└── README.md

Update the one-line comments above to match what each file actually does.

Setup and Installation
Clone the repository
bash
   git clone https://github.com/bibhashkumar45/Automation_Testing_Using_Selenium.git
   cd Automation_Testing_Using_Selenium
Install Selenium
bash
   pip install selenium
Make sure the browsers you want to test (Chrome, Firefox, Edge) are installed. Selenium 4.6+ downloads the matching browser drivers automatically.
How to Run

Single browser test

bash
python main.py

Cross-browser test (Chrome, Firefox, Edge)

bash
python cross_browser.py
What I Learned
Locating web elements using ID, XPath and CSS selectors
Using explicit waits for stable tests
Writing positive and negative test cases
Running the same tests across different browsers
Future Improvements
Add PyTest and an HTML test report
Use the Page Object Model (POM) for cleaner code
Add screenshots on test failure
Add more modules (PIM, Leave, Admin)
Related Work

This project is the automation part of my OrangeHRM login page testing. The manual test cases and bug report are in a separate document: Manual Testing - Google Drive

Author

Bibhash Kumar B.E. Computer Science Engineering, Chandigarh University GitHub | bibhashkumar4587@gmail.com
