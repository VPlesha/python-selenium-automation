# Created by viktoriaplesha at 8/17/23
Feature: Verify user can see that every product has a name and image

  Scenario: Verify product has name and image
    Given Open amazon home page
    When Search for product
    When Click on search button
    Then Verify every product has name and image