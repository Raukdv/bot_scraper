# What is this shit?
This bot is used to scrape products from third party sites, download images, rename them according to csv files.
Create csv report files and generate wordpress type urls according to your upload path which is: https://domain.com/wp-content/uploads/2023/01/generate_img.extension
The downloaded images will be displayed in a file with the name of the product code that will be found (generated) in the root/contentino path.

You should be able to see in "contenido" the folder with the product code name like this: 

    itemcode

      img.extension

      img-1.extension

      img-2.extension

      img-n.extension

      MainBath.csv

      ReportBath.csv

# Requeriments

Python >= 3.8

Chrome ver 91.0.4472.77 for the driver given. 

do not use any version above 95 and below 90.

# bot_scraper
This bot use command line and auto setup.

# Install
In the root folder; python setup.py

# Run bot
bot porch

# Process
The following bot requires a csv with the following dictionary-like format.

itemcode
itemname	
urlimg

The image name will depend on the value in the upload csv called itemname. Names without special characters, and only with spaces and/or all together are recommended:
Example: 
My Image Is Cool

myimagenescool

this bot is used to scrape product images. 
Note that it requires a product code (it can be any to track the report) the product name and the url where the product is presented.
This bot is based on a specific page but you can change its selection in the following file: bot/porch/selenium.py from line 105 to 110.

In this case there is:

    try:
      elements = self.get_elements(
      By.CSS_SELECTOR, '.fotorama__img'
      )
    except:
        elements = None
    
the next value in the get_elements() its the css class for point the method try find the exacts values. So say it like this you just need to inspect the page and try
find the correct way for '.fotorama__img'

# Other files:
.env

bot\config.py

You can config your init values in here and you have to set to in bot/config.py

# .env values
This bot use this values in .env to run:

DOMAIN_PATH = 'https://wordpress-domain/wp-content/uploads/2023/01/'

CSV_NAME = 'filename.csv'

# bot/config.py
DOMAIN_PATH = os.getenv('DOMAIN_PATH', '')

CSV_NAME = os.getenv('CSV_NAME', '')

this os.getenv come from .env

# DO NOT CHANGE ANY OTHER VALUE IN bot/config.py
Note that there are other values that the bot uses such as time out or attempts.
Do not change these values unless you know how selenium will respond.

Some inherited BaseSelenium method such as get_elements() may not return anything if you remove or change them.

# final :D
  
That said, i may change the syntax of certain parts without changing the final result.
Have a nice scraper :)
