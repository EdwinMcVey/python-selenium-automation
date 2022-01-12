# Created by Owner at 1/5/2022
Feature: Open Amazon Best Seller Page

  Scenario: User can see 5 links on the Best Seller page
    Given Open Amazon Best Sellers page
    Then Verify there are 5 links
