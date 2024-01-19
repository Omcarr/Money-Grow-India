import time
import os
from datetime import datetime
from Features import Features
from ClientFolders import GetDatafromCSV
from Secure import download_loc
from FileSorting import move_files


def PreDownload():
    #Folder should not have any data initally
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


def chunk(BeginAt, end, id_list, client_dict, start_date, end_date, CustomDate):
    Bot = Features()
    Bot.login()
    for i in range(BeginAt, end):
        Bot.FactSheet(client_id=id_list[i])
        Bot.CurrentPortfolio(client_id=id_list[i])
        Bot.TransactionStatement(
            client_id=id_list[i], start_date=start_date, end_date=end_date, CustomDate=CustomDate)
        Bot.BankBook(client_id=id_list[i], start_date=start_date,
                     end_date=end_date, CustomDate=CustomDate)
        Bot.StatementOfDividend(
            client_id=id_list[i], start_date=start_date, end_date=end_date, CustomDate=CustomDate)
        Bot.StatementOfExpense(
            client_id=id_list[i], start_date=start_date, end_date=end_date, CustomDate=CustomDate)
        Bot.CaptialGainLoss(
            client_id=id_list[i], start_date=start_date, end_date=end_date, CustomDate=CustomDate)
        time.sleep(5)
        move_files(source_folder=download_loc,
                   client_id=id_list[i], client_name=client_dict[id_list[i]])
    Bot.EndTask()


def RegularDownload(start_date, end_date, CustomDate):
    client_dict = PreDownload()
    id_list = []
    for key in client_dict.keys():
        id_list.append(key)

    # dividing codes into chunks to minimse website server overloading cases
    chunk_size = 10
    num_chunks = len(id_list) // chunk_size

    for n in range(num_chunks):
        BeginAt = n * chunk_size
        end = (n + 1) * chunk_size
        chunk(BeginAt, end, id_list, client_dict,
              start_date, end_date, CustomDate=CustomDate)

    # Handling remaining clients
    if num_chunks * chunk_size < len(id_list):
        BeginAt = num_chunks * chunk_size
        end = len(id_list)
        chunk(BeginAt, end, id_list, client_dict,
              start_date, end_date, CustomDate=CustomDate)


# def CustomDownload(BeginAt, start_date, end_date, CustomDate):
#     client_dict = PreDownload()
#     id_list = []
#     for key in client_dict.keys():
#         id_list.append(key)

#     chunk(BeginAt=BeginAt, end=len(id_list),
#           id_list=id_list, client_dict=client_dict, start_date=start_date, end_date=end_date, CustomDate=CustomDate)


def choice():
    print(datetime.now(),end='\n\n')
    download_type = input(
        '\nEnter 1] for Regular download\n\t2] for Custom Date Regular download\n')

    if download_type == '1':
        current_datetime = datetime.now()
        end_date = current_datetime.strftime("%d/%m/%Y")
        curr_month = current_datetime.strftime("%m")
        curr_year = current_datetime.strftime("%y")

        if int(curr_month) >= 4:
            start_date = f'01/04/{curr_year}'
        else:
            start_date = f'01/04/{int(curr_year)-1}'

        CustomDate = False
        RegularDownload(start_date=start_date,
                        end_date=end_date, CustomDate=CustomDate)

    # elif download_type == '2':
    #     current_datetime = datetime.now()
    #     end_date = current_datetime.strftime("%d/%m/%Y")
    #     curr_month = current_datetime.strftime("%m")
    #     curr_year = current_datetime.strftime("%y")
    #     if int(curr_month) >= 4:
    #         start_date = f'01/04/{curr_year}'
    #     else:
    #         start_date = f'01/04/{int(curr_year)-1}'

    #     CustomDate = False
    #     A = int(input('Enter the Last significant digits of the Client ID:\n'))
    #     CustomDownload(BeginAt=A-1, start_date=start_date,
    #                    end_date=end_date, CustomDate=CustomDate)

    elif download_type == '2':
        start_date = input("\nEnter the start date (format: DD/MM/YYYY): ")
        end_date = input("\nEnter the end date (format: DD/MM/YYYY): ")
        CustomDate = True
        RegularDownload(start_date=start_date,
                        end_date=end_date, CustomDate=CustomDate)

    # elif download_type == '4':
    #     start_date = input("\nEnter the start date (format: DD/MM/YYYY): ")
    #     end_date = input("\nEnter the end date (format: DD/MM/YYYY): ")
    #     CustomDate = True
    #     A = int(input('Enter the Last significant digits of the Client ID:\n'))
    #     CustomDownload(BeginAt=A-1, start_date=start_date,
    #                    end_date=end_date, CustomDate=CustomDate)

    else:
        print('\nChoose a valid option')
        raise SystemExit

    print('\nDownload complete succesfully')
    print(datetime.now())


if __name__ == '__main__':
    choice()
