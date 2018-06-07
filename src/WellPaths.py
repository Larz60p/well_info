from pathlib import Path, PurePath, PureWindowsPath
import os


class WellPaths:
    def __init__(self):
        # Make sure start path is  properly set
        self.set_starting_dir()
        
        self.homepath = Path('.')
        self.rootpath = self.homepath / '..'
        self.datapath = self.rootpath / 'data'
        self.commandpath = self.datapath / 'command_files'
        self.completionspath = self.datapath / 'completions'
        self.htmlpath = self.datapath / 'html'
        self.reportspath = self.datapath / 'reports'
        self.docpath = self.rootpath / 'doc'
        self.new_user_path = self.datapath / 'NewUser'
        self.finding_infopath = self.new_user_path / 'FindingInformation-html'

        self.testfile = self.commandpath / 'Api_May_27_2018.txt'
        self.find_info_html = self.finding_infopath / 'http _wogcc.state.wy.us_rnewuserspage.html'

        # URL's
        self.Codes = 'http://wogcc.state.wy.us/codes.html'


    def set_starting_dir(self):
        path = Path(__file__).resolve()
        path, file = os.path.split(path)
        path = os.path.abspath(path)
        os.chdir(path)

def testit():
    wp = WellPaths()
    print(wp.commandpath.resolve())

if __name__ == '__main__':
    testit()
