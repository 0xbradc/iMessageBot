# iMessageManipulation
Using Python and Apple Script to send iMessages.



# Getting Started
1. Ensure you have Python3 (3.6+) installed.

2. Find your iMessage service ID with the following Applescript.
    ```
    tell application "Messages"
        get every account
    end tell
    ```

3. Copy and paste that service ID into the serviceID variable on line 12.

4. Navigate to the project's directory and run the following command.
    ```
    python3 iMessage.py
    ```
    
5. Input the desired message and phone number.
