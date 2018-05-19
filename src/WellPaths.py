from pathlib import Path


class WellsPath:
    def __init__(self):
        self.homepath = Path('.')
        self.rootpath = self.homepath / '..'
        self.docpath = self.rootpath / 'doc'
        self.docpath.mkdir(exist_ok=True)
        self.datapath = self.rootpath / 'data'
        self.datapath.mkdir(exist_ok=True)
        self.commandpath = self.datapath / 'command'
        self.commandpath.mkdir(exist_ok=True)
        self.htmlpath = self.datapath / 'html'
        self.htmlpath.mkdir(exist_ok=True)
        self.welldatapath = self.datapath / 'well_data'
        self.welldatapath.mkdir(exist_ok=True)

# Direfctory structure
# well_info/
#    data/
#        command/
#        html/
#        well_data/
#    doc/
#    src/
if __name__ == '__main__':
    WellsPath()
