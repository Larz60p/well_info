import WellPaths


class Codes:
    def __init__(self):
        self.GeologyCodes = {
            'Well File Status': {
                'PO': 'Producing Oil Well',
                'PG': 'Producing Gas Well',
                'DH': 'Dry Hole',
                'SI': 'Shut - In',
                'TA': 'Temporarily Abandoned',
                'PA': 'Permanently Abandoned',
                'AI': 'Active Injector',
                'DR': 'Dormant',
                'NI': 'Notice of Intent to Abandon',
                'SR': 'Subsequent Report of Abandonment',
                'EP': 'Expired Permit',
                'AP': 'Permit to Drill',
                'SP': 'Well Spudded',
                'WP': 'Waiting on Approval',
                'UNK': 'Unknown',
                'NR': 'No Report',
                'SO': 'Suspended Operations'
            },
            'Classification': {
                'O': 'Oil Well',
                'G': 'Gas Well',
                'C': 'Condensate',
                'I': 'Injector Well',
                'S': 'Source Well',
                'AP': 'Active Permit',
                'D': 'Disposal',
                'M': 'Monitor Well',
                'MW': 'Monitor Well ( Not for Form 2 Reporting )',
                'ST': 'Strat Test',
                'GS': 'Gas Storage',
                'GO': 'Gas Orphaned',
                'OO': 'Oil Orphaned',
                'DO': 'Disposal Orphaned',
                'IO': 'Injector Orphaned',
                'MO': 'Monitor Well Orphaned',
                'LW': 'LandOwner Water Well'
            },
            'Form2 Classification': {
                'O': 'Oil Well',
                'G': 'Gas Well',
                'C': 'Condensate',
                'I': 'Injector Well',
                'S': 'Source Well',
                'D': 'Disposal',
                'M': 'Monitor Well'
            },
            'Form2 Status': {
                'FL': 'Flowing',
                'GL': 'Gas Lift',
                'PR': 'Pumping Rods',
                'PS': 'Pumping Submersible',
                'PH': 'Pumping Hydraulic',
                'PL': 'Plunger Lift',
                'TA': 'Temporarily Abandoned',
                'PA': 'Permanently Abandoned',
                'AI': 'Active Injector',
                'DR': 'Dormant',
                'SI': 'Shut-In'
            },
            'APD File Status': {
                'AP': 'Active Permit',
                'EP': 'Expired Permit',
                'DP': 'Drilling or Drilled Permit',
                'NO': 'Denied or Cancelled',
                'WP': 'Waiting on Approval'
            },
            'Land Type': {
                '10': 'Federal/Unknown',
                '11': 'Federal/Federal',
                '13': 'Federal/Fee',
                '14': 'Federal/State',
                '20': 'Patented',
                '23': 'Fee/Fee',
                '30': 'Fee',
                '31': 'Fee/Federal',
                '34': 'Fee/State',
                '36': 'Fee/Tribal',
                '40': 'State',
                '41': 'State/Federal',
                '43': 'State/Fee',
                '46': 'State/Tribal',
                '60': 'Tribal',
                '63': 'Tribal/Fee',
                '64': 'Tribal/State',
                '81': 'MM /Fed',
                '83': 'MM /Fee',
                '84': 'MM /State',
                '85': 'MM-State/Fee',
                '91': 'MM w-Fed/Fed',
                '93': 'MM w-Fed/Fee',
                '94': 'MM w-Fed/State'
            },
            'County': {
                '001': 'Albany',
                '003': 'Big Horn',
                '005': 'Campbell',
                '007': 'Carbon',
                '009': 'Converse',
                '011': 'Crook',
                '013': 'Fremont',
                '015': 'Goshen',
                '017': 'Hot Springs',
                '019': 'Johnson',
                '021': 'Laramie',
                '023': 'Lincoln',
                '025': 'Natrona',
                '027': 'Niobrara',
                '029': 'Park',
                '031': 'Platte',
                '033': 'Sheridan',
                '035': 'Sublette',
                '037': 'Sweetwater',
                '039': 'Teton',
                '041': 'Uinta',
                '043': 'Washakie',
                '045': 'Weston'
            },
            'Sage Grouse Area Types': {
                'SG-1': 'Core Area',
                'SG-2': 'Seasonal/NSO'
            }
        }

    # This dictionary can saved as a json file and recalles in any script that needs it:

    def print_code(self, cd_type, code):
        """
        print_code(cd_type, code)

        Example: you get a well file status code from some data somewhere, and want to display that code

        :cd_type: Holds code type 'Well File Status', or 'Classification', etc.
        :code: Holds actual code like 'AP'
        
        :returns: None
        """
        print(self.GeologyCodes[cd_type][code])

    def try_status(self):
        """
        try_status()

        test print_code
        
        :returns: None
        """
        self.print_code('Well File Status', 'PG')
        code_type_from_file = 'Classification'
        code_from_file = 'LW'
        self.print_code(code_type_from_file, code_from_file)
        
if __name__ == '__main__':
    cd = Codes()
    cd.try_status()
