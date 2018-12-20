'''This module represents the answer entity'''
from datetime import datetime

from app.api.utils.serializer import serialize
from app.api.v1.models.question_model import QuestionModel

ANSWERS = [] # Data store for the answers

class AnswerModel:
    '''Entity representation for an answer'''
    def __init__(self, description, answered_by, accepted=None, rejected=None):
        self.answer_id = len(ANSWERS) + 1
        self.description = description
        self.answered_by = answered_by
        self.accepted = False if accepted is None else accepted
        self.rejected = False if rejected is None else rejected
        self.answered_on = str(datetime.utcnow())

    def get_answer_id(self):
        '''Fetch the answer id'''
        return self.answer_id

    def is_accepted(self):
        '''Return True/False for accepted'''
        return self.accepted

    def is_rejected(self):
        '''Return True/False for rejected'''
        return self.is_rejected

    def get_time_of_answer(self):
        '''Return the date the question was answered'''
        return self.answered_on

    @staticmethod
    def add_answer(answer, question_id):
        '''Add a new answer to the data store'''
        question = QuestionModel.get_question_by_id(int(question_id))
        ANSWERS.append(answer)
        question["answers"].append(serialize(answer))
