import os

def getCitiBikeCSV(date):
    ''' 
    This function returns citi bike data for a given month(s)
    
    Parameters
    ----------
    date: string
        Pass one month by inputting format <YYYY><MM>; EX: 201801
        Pass month range by inputting format <YYYY><M1M1><M2M2>; EX: 20180103
        
    Returns
    ----------
    csv: table
        dumps it into your PUIDATA folder
    '''
    path = "https://s3.amazonaws.com/tripdata/{}-citibike-tripdata.csv.zip".format(str(date))
    os.system('curl -O ' + path)
    currentpath = []
    currentpath.append(os.getcwd())
    os.system('unzip -u '+currentpath[0]+'/'+ path.split('/')[-1]+ ' -d $PUIDATA')
    print('Downloaded',path.split('/')[-1].split('.z')[0], 'to your PUIDATA folder!')