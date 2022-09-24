# Python Automation Framework 

Automation BDD/Hybrid framework build using [Behave](https://behave.readthedocs.io/en/stable/), [Selenium](https://selenium.dev/),[Appium](appium.io/),[Requests](https://requests.readthedocs.io/en/latest/).
Framework is used for Web & Mob applications automation testing with Browserstack. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install framework.

```bash
pip install -r requirements.txt
```

## Usage
Using Python with allure reporting:
```python
behave -f allure -o output/allure_report
```
Using commandl ine Bash
```bash
chmod 777 ./run.sh
./run.sh
```

## Feature List to added
- [ ] Live logging
- [ ] update shell : "install.sh"
- [ ] Docs
- [ ] API Automation testing using [Requests](https://requests.readthedocs.io/en/latest/)
- [ ] More improvements to added, soon !!


## Project structure
~~~
├Root
├───config              # Web and mobile devcies capabilites
├───drivers             # Common driver gecko, chrome, etc drivers
├───features            # BDD Gherkins feaure files
│   ├───features        
│   └───steps           # Steps Def as features
├───output
│   ├───allure_report   # allure report
│   ├───downloads        # any downloads
│   ├───logs
│   └───screenshots     # screen shots while test executions
├───page_objects        # POM Models
│   ├───core
│   │   ├───api         # API python moduels soo to be updated
│   │   ├───mob         # Mobile moudels classes 
│   │   ├───web         # Web browsers module classes
│   │ 
│   ├───helper          # utils helper functions - read Json, Csv, browser interaction helper functions
│   └───locators        # Mobile & Web application locators: Supported format -> Json, Py class.
├───test_data           # test data for continuous testing using json, excel.
└───utils

~~~

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
