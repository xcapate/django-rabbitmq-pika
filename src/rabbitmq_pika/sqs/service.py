from .BaseExceptions import CustomException
class TempService(object):
    def checkDict(self):
        dict = {"name":"foo"}
        try:
            guy = dict["name"]
        except KeyError as e:
            raise CustomException(e)