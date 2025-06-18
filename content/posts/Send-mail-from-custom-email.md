+++
title = "Send-mail-from-custom-email"
description = "Cloudflare Email Routing allows you to create custom email addresses that forward emails to your existing email account. This is useful for creating professional-looking email addresses without needing a separate email hosting service."
+++

# Sending mail from a custom email address

## Cloudflare Email Routing

Cloudflare Email Routing allows you to create custom email addresses that forward emails to your existing email account. This is useful for creating professional-looking email addresses without needing a separate email hosting service.

You can simply setup it without any issues, right fro cloudflare dashboard.

## Setting up Gmail to send from a custom email address

1. **Add your custom email address in Gmail**:

- Go to Gmail settings by clicking on the gear icon and selecting "See all settings".
- Navigate to the "Accounts and Import" tab.
- Under "Send mail as", click on "Add another email address".
- Enter your custom email address, check 'Treat it as alias' and click "Next Step".
- Set SMTP server to `smtp.gmail.com`, port to `587`, and use your Gmail credentials.
  - Gmail credentials are your Gmail email address and password.
  - This password can be obtained from your Google account settings under "Security" > "App passwords" if you have 2FA enabled.
- Leave the "Secured connection using TLS" option checked.
- Click "Add Account".
- A verification email will be sent to your custom email address. Click the verification link in that email to complete the setup.

> A tutorial link, <https://youtu.be/NmXWA08ly_s>

