'''This module represents the question entity'''
from datetime import datetime

QUESTIONS = [] # Data store for questions

class QuestionModel:
    '''Entity representation for a question'''
    def __init__(self, title, description, created_by):
        self.question_id = len(QUESTIONS) + 1 # The question primary key
        self.title = title
        self.description = description
        self.created_by = created_by
        self.created_on = str(datetime.utcnow())

    def get_question_id(self):
        '''Fetch the question id'''
        return self.question_id

    @staticmethod
    def add_questions(question):
        '''Add a new question to the data store'''
        QUESTIONS.append(question)

    @staticmethod
    def get_question_by_id(question_id):
        '''Return a question given a question id'''
        question = {}
        for index, _ in enumerate(QUESTIONS):
            if QUESTIONS[index].get('question_id') == question_id:
                question = QUESTIONS[index]
        return question

    @staticmethod
    def get_all_questions():
        '''Fetch all questions'''
        return QUESTIONS

    @staticmethod
    def delete_a_question_by_id(question_id):
        '''Delete a question given its id'''
        global QUESTIONS
        QUESTIONS = list(filter(lambda question: question['question_id'] != question_id, QUESTIONS))

    def question_as_dict(self):
        '''Convert the question object into a dictionary'''
        return {
            'question_id': self.question_id,
            'title': self.title,
            'description': self.description,
            'created_by': self.created_by,
            'created_on': self.created_on
        }
