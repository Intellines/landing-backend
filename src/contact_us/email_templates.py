contact_us_email = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width" />
  <title>Contact Us</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: 'Arial', sans-serif;
      background-color: #f8f9fa;
    }
    .container {
      max-width: 600px;
      margin: 0 auto;
      background-color: #ffffff;
      padding: 40px 30px;
      border-radius: 8px;
      text-align: left;
    }
    h1 {
      font-size: 20px;
      margin-bottom: 20px;
      color: #121212;
    }
    p {
      font-size: 15px;
      line-height: 1.6;
      color: #333333;
      margin-bottom: 16px;
    }
    a.custom-link {
      color: #121212;
      text-decoration: none;
      background-color: #f2f2f2;
      padding: 3px 6px;
      border-radius: 4px;
      font-weight: 500;
    }
    a.custom-link:hover {
      background-color: #e0e0e0;
    }
    .footer {
      text-align: center;
      font-size: 12px;
      color: #888;
      margin-top: 40px;
    }
    .contact-details {
      margin-bottom: 20px;
      text-align: center;
    }
    .contact-details a {
      color: #666666;
      text-decoration: none;
      font-weight: bold;
      display: inline;
      margin: 0 4px;
      font-size: 14px;
    }
    .contact-details .separator {
      color: #666666;
      margin: 0 4px;
      font-size: 14px;
    }
    .social-icons {
      margin-top: 20px;
      text-align: center;
    }
    .social-icons a {
      display: inline-block;
      margin: 0 8px;
    }
    .social-icons img {
      width: 24px;
      height: 24px;
      vertical-align: middle;
    }
    .contact-table {
      width: 100%;
      max-width: 400px;
      border-collapse: collapse;
      margin-top: 10px;
      margin-bottom: 20px;
    }
    .contact-table td {
      vertical-align: top;
      padding: 6px 8px;
      font-size: 15px;
      color: #333;
    }
    .contact-label {
      font-weight: bold;
      width: 80px;
      white-space: nowrap;
    }
    @media only screen and (max-width: 600px) {
      .container {
        padding: 20px 15px;
      }
    }
  </style>
</head>
<body>
  <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #f8f9fa;">
    <tr>
      <td align="center" style="padding: 40px 20px;">
        <div class="container">
          <div style="text-align: center; margin-bottom: 30px;">
            <img src="https://intellines.retool.com/api/file/1a20e7fa-04e5-43ab-9b69-2710d161514d" alt="Intellines Logo" style="max-width: 300px;" />
          </div>

          <hr style="border: none; border-top: 1px solid #ccc; margin: 30px 0;" />

          <h1>Thank You for Contacting Us</h1>
          <p>Hello {{ startTrigger.data.name }}!</p>

          <p>
            We've received your message and will get back to you shortly.
          </p>

          <p>We appreciate your interest in Intellines.</p>

          <p style="margin-top: 30px;">Best regards,<br />Intellines team</p>

          <hr style="border: none; border-top: 1px solid #ccc; margin: 30px 0;" />

          <div class="contact-details">
            <a href="mailto:intellines.company@gmail.com">intellines.company@gmail.com</a>
            <a href="tel:+380935696518">+380 93 569 6518</a>
          </div>

          <div class="social-icons">
            <a href="https://x.com/intellines_" target="_blank">
              <img src="https://intellines.retool.com/api/file/f23336a0-c80c-42ee-a899-185fe9b48d1d" alt="X.com" style="width: 28px; height: 28px;" />
            </a>
            <a href="https://linkedin.com/company/intellines" target="_blank">
              <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="24" height="24" />
            </a>
            <a href="https://wa.me/+380935696518" target="_blank">
              <img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" alt="WhatsApp" width="24" height="24" />
            </a>
            <a href="https://t.me/intellines" target="_blank">
              <img src="https://cdn-icons-png.flaticon.com/512/2111/2111646.png" alt="Telegram" width="24" height="24" />
            </a>
          </div>

          <div class="footer">
            © 2025 Intellines
          </div>
        </div>
      </td>
    </tr>
  </table>
</body>
</html>
"""
