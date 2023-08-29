# Created by viktoriaplesha at 8/17/23
Feature: Verify user can see that every product has a name and image

  Scenario: Verify product has name and image
    Given Open Amazon page
    When Look for item
    When Click on search button
    Then Verify every product has name and image