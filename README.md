This project extracts product data from a website and stores it in a database: 


Data Extraction : 
1. technicaltest.py: Python script that scrapes product data from the target URL (https://www.pascalcoste-shopping.com/esthetique/fond-de-teint.html) and extracting it into the json file "products.json".

2. Execution Environment: https://colab.research.google.com/drive/15bjbLFB3JR8pmObNq2g3oDaE7klFdXok?authuser=0#scrollTo=dO_RzaedCp70
 Output: JSON file named products.json containing the extracted data.

Docker Image :  
https://hub.docker.com/repository/docker/amenib/products_image/general :  Docker image available on Docker Hub (https://hub.docker.com/) containing the necessary dependencies for running the data processing script.

Data Processing
python/products.py: Python script that reads data from products.json, transforms it (if needed), and inserts it into a database. The script also prints the inserted data for verification.

Data Storage
python/products.json: JSON file containing the extracted product data.
