Feature: User can search for a dress
  Scenario: Verify that a user can search for a dress
    Given Open Amazon page
    When Search for dress
    Then Verify search result is correct



#Feature: Verify that a user can search for a product

  Scenario Outline: Verify that a user cab search for a product
    Given Open Amazon page
    When Search for <search_word>
    Then Verify search result is <search_word>

    Examples:
      | search_word | search_result |
      | cup         | "cup"         |
      | dress       | "dress"       |
      | tea         | "tea"         |

  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Search for Tritan Farm to Table Pitcher on amazon
    When Click on the first product
    When Store product name
    When Click on Add to cart button
    When Open cart page
    Then verify cart has 1 item(s)
    Then Verify cart has correct product


  Scenario: Verify that user see product names and images
    Given Open Amazon page

