import sys

class NetworkSecurtyException(Exception):
    def __init__(self, error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = sys.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in the pyton script name[{0}] line number [{1}] error message [{2}]".format(self.file_name,self.lineno,str(self.error_message))