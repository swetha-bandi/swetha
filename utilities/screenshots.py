import os
from datetime import datetime
from utilities.logger import Logger
import allure

class Screenshot:
   logger = Logger.get_logger()
   @staticmethod
   def take_screenshot(driver, test_name):
       screenshot_dir = "reports/screenshots"
       os.makedirs(screenshot_dir, exist_ok=True)
       timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
       filename = f"{test_name}_{timestamp}.png"
       filepath = os.path.join(screenshot_dir, filename)

       try:
           driver.save_screenshot(filepath)
           allure.attach.file(
               filepath,
               name=test_name,
               attachment_type=allure.attachment_type.PNG
           )
           Screenshot.logger.info(f"Screenshot saved to {filepath}")

       except Exception as e:
           Screenshot.logger.error(
               f"Failed to save screenshot: {e}"
           )

           raise

       return filepath









