import xlrd
import os

class readExcel:
    def __init__(self, filename):
        self.cur_path = os.path.dirname(os.path.realpath(__file__))
        self.xls_path = os.path.join(self.cur_path, filename)
        self.file = xlrd.open_workbook(self.xls_path)

    def get_value(self,sheetname,rownum):
        sheet = self.file.sheet_by_name(sheetname)
        return sheet.row_values(rownum)

 #   def get_sheet_by_name(self,sheetname):
 #       return self.file.sheet_by_name(sheetname)

 #   def get_sheet_by_index(self,index):
 #       return self.file.sheets()[index]