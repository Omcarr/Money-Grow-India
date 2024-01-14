#login creds
Url = 'https://faconnect.kotak.com:9445/wealthspectrum/app/login'
login_id='MONEYGROW1'
pass_word='Temp1234#'
download_loc='D:\\Omkar\\MGI data\\'

#each file is taking about 7-10 seconds for the download
#logging in and scraping the columns from csv file take about 15 seconds

# cd={ 10210001: 'POOJA GUPTA  ',
#     10210002: 'SUNITA GUPTA  ',
#     10210003: 'DAYA NAND GUPTA  ',
#     10210004: 'KRISHNAVA DUTT',
#     10210005: 'PARUL AGARWAL  ',
#     10210006: 'MANISH GUPTA  ',
#     10210007: 'SWAGATAM BISWAS  ',
#     10210008: 'MONEYGROW ASSET PRIVATE LIMITED  ',
#     10210009: 'SUSHMA GUPTA',
#     10210010: 'GUNPRAVEEN KAUR',}
#time for download and sorting of 38 fact sheets 5:55



#move_files(client_id=10210001,client_name=cd[10210001])
# source="D:\\Omkar\\folder sort test\\MONEYGROW1_10210001_PortFolioFactSheet6020CT.pdf"
# destination="D:\\Omkar\\folder sort test\\POOJA GUPTA"
# shutil.move(src=source,dst=destination)

#move_files(source_folder="D:\\Omkar\\MGI data\\",client_id=10210004,client_name=cd[10210004])



# from datetime import datetime
# current_datetime = datetime.now()
# curr_date=current_datetime.strftime("%d/%m/%Y")
# # Extract the current month as a two-digit number
# curr_month = current_datetime.strftime("%m")
# curr_year=current_datetime.strftime("%y") 

# print(curr_date,curr_month,curr_year)



#test.py
# import time
# import os
# from Features import Features
# from ClientFolders import GetDatafromCSV
# from Secure import download_loc
# from FileSorting import move_files
# from datetime import datetime

# def main():
#     # Target folder should not have any pdfs or folders to avoid naming and copy issues
#     JUNK_DATA = os.listdir(download_loc)
#     if JUNK_DATA:
#      print('\nPlease empty the download folder\n')
#      raise SystemExit

#     # # Object created to access features class functions
#     # Bot = Features()

#     # # login into the account
#     # Bot.login()


#     # Client master download
#     # Bot.CSVdownloader()
#     # time.sleep(5)
#     # Bot.EndTask()

#     # # Csv to client_dict. Handles errors in case of wrong Client master
#     # try:
#     #  if os.path.isfile(f"{download_loc}MONEYGROW1_ClientMaster.csv"):
#     #     client_dict = GetDatafromCSV(
#     #         path=f"{download_loc}MONEYGROW1_ClientMaster.csv")
#     #  else:
#     #     with open(f"{download_loc}Errors.txt", 'w') as ErrorLog:
#     #         ErrorLog.write('Master Csv was not downloaded.')

#     # except Exception as e:
#     #  with open(f"{download_loc}Errors.txt", 'w', 'w') as ErrorLog:
#     #     ErrorLog.write(f'\nAn error occurred: {str(e)}')
    
#     def askdate():
#        user_start_date=input("\nEnter the start date (format: DD/MM/YYYY): ")
#        user_end_date=input("\nEnter the end date (format: DD/MM/YYYY): ")
#        return user_start_date,user_end_date
    
#     client_id=10210001
#     s,e=askdate()
#     # s='25/12/2023'
#     # e='12/01/2024'
#     Bot=Features()
#     Bot.login()
#     Bot.StatementOfExpense(client_id=client_id,start_date=s,end_date=e)
#     time.sleep(3)
    

# if __name__=='__main__':
#   main()