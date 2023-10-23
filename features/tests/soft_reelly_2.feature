# Created by viktoriaplesha at 10/13/23
Feature: Right number of UI elements

  Scenario: User can go to settings and see the right number of UI elements
    Given Open the main page
    When  Log in to the page
    When  Click on settings option
    When  Verify the right page opens
    When  Click on each settings option and go back (except on log out)
    Then  Verify there are 11 options for the settings