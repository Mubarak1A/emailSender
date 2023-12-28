# Email Sender Script

This Python script automates the process of sending emails to a list of recipients using the SMTP protocol. The script is designed to establish a connection with an SMTP server, create an email message, and send it to multiple recipients.

## Usage

1. **Clone Script Repo:**
    ```git clone https://github.com/Mubarak1A/emailSender.git```

2. **Update Email List:**
   Populate the `emails` list in the script with the email addresses of the recipients to whom you want to send emails and that of the sender.

3. **HTML Content:**
   Customize the content of the HTML email by modifying the `sample.html` file. The script reads the content from this file and substitutes a variable (e.g., `name`) with a specified value.

4. **Run the Script:**
   Execute the script using the following command:

   ```bash
   python3 send_mail.py
   ```

## Script Overview

The script follows these key steps:

1. **Read HTML Content:**
   The HTML content for the email is read from the `sample.html` file using the `pathlib` module.

2. **Email Configuration:**
   The script configures the email message using the `EmailMessage` class. Sender information, recipient email, and email subject are set.

3. **SMTP Connection:**
   The script establishes a connection with the SMTP server (in this case, Gmail's SMTP server) using the `smtplib` module.

4. **Sending Emails:**
   For each email in the `emails` list, the script sends an email with the configured content.

5. **Print Status:**
   The script prints a success message for each email sent.

## Requirements

- Python 3
- `smtplib` (standard library)
- `email.message` (standard library)
- `string.Template` (standard library)
- `pathlib` (standard library)

Note: Ensure that the SMTP server specified in the script allows the provided sender email to send emails. Additionally, be cautious when handling sensitive information and consider using secure methods for storing and retrieving credentials.

Feel free to customize the script according to your specific use case and email content requirements.
