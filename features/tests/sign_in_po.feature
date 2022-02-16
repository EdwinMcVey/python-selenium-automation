# Created by Owner at 1/22/2022
Feature: User can see Sign page when Clicking Orders

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon Page
    When Click Amazon Orders link
    Then Verify Sign in page is opened


