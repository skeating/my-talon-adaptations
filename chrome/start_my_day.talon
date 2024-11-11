app: chrome
-
tag(): browser
tag(): user.tabs


open calo plast:
    app.window_open()
    browser.go("https://sharedprweaadb2c.b2clogin.com/e43ba4d8-e1cd-4145-84d1-29498cef4324/B2C_1_charter_si1/oauth2/v2.0/authorize?client_id=f77bf614-60f9-4cf7-93c5-f345dd0a76ec&response_type=code%20id_token&scope=https%3A%2F%2Fsharedprweaadb2c.onmicrosoft.com%2Fb5c2de6c-ed59-456f-bea4-86f5948af3c8%2FFunctions.ReadWrite%20openid%20offline_access&redirect_uri=https%3A%2F%2Fwww.coloplastcharter.co.uk%2Fapi%2Foidc-aadb2c-consumer-reply&state=%2Fmy-account%2F&response_mode=form_post&ui_locales=en-GB&GTMID=GTM-KFW86MF&multisite_origin=https%3A%2F%2Fwww.coloplastcharter.co.uk%2F%3Faccountregistrationtype%3DTopNavigation.")

start my day:
    app.window_open()
    browser.go("https://outlook.office.com/mail/")
    app.window_open()
    browser.go("https://outlook.office.com/calendar/")
    app.window_open()
    browser.go("https://uclrsdt.harvestapp.com/time")
    app.window_open()
    browser.go("https://otter.ai/home")
    app.window_open()
    browser.go("https://mail.google.com/mail/u/0/?ogbl#inbox")

start finance:
    app.window_open()
    browser.go("https://docs.google.com/spreadsheets/d/1QaNxBMIo3GQmxjRvEY9_kqrWzvy92fcd/edit?gid=1252592722#gid=1252592722")   
    app.window_open()
    browser.go("https://www.onlinebanking.natwest.com/Default.aspx")
    app.window_open()
    browser.go("https://online.mbna.co.uk/personal/logon/login.jsp*")


open male:
    app.window_open()
    browser.go("https://outlook.office.com/mail/")
    
open calendar:
    app.window_open()
    browser.go("https://outlook.office.com/calendar/")

open time sheet:
    app.window_open()
    browser.go("https://uclrsdt.harvestapp.com/time")

open otter:
    app.window_open()
    browser.go("https://otter.ai/home")

open google mail:
    app.window_open()
    browser.go("https://mail.google.com/mail/u/0/?ogbl#inbox")

open personal time sheet:
    app.window_open()
    browser.go("https://docs.google.com/spreadsheets/d/1PlwrassxaYlM2lyRDQEcbMSEhV1EA00pC7Ye_yW5lW4/edit#gid=621060324")
