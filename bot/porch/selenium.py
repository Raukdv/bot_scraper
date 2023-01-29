import requests as r
import csv
import os
import shutil

from selenium.webdriver.common.by import By

from ..base.selenium import BaseSelenium
from .. import config

class PorchSelenium(BaseSelenium):
    def __init__(self, *args, **kwargs):
        self.DOMAIN_CREATOR = config.DOMAIN_PATH
        self.counter = 0
        self.bath = []
        self.main = []
        self.codeitem = ''

        super().__init__(*args, **kwargs)

    def __call__(self):
        try:
            return self.handle()
        except Exception as err:
            print(err)
            self._wait(10)
        finally:
            self.quit_driver()

    def handle(self):
        self.do_scraper()

    def move_file_to_folder(self):
        listdir = os.listdir('contenido')
        #if self.codeitem in listdir: listdir.remove(self.codeitem)
        #Create a folder with codeitem
        print(f'Creando carpeta contenedora de imagenes para {self.codeitem}')
        path_folder = 'contenido/'+self.codeitem
        os.mkdir(path_folder)

        #move aech file to the new path
        print(f'Moviendo imagenes a {self.codeitem}')
        for img in listdir:
            img_path = 'contenido/'+img
            isFile = os.path.isfile(img_path)
            if isFile:
                shutil.move(img_path, path_folder+'/'+img)
    
    def write_main_csv(self):
        #MAIN CSV GENERATOR
        print("Creando CSV de reporte principal")
        csvfile = open('contenido/'+self.codeitem+'/MainReport.csv', 'w', newline='')
        fieldnames = ['Code', 'NameGenerate', 'Url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for data in self.main:
            writer.writerow(data)
        self.main.clear()
        csvfile.close()

    def write_bath_csv(self):
        #BATH CSV GENERATOR
        print("Creando CSV de reporte de muestra")
        csvfilebath = open('contenido/'+self.codeitem+'/ReportBath.csv', 'w', newline='')
        fieldnamesbath = ['Batch']
        writerbath = csv.DictWriter(csvfilebath, fieldnames=fieldnamesbath)
        writerbath.writeheader()
        bath = ', '.join(self.bath)
        writerbath.writerow({'Batch':bath,})
        self.bath.clear()
        csvfilebath.close()
    
    def write_product_csv(self):
        #MAIN CSV GENERATOR
        print("Creando CSV de reporte principal")
        csvfile = open('contenido/'+self.codeitem+'/MainReport.csv', 'w', newline='')
        fieldnames = ['Code', 'NameGenerate', 'Url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for data in self.main:
            writer.writerow(data)
        self.main.clear()

    #Main process
    def do_scraper(self):
        csvfile = open(config.CSV_NAME, newline='')
        reader = csv.DictReader(csvfile)
        
        #Product
        for row in reader:

            self.codeitem = row.get('itemcode', 'None')
            url = row.get('urlimg', 'None')
            product = row.get('itemname', 'None')
            productname = product.replace(' ', '-')

            print(f'Checking product: {self.codeitem} :: {product}')

            self.driver = self.get_driver(size=(1200, 700))
            self.driver.get(url)
            self._wait(2)
            #This is the get items process
            try:
                elements = self.get_elements(
                    By.CSS_SELECTOR, '.fotorama__img'
                )
            except:
                elements = None
            
            #Image
            if elements:
                for element in elements:
                    #Counter and batch for img wordpress list
                    link = element.get_attribute('src')
                    self.counter +=1
                    #Format name -> image.jpg, image-1.jpg, image-2.jpg....
                    #image.jpg are the main img in the list
                    if self.counter == 1:
                        NAME_HOLDER_REPLACED = productname+config.EXTENSION
                        DOMAIN_URL_IMAGE = self.DOMAIN_CREATOR+NAME_HOLDER_REPLACED
                    elif self.counter == 2:
                        NAME_HOLDER_REPLACED = productname+'-1'+config.EXTENSION
                        DOMAIN_URL_IMAGE = self.DOMAIN_CREATOR+NAME_HOLDER_REPLACED
                    else:
                        NAME_HOLDER_REPLACED = productname+'-'+str(self.counter-1)+config.EXTENSION
                        DOMAIN_URL_IMAGE = self.DOMAIN_CREATOR+NAME_HOLDER_REPLACED
                    
                    #Create main and batch data
                    self.main.append({
                            'Code':self.codeitem, 
                            'NameGenerate':NAME_HOLDER_REPLACED, 
                            'Url':DOMAIN_URL_IMAGE
                        })
                    self.bath.append(DOMAIN_URL_IMAGE)
                    
                    self._wait(2)
                    print(f'Descargando imagen de: {link}')
                    imgcontent = r.get(link).content
                    #Open and close the file
                    content = open('contenido/'+NAME_HOLDER_REPLACED, 'wb')
                    content.write(imgcontent)
                    content.close()

                #Sub process for each product scraped
                self.counter = 0
                self._wait(2)
                self.move_file_to_folder()
                self.write_main_csv()
                self.write_bath_csv()

            else:
                print("Nothing to check") 