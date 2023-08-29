# Created by viktoriaplesha at 8/28/23
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page is opened
