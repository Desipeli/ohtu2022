class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.scores = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty", 4: "Deuce"}

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 = self.m_score1 + 1
        elif player_name == self.player2_name:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score = ""

        if self.m_score1 == self.m_score2:
            score = self.same_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score = self.score_at_least_4()
        else:
            score = self.scores_under_4()

        return score

    def same_score(self):
        if self.m_score1 < 4:
            return f"{self.scores[self.m_score1]}-All"
        return f"{self.scores[self.m_score1]}"

    def score_at_least_4(self):
        minus_result = self.m_score1 - self. m_score2

        if minus_result == 1:
            score = f"Advantage {self.player1_name}"
        elif minus_result == -1:
                score = f"Advantage {self.player2_name}"
        elif minus_result >= 2:
            score = f"Win for {self.player1_name}"
        else:
            score = f"Win for {self.player2_name}"
        return score

    def scores_under_4(self):
        return f"{self.scores[self.m_score1]}-{self.scores[self.m_score2]}"