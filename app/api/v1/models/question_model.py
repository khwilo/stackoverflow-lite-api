'''This module represents the question entity'''
from datetime import datetime

QUESTIONS = [] # Data store for questions

class QuestionModel:
    '''Entity representation for a question'''
    def __init__(self, title, description, created_by, answers=None):
        self.question_id = len(QUESTIONS) + 1 # The question primary key
        self.title = title
        self.description = description
        self.created_by = created_by
        self.created_on = str(datetime.utcnow())
        self.answers = [] if answers is None else answers

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
    def get_answer_by_id(question, answer_id):
        '''Return an answer to a question by its id'''
        answers = question.get("answers")
        answer = {}
        for index, _ in enumerate(answers):
            if answers[index].get('answer_id') == answer_id:
                answer = answers[index]
        return answer

    @staticmethod
    def get_all_questions():
        '''Fetch all questions'''
        return QUESTIONS
