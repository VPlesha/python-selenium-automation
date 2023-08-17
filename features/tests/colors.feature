# Created by viktoriaplesha at 6/7/23
Feature: User can select color

  Scenario: User can pick a color
    Given Open amazon product page with multiple colors
    When  Click available color
    Then  All colors were selected one by one
