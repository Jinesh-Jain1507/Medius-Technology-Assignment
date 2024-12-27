# My Approach to the Assignment: Automating Google Form Submission and Email Sending

## Overview
This project involves:

1. Automating the submission of a Google Form using Selenium.
2. Capturing a screenshot of the confirmation page.
3. Sending an email programmatically (via Django) with required attachments.

---

## Steps

### Step 1: Automating Google Form Submission

**Tools Used:** Python, Selenium, Chrome WebDriver, Django

1. **Environment Setup:**
   - Installed required libraries.
   - Used Chrome WebDriver with `webdriver-manager` to avoid manual WebDriver downloads.

2. **Code Implementation:**
   - Launched the Google Form using Selenium.
   - Located input fields using element `XPATH`.
   - Filled the input fields with suitable answers.
   - Clicked the submit button to finalize the form submission.
   - Captured a screenshot of the confirmation page using Selenium's `save_screenshot` method.

3. **Output:**
   - A screenshot of the confirmation page is saved as `confirmation_page.png`.

### Step 2: Sending Email Programmatically

**Tools Used:** Python, Django, SMTP

1. **Environment Setup:**
   - Configured Django project to send emails using Gmail's SMTP server.
   - Used environment variables to securely store email credentials.

2. **Code Implementation:**
   - Created a Django view to send an email with required attachments.
   - Attached the following files:
     - `confirmation_page.png`: Screenshot of the confirmation page.
     - `resume.pdf`: A sample resume.
   - Used `os` module to dynamically fetch file paths and attach them.

3. **Email Security:**
   - Used environment variables for email credentials (`EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD`).
   - Added `.env` file to `.gitignore` to prevent sensitive data from being pushed to version control.

4. **Output:**
   - An email is sent to the specified recipients with all required attachments.
