# Python-Automania

> Python Automation framework based on python using selenium, appium, behave.


### Framework file structure
```
├───config                  # devices, web, browserstack capabilites
├───drivers                 # chrome, gecko & others divers
├───features                
│   ├───core
│   │   ├───mob             # mobile scripts files
│   │   └───web             # web browser scripts files
|   |───features            # BDD feature files
│   ├───helper              # helper functions e.g. custom wait, drivers
│   ├───locators            # locators json
│   └───steps               # BBD step definitions
├───output
│   ├───allure_report       # allure reports
│   ├───downloads           # download-able files
│   ├───logs                # logs
│   └───screenshots         # any screen shots saved during test
├───page object             # TO BE REMOVED
│   └───locators    
└───utils                   # utils scripts
|___README.MD
```

