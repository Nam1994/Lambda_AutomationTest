#I. Install Package 
    Import package in the requirement.txt include:
    + Install Selenium 
    + Install Allure pytest
    + Install Pytes

#II.How to download Driver
+ We can download driver Browser in the table:

|`Name Browser`  | `Driver  `           |          `Download    `                |                        
|-------------- |:------------------:|--------------------------------:     |
|<img src="https://cdn2.iconfinder.com/data/icons/social-media-8/512/Chrome.png" width="25" height="25" />        | `Chromedriver `    |[Link](ChromeDriver 93.0.4577.15)     |
| <img src="https://upload.wikimedia.org/wikipedia/commons/1/16/Firefox_logo%2C_2017.png" width="20" height="20" />       | `geckodriver `     |[Link](geckodriver-v0.29.1-win64.zip) |
| ...           |                    |                                      |
                                               
#How to run the test case:
     We will run the test case in Terminal:
        1.1 test_integration_page.py
        1.2 test_lambda_page_02.py

#How to run test  in Allure Reports
    We have to run the testcase.py and run allure application by command:
    Step 1: pytest -v -s Report/testcase.py
    Step 2: pytest -v -s allure="path_file_Reports"   Report/testcase.py   
    Step 3: allure serve path_file 
    
    



        
