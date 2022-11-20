*** Settings ***
Resource  resource.robot
Test Setup  Create New User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input New User  pekka  pakka1234
    Output Should Contain  New user registered
    

Register With Already Taken Username And Valid Password
    Input New User  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New User  ab  abcd1234
    Output Should Contain  Username must be at least 3 letters long, and contain only [a-z]

Register With Valid Username And Too Short Password
    Input New User  pekka  pekka1
    Output Should Contain  Password must be at least 8 characters long and must contain also other symbols than letters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New User  Pekka  pekPEKKAka

*** Keywords ***
Create New User And Input New Command
    Create User  kalle  kalle123
    Input New Command
    