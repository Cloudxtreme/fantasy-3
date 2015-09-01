import time
import urllib2
from itertools import product

from pylearn2.utils import serial




element_filter = {'te_1': 'Arsenal',
                  'te_2': 'Aston Villa',
                  'te_3': 'Bournemouth',
                  'te_4': 'Chelsea',
                  'te_5': 'Crystal Palace',
                  'te_6': 'Everton',
                  'te_7': 'Leicester',
                  'te_8': 'Liverpool',
                  'te_9': 'Man City',
                  'te_10': 'Man Utd',
                  'te_11': 'Newcastle',
                  'te_12': 'Norwich',
                  'te_13': 'Southampton',
                  'te_14': 'Spurs',
                  'te_15': 'Stoke',
                  'te_16': 'Sunderland',
                  'te_17': 'Swansea',
                  'te_18': 'Watford',
                  'te_19': 'West Brom',
                  'te_20': 'West Ham',}

stat_filter = {'total_points': 'Total score',
               'event_points': 'Round score',
               'now_cost': 'Price',
               'selected_by_percent': 'Teams selected by %',
               'minutes': 'Minutes played',
               'goals_scored': 'Goals scored',
               'assists': 'Assists',
               'clean_sheets': 'Clean sheets',
               'goals_conceded': 'Goals conceded',
               'own_goals': 'Own goals',
               'penalties_saved': 'Penalties saved',
               'penalties_missed': 'Penalties missed',
               'yellow_cards': 'Yellow cards',
               'red_cards': 'Red cards',
               'saves': 'Saves',
               'bonus': 'Bonus',
               'ea_index': 'EA SPORTS PPI',
               'bps': 'Bonus Points System',
               'form': 'Form',
               'dreamteam_count': 'Times in Dream Team',
               'value_form': 'Value (form)',
               'value_season': 'Value (season)',
               'points_per_game': 'Points per game',
               'transfers_in': 'Transfers in',
               'transfers_out': 'Transfers out',
               'transfers_in_event': 'Transfers in (round)',
               'transfers_out_event': 'Transfers out (round)',}
#                'cost_change_start': 'Price rise',
#                'cost_change_start_fall': 'Price fall',
#                'cost_change_event': 'Price rise (round)',
#                'cost_change_event_fall': 'Price fall (round)',}


class Data(object):
    
    def __init__(self):
        self.data = dict()
        
    def add_data_block(self, playerID, header, content):
#         assert len(header)==(len(content)-1)
        state = self.data[playerID] if self.data.has_key(playerID) else {}
        newInfo = {h: c for h, c in zip(header, content)}
        state.update(newInfo)
        self.data[playerID] = state
    


def ParseContentBlock(block):
    
    block = [line.strip() for line in block[1:]]
    
    playerID = block[0].split(' ')
    if len(playerID)>1:
        playerID = int(playerID[1].split('"')[1][1:])
    else:
        playerID = 'ID'
    
    block = [line.strip('</th>') for line in block[1:]]
    block = [line.strip('</td>') for line in block]
    block = [line if not line[:4]=='abbr' else line.split('"')[1] for line in block]
    block = [line for line in block if not line=='']
    
    return playerID, block



if __name__=="__main__":

    Database = Data()
    
    urlpath = 'http://fantasy.premierleague.com/stats/elements/'
    
    ef = 'te_1'
    sf = 'assists' 
    
    """
    t = time.time()    
    for ef, sf, page in product(element_filter, stat_filter, range(2)):
        _urlpath = urlpath+'?element_filter='+ef+'&stat_filter='+sf+'&page='+str(page+1)
        f = urllib2.urlopen(_urlpath)
        
        content = []
        for line in f:
            line = line[:-1]
            if not line=='':
                content.append(line)
        
        try:
            start_index = content.index('<option value="cost_change_event_fall">Price fall (round)</option>')+1
        except:
            print ef, sf, page
            
        index = start_index
        isHeader = True
        while not content[index]=='    </table>':
            if content[index]=='            <tr>': 
                block_start = index
                while not content[index]=='            </tr>':
                    index += 1
                block = content[block_start+1:index]
                if isHeader:
                    _i, headerContent = ParseContentBlock(block)
                    isHeader = False
                else:
                    playerID, blockContent = ParseContentBlock(block)
                    Database.add_data_block(playerID, headerContent, blockContent)
                    
            else:
                index += 1
            
    serial.save('Database.pkl', Database)
    
    print "Total time: ", time.time() - t
    
    """
    
    Database = serial.load('Database.pkl')
    print len(Database.data.keys())
    for key in Database.data[1]:
        print key
    
    
    