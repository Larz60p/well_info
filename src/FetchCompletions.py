import WellPaths
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import CheckInternet
import sys


class GetCompletions:
    def __init__(self, infile):
        self.wpath = WellPaths.WellPaths()
        self.check_network = CheckInternet.CheckInternet()
        # self.homepath = Path('.')
        # self.rootpath = self.homepath / '..'
        # self.datapath = self.rootpath / 'data'
        # self.commandpath = self.datapath / 'command_files'
        # self.completionspath = self.datapath / 'completions'
        # self.htmlpath = self.datapath / 'html'
        # self.reportspath = self.datapath / 'reports'

        if self.check_network.check_availability():
            # use: Api_May_27_2018.txt for testing
            self.infilename = 'Api_May_27_2018.txt'
            # self.infilename = input('Please enter api filename: ')

            self.infile = self.wpath.commandpath / self.infilename
            self.api = []

            with self.infile.open() as f:
                for line in f:
                    self.api.append(line.strip())

            self.fields = ['Spud Date', 'Total Depth', 'IP Oil Bbls', 'Reservoir Class', 'Completion Date',
                           'Plug Back', 'IP Gas Mcf', 'TD Formation', 'Formation', 'IP Water Bbls']
            self.get_all_pages()
            self.parse_and_save(getpdfs=True)
        else:
            print('Internet access required, and not found.')
            print('Please make Internet available and try again')

    def get_url(self):
        """

        :return:
        """
        for entry in self.api:
            print("http://wogcc.state.wy.us/wyocomp.cfm?nAPI={}".format(entry[3:10]))
            yield (entry, "http://wogcc.state.wy.us/wyocomp.cfm?nAPI={}".format(entry[3:10]))

    def get_all_pages(self):
        for entry, url in self.get_url():
            print('Fetching main page for entry: {}'.format(entry))
            response = requests.get(url)
            if response.status_code == 200:
                filename = self.wpath.htmlpath / 'api_{}.html'.format(entry)
                with filename.open('w') as f:
                    f.write(response.text)
            else:
                print('error downloading {}'.format(entry))

    def parse_and_save(self, getpdfs=False):
        filelist = [file for file in self.wpath.htmlpath.iterdir() if file.is_file()]
        for file in filelist:
            with file.open('r') as f:
                soup = BeautifulSoup(f.read(), 'lxml')
            if getpdfs:
                links = soup.find_all('a')
                for link in links:
                    url = link['href']
                    if 'www' in url:
                        continue
                    print('downloading pdf at: {}'.format(url))
                    p = url.index('=')
                    response = requests.get(url, stream=True, allow_redirects=False)
                    if response.status_code == 200:
                        try:
                            header_info = response.headers['Content-Disposition']
                            idx = header_info.index('filename')
                            filename = self.wpath.completionspath / header_info[idx+9:]
                        except ValueError:
                            filename = self.wpath.completionspath / 'comp{}.pdf'.format(url[p + 1:])
                            print("couldn't locate filename for {} will use: {}".format(file, filename))
                        except KeyError:
                            filename = self.wpath.completionspath / 'comp{}.pdf'.format(url[p + 1:])
                            print('got KeyError on {}, response.headers = {}'.format(file, response.headers))
                            print('will use name: {}'.format(filename))
                            print(response.headers)
                        with filename.open('wb') as f:
                            f.write(response.content)
            sfname = self.wpath.reportspath / 'summary_{}.txt'.format((file.name.split('_'))[1].split('.')[0][3:10])
            tds = soup.find_all('td')
            with sfname.open('w') as f:
                for td in tds:
                    if td.text:
                        if any(field in td.text for field in self.fields):
                            f.write('{}\n'.format(td.text))
            # Delete html file when finished
            file.unlink()

if __name__ == '__main__':
    GetCompletions('apis.txt')
