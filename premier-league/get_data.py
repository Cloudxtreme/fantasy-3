import urllib2
from HTMLParser import HTMLParser


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
               'transfers_out_event': 'Transfers out (round)',
               'cost_change_start': 'Price rise',
               'cost_change_start_fall': 'Price fall',
               'cost_change_event': 'Price rise (round)',
               'cost_change_event_fall': 'Price fall (round)',}


class Data(object):
    
    def __init__(self):
        self.data = dict()
        
    def add_data_block(self, header, content):
#         assert len(header)==(len(content)-1)
        playerID = content[0]
        oldState = self.data[playerID]
        newInfo = {h: c for h, c in zip(header, content[1:])}
        newState = oldState.update(newInfo)
        self.data[playerID] = newState
    


def ParseContentBlock(block):
    
    
    return block



if __name__=="__main__":

    Database = Data()
    
    urlpath = 'http://fantasy.premierleague.com/stats/elements/'
    
    ef = 'te_1'
    sf = 'total_points' 
    
    parser = HTMLParser()
    
    for page in range(2):
        _urlpath = urlpath+'?element_filter='+ef+'&stat_filter='+sf+'&page='+str(page+1)
        f = urllib2.urlopen(_urlpath)
        
        content = []
        for line in f:
            line = line[:-1]
            if not line=='':
                content.append(line)
        
        start_index = content.index('<option value="cost_change_event_fall">Price fall (round)</option>')+1
        index = start_index
        isHeader = True
        while not content[index]=='    </table>':
            if content[index]=='            <tr>': 
                block_start = index
                while not content[index]=='            </tr>':
                    index += 1
                block = content[block_start+1:index]
                if isHeader:
                    headerContent = ParseContentBlock(block)
                    isHeader = False
#                     print headerContent
                else:
                    blockContent = ParseContentBlock(block)
                    pass
                    
#                     Database.add_data_block(headerContent, blockContent)
                    
            else:
                index += 1
            
            
        
        print page, len(content), start_index, index
    
    print Database.data
    
    
    
    
    
    
    
    