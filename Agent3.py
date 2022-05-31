# !/usr/bin/env python
import random
class Agent3:

    def __init__(self,valence_table):
        """ Creating our agent """
        self.valence_table = valence_table
        self._action = 0
        self.previous_outcome = 0
        self.previous_action = 0
        self.outcome_for_action1 = 0
        self.outcome_for_action0 = 0
        self.anticipated_outcome = None
        self.counter = 0


    def action(self, outcome):
        """ tracing the previous cycle """
        if self._action is not None:
                print("Action: " + str(self._action) +
                      ", Anticipation: " + str(self.anticipated_outcome) +
                      ", Outcome: " + str(outcome) +
                      ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                      ", valence: " + str(self.valence_table[self._action][outcome]) +
                      "; counter: " + str(self.counter) + ")")


        # Choisir la prochaine action
        if self._action == 0:
            self.outcome_for_action0 = outcome
        else:
            self.outcome_for_action1 = outcome

        valence0 = self.valence_table[0][self.outcome_for_action0]
        valence1 = self.valence_table[1][self.outcome_for_action1]

        if valence0 > valence1:
            self._action = 0
        else:
            self._action = 1



        return self._action