Feature: Games
  laxleague games are between two teams and have a score resulting
  in a winner or a tie.

  Scenario: Determine The Winner
    Given a home team of Blue
    And a visiting team of Red
    And a game between them
    When the score is 10 for Blue to 5 for Red
    Then Blue is the winner