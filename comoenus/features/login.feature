Feature: Login in user

  Scenario: User logs in
      Given that user is in the database
      when user logs with username "dummy" and password "Password2016"
      then auth message should be "success"