
# EXAMPLE OF USE IN SIMPLE EXCEL MANIPULATION AND APP CREATION.

from duality import Record

r = Record()

class App:

    @r.entry('init', autoinit = True)
    def __init__(
        self,
        file = None,
    ):
        import pandas as pd
        file = r'C:\Users\kundi\Sphere\duality\.testassets\MC_testassets.xlsx'
        self.file = pd.read_excel(file)
        return 

    @r.entry('remove')
    def remove_vals(self):
        file = self.file.drop(columns=['set1'], inplace = True)
        return file

    @r.entry('save')
    def save_file(self):
        file = self.file.to_excel('Export.xlsx')
        return file

    def initconfig(self):
        return r.config(type = 'dynamic', queue = True)

a = App()

a.initconfig()