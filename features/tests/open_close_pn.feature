# Created by Owner at 1/19/2022
Feature: User open and close Privacy Notice Page

  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened page
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window
    And Switch back to original

