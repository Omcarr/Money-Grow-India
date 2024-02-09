import time
import os
from datetime import datetime
from Features import Features
from ClientFolders import GetDatafromCSV
from Secure import download_loc
from FileSorting import move_files


def PreDownload():
    # Folder should not have any data initally
    JUNK_DATA = os.listdir(download_loc)
    if JUNK_DATA:
        print('\nPlease empty the Download folder\n')
        raise SystemExit

    # Object created to access features class functions
    Bot = Features()

    # login into the account
    Bot.login()

    # Client master download
    Bot.CSVdownloader()
    time.sleep(5)
    Bot.EndTask()

    # Csv to client_dict. Handles errors in case of wrong Client master
    try:
        if os.path.isfile(f"{download_loc}MONEYGROW1_ClientMaster.csv"):
            client_dict = GetDatafromCSV(
                path=f"{download_loc}MONEYGROW1_ClientMaster.csv")
        else:
            with open(f"{download_loc}Errors.txt", 'w') as ErrorLog:
                ErrorLog.write('Master Csv was not downloaded.')

    except Exception as e:
        with open(f"{download_loc}Errors.txt", 'w', 'w') as ErrorLog:
            ErrorLog.write(f'\nAn error occurred: {str(e)}')

    return client_dict

def chunk(BeginAt, end, client_dict, start_date, end_date, CustomDate):
    Bot = Features()
    Bot.login()
    for i in range(BeginAt, end):
        Bot.FactSheet(client_id=i,end_date=end_date)
        Bot.CurrentPortfolio(client_id=i,end_date=end_date)
        Bot.TransactionStatement(
            client_id=i, start_date=start_date, end_date=end_date, CustomDate=CustomDate)
        Bot.BankBook(client_id=i, start_date=start_date,
                     end_date=end_date, CustomDate=CustomDate)
        Bot.StatementOfDividend(
            client_id=i, start_date=start_date, end_date=end_date, CustomDate=CustomDate)
        Bot.StatementOfExpense(
            client_id=i, start_date=start_date, end_date=end_date, CustomDate=CustomDate)
        Bot.CaptialGainLoss(
            client_id=i, start_date=start_date, end_date=end_date, CustomDate=CustomDate)
        time.sleep(5)
        move_files(source_folder=download_loc,
                   client_id=i, client_name=client_dict[i])
    Bot.EndTask()


def RegularDownload(BeginAt, start_date, end_date, CustomDate):
    client_dict = PreDownload()
    id_list = []
    for key in client_dict.keys():
        id_list.append(key)

    chunk(BeginAt=BeginAt, end=int(id_list[-1])+1, client_dict=client_dict,
          start_date=start_date, end_date=end_date, CustomDate=CustomDate)


def choice():
    start_date = input("\nEnter the start date (format: DD/MM/YYYY): ")
    start_date= datetime.strptime(start_date, "%d/%m/%Y").date()
    end_date = input("\nEnter the end date (format: DD/MM/YYYY): ")
    end_date= datetime.strptime(end_date, "%d/%m/%Y").date()
    current_date = datetime.now().date()
    if start_date > current_date or end_date > current_date or start_date>end_date:
        print("\nPlease enter a valid date.")
    else:
        CustomDate = True
        start_date=start_date.strftime("%d/%m/%Y")
        end_date=end_date.strftime("%d/%m/%Y")
        A =int(input('\nEnter the Client ID: '))
        if len(str(A))!=8:
            print('\nInvalid Client ID. Please try again')

        RegularDownload(BeginAt=A, start_date=str(start_date),
                        end_date=str(end_date), CustomDate=CustomDate)
        print('\nDownload complete succesfully')


if __name__ == '__main__':
    choice()