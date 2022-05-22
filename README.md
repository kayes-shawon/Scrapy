# Product Scrapy 
-----------------------------------

# Local project setup
1. Use virtual environment for setting up
2. Activate virtual environment
3. Install pip requirements
```
pip3 install -r requirements.txt
```
4. create postgres database
5. Create .env file. Example .ci_env has been provided.
```
cp .ci_env .env
```
6. Update .env file according to the system
7. run following commands for migrations related issues.
```
python manage.py migrate
```
8. Once all of the above command run sucessfully, We are ready to go. Start server by executing command.
```
make run
```
-------------------------------
### Async Setup
-------------------------------
1. Install Redis as a Celery “Broker
2. Open other terminal and run worker
```
make celery
```
