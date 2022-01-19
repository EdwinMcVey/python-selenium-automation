# Created by Owner at 12/11/2021

Feature: Test Scenarios for Adding Item to Amazon Cart


  Scenario: User can search for Adding Item to Cart
    Given Open Amazon Page
    When Search for penny whistle key of d
    And Click search icon
    And Click on first item
    And Click on Add to cart button
    Then Verify cart has 1 item(s)
