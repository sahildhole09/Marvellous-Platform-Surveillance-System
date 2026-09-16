import smtplib
import os
from email.message import EmailMessage

def SendMail(FileName, ReceiverMail):
    try:
        SenderMail = "youremail@gmail.com"
        AppPassword = "your_16_character_app_password"

        msg = EmailMessage()

        msg["Subject"] = "Marvellous Platform Surveillance System Log File"
        msg["From"] = SenderMail
        msg["To"] = ReceiverMail

        msg.set_content(
            "Hello,\n\n"
            "Please see the attached Automated Platform Surveillance Log File.\n\n"
            "Regards,\n"
            "Sahil Ashok Dhole"
        )

        fobj = open(FileName, "rb")

        FileData = fobj.read()

        FileNameOnly = os.path.basename(FileName)

        msg.add_attachment(FileData,maintype="application",subtype="octet-stream",filename=FileNameOnly)

        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        #smtp.starttls()

        smtp.login(SenderMail, AppPassword)

        smtp.send_message(msg)

        smtp.quit()

        print("Email Sent Successfully.")

    except Exception as e:
        print("Unable to send email")
        print("Error :", e)