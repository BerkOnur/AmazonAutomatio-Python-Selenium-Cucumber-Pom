Feature: Amazon

	Scenario: Amazon login, add list
        Given I visit Amazon
        When I click Sign In button
        When I login Amazon with username "YOUR E-MAIL" and password "YOUR PASSWORD"
        When I write "samsung" in search field and click
        Then I check result is samsung
        Then I click second page
        When I click third product
        Then I click add list button
        Then I close add list page
        When I click list button and later click Shopping List button
        Then I see product and check
        Then I deleted the product and I see deleted alert
