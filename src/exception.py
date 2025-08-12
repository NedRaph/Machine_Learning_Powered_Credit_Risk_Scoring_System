import sys

class CustomException(Exception):
    def __init__(self, message, error_detail: sys):
        super().__init__(message)
        self.error_detail = error_detail

    def __str__(self):
        _, _, exc_tb = self.error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return f"Error occurred in file [{file_name}] line [{line_number}] message: {super().__str__()}"
