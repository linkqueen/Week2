class Python():

    @classmethod
    def get_string(cls):
        response = str(input('How is Python Going for you?'))
        Python.print_string(response)

    @classmethod
    def print_string(cls,response):
        print(response.upper())
        


Ramika = Python()
Ramika.get_string()

