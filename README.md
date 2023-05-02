
# otp_verification_python
The code provided is a Python script for a simple OTP (One-Time Password) verification application. It uses the Twilio API to send an OTP via SMS to the user's phone number.

The user enters the OTP into a text field in the GUI, and the code validates the OTP. If the OTP is correct, the application displays a "Login Success" message. If the OTP is incorrect or invalid, the application displays a "Wrong OTP" or "Invalid OTP" message, respectively.

The application also includes a "RESEND OTP" button that allows the user to request a new OTP via SMS. An OTP expires after 20 seconds, and a timer is displayed in the GUI to indicate the time remaining until the OTP expires.

Overall, this code provides a basic framework for OTP verification in a Python application using the Twilio API.


## Prerequisites
- Twilio Account SID and Auth Token.
- Python 3.x.
- Required modules:
    `twilio`
    `tkinter`


    
## Description



| Function |  Description                |
| :-------- |  :------------------------- |
| `otp_verifier()` |  Constructor that initializes the GUI window, generates a random OTP, and sends it via Twilio API. |
| `Labels()` |  Creates labels for the GUI window, including the title and the "Resend OTP" message. |
| `clear_text()` |  Clears the text in the User_Name field. |
| `Entry()` | Creates the User_Name field where the user enters the OTP. |
| `Buttons()` | Creates the "Submit" and "Resend OTP" buttons for the GUI window. |
| `callback()` |  Displays a message box to confirm that a new OTP has been sent via Twilio API. |
| `checkOTP()` |  	Checks if the user input matches the generated OTP and displays an appropriate message. |
| `resendOTP()` |  Generates a new OTP and sends it via Twilio API. |
| `update_time(t)` |  Updates the timer for the OTP validity and displays a message box if the OTP has expired. |





## Run Locally

- Clone the repository or download the zip file.



- Install the required modules using the following command:

```bash
  pip install twilio tkinter
```

- Open the .py file in an IDE or a text editor.


- Replace the following lines with your Twilio Account SID and Auth Token:

```bash
  self.client = Client("AC343e7570357ba769847f695f2c89d63a", "a5c5706200923411b3c6bf38c828b277")
```
- Replace the following line with your phone number to receive the OTP:

```bash
  self.client.messages.create(to=["+919833xxxxxx"],from_="+91705xxxxxxx", body=self.n)
```
- Save the changes and run the .py file.
## Usage

- After running the code, a GUI window will appear.
- Enter the OTP received on your phone in the text box.
- Click the Submit button to verify the OTP.
- If the OTP is correct, a message box will appear saying "Login Success".
- If the OTP is incorrect, a message box will appear saying "Wrong OTP".
- If you didn't receive the OTP or the OTP has expired, click the Resend OTP button to receive a new OTP.

```bash
 Note: The OTP will expire after 20 seconds. You can change the time by changing the parameter passed to the update_time() function in the last line of the code.
```

