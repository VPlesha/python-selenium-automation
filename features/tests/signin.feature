# Created by viktoriaplesha at 8/28/23
Feature: SignIn test
  # Enter feature description here

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page is opened


  Scenario: Amazon users see sign in button
    When Open Amazon page
    Then Verify Sign In is clickable
    When Wait for 3 sec
    Then Verify Sign In is clickable
#    Then Verify Sign In disappears
