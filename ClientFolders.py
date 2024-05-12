import pandas
#from pprint import pprint
# pprint(client_dict,indent=4)

def GetDatafromCSV(path):
    #path for the data
    client_data=pandas.read_csv(path)
    client_id=client_data['CLIENTID'].to_list()
    client_names=client_data['CLIENTNAME'].to_list()
    client_scheme=client_data['SCHEMENAME'].to_list()
    cd={}
    
    for i in range(len(client_id)):
        cd[client_id[i]]=f'{client_names[i]} ({client_scheme[i]})'
        #cd[client_id[i]]=client_names[i]
    return cd
