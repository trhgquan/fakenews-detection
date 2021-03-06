'''Detection API module'''

from flask_restful import Resource

from .utils import get_input
from .pipeline import Pipeline

class Detection(Resource):
    '''Detection API module class'''

    def __init__(self) -> None:
        '''Initialise data'''
        self.__p = Pipeline()

    def post(self):
        '''Handling POST method'''

        try:
            article_content = get_input('article_content')
            classifiers_list = self.__p.get_classifiers_list()

            return {
                'error' : False,
                'result' : self.__p.predict_all([article_content]),
                'total_classifiers' : len(classifiers_list)
            }, 200
        except FileNotFoundError as file_error:
            return {
                'error' : True,
                'message' : str(file_error)
            }, 400
        except AssertionError as exception:
            return {
                'error' : True,
                'message' : str(exception)
            }, 400
