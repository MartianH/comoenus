Feature: Send GET request to REST API

  Scenario: submission REST request
      when I send a GET request for submission thumbnail for "dummy"
      then response code should be 200

  Scenario: submission REST request
      when I send a GET request for submission thumbnail for misspelled "dumm"
      then response code should be 404

