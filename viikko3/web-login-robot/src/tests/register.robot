*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Register User
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  pe
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Register User
    Register Should Fail With Message  Username must be at least 3 characters long and can contain only letters a-z

Register With Valid Username And Too Short Password
    Set Username  pekka
    Set Password  pekka1
    Set Password Confirmation  pekka1
    Register User
    Register Should Fail With Message  Password must be at least 8 characters long and must contain also other symbols than letters A-z

Register With Nonmatching Password And Password Confirmation
    Set Username  pekka
    Set Password  pekka1234
    Set Password Confirmation  pekka1235
    Register User
    Register Should Fail With Message  Password fields do not match


*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register User
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
