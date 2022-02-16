# Created by Owner at 1/27/2022
Feature: Amazon Cart is empty is not product added

 Scenario "Your Shopping Cart is empty' shown if no product added
    Given Open Amazon Page
    When Click on Cart Icon
    Then Very 'Your Amazon Cart is empty' text present
