# What is this shit?
This bot is used to scrape products from third party sites, download images, rename them according to csv files.
Create csv report files and generate wordpress type urls according to your upload path which is: https://domain.com/wp-content/uploads/2023/01/generate_img.extension
The downloaded images will be displayed in a file with the name of the product code that will be found (generated) in the root/contentino path.

You should be able to see the following in the file whose name is when finished the process: 
itemcode
  img.extension
  img-1.extension
  img-2.extension
  img-n.extension
  MainBath.csv
  ReportBath.csv 

# bot_scraper
This bot use command line and auto setup.

# Install
In the root folder; python setup.py

# Run bot
bot porch

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
This bot is based on a specific page but you can change its selection in the following file: bot\porch\selenium.py from line 86 to 91.

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

You can config your init values in here and you have to set to in bot\config.py

# .env values
This bot use this values in .env to run:
DOMAIN_PATH = 'https://wordpress-domain/wp-content/uploads/2023/01/'
CSV_NAME = 'filename.csv'

# bot\config.py
DOMAIN_PATH = os.getenv('DOMAIN_PATH', '')
CSV_NAME = os.getenv('CSV_NAME', '')
this os.getenv come from .env  

That said, i may change the syntax of certain parts without changing the final result.
Have a nice scraper :)
