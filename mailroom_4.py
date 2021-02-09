# This program will open by allowing for three options
# One, it should allow the user to send a Thank You note using an input
## - By inputting "list" it should show a list of all donor names and reprompt
## - By typing in a name not in the list, it should add the name to the records
## - If a valid name is entered, it should ask for donation amount to be recorded
## - After these tasks are complete, it should print a letter and go to the original prompt
# Two, it should allow the user to create a report of all donors, ordered by total donated historically

# Three, it should allow the user to quit the program

import tempfile
import os

import pytest


donors = [{'name':'Young',
           'donations':[23, 20],
           'donation_total': 43},
          {'name':'Ryan',
           'donations':[10, 22, 12],
           'donation_total': 44},
          {'name':'Brian',
           'donations':[30],
           'donation_total': 30},
          {'name':'Esther',
           'donations':[20],
           'donation_total': 20},
          {'name':'Melissa',
           'donations':[40],
           'donation_total': 40}
          ]


def write_files(file_location):

    try:
        for donor in donors:
            #try:
            #new_file = open(f"{tempfile.gettempdir()}\{donor['name']}.txt", "w")
            #new_file = open(f"{file_location}\{donor['name']}.txt", "w")
            with open(f"{file_location}\{donor['name']}.txt", "w", newline="") as new_file:
                # new_file.write(f"Dear {donor['name']},\n"
                #   f"We wanted to thank you for your generous donations totaling {donor['donation_total']}!\n"
                #   f"We really appreciate every contribution. You should know that it does a world of good.\n"
                #   f"All the best,\n"
                #   f"The Organization")
                # #-- Open in read mode and try again. print(new_file.read())
            #new_file.close()
            #except FileNotFoundError:
                #print("That location does not exist")
                new_file.write("Dear {name},\n"\
                                "We wanted to thank you for your generous donations totaling {donation_total}!\n"\
                               "We really appreciate every contribution. You should know that it does a world of good.\n"\
                               "All the best,\n"\
                               "The Organization".format(**donor))
    except FileNotFoundError:

        print("That file location does not exist. Please try again.")


def send_all_letters():
    # tempfile.mkdtemp()
    # print(tempfile.gettempdir())
    file_location = input("Where do you want your letters to be saved?")
    write_files(file_location)
    #check_path = os.path.exists(file_location)

    # This attempts to create a new file and to write text to that file
    # The way to test this would be determine if the path for the file exists
    # Not sure how to check for the existence of the text

#Try creating a new directory if it doesn't already exist.


def donor_sort(sort_key, reverse = True):
    donor_list = sorted(donors, key=lambda x: x[sort_key], reverse=reverse)
    return donor_list


def create_report():
    donor_list = donor_sort('donation_total')
    # Need to reorder the existing donor list so that it is ordered by highest amount given first
    report = '{:<25}|{:^16} |{:^12}|{:^18}\n'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    for donor in donor_list:
        total_gift_number = 0
        for donation in donor['donations']:
            total_gift_number += 1
        avg_gift = round((donor['donation_total'] / total_gift_number), 2)
        report += '{:<25}| ${:>14.2f} |{:>11} | ${:>13.2f}\n'.format(donor['name'], donor['donation_total'], total_gift_number, avg_gift)

    print(report)


def print_list(donor_list):
    new_donor_list = [donor['name'] for donor in donor_list]
    return new_donor_list


def add_new_record(donor_list, response, donation_amount):
    new_user = 1
    for donor in donor_list:
        if response == donor['name']:
            donor['donations'].append(donation_amount)
            donor['donation_total'] += donation_amount
            new_user = 0
            break
    if new_user:
        donors.append({'name': response,
                       'donations': [donation_amount],
                       'donation_total': donation_amount
                       })
    return donor_list


def send_thank_you():
    donor_list = donor_sort('name', False)
    while True:
        # Wondering if this would be better created as a separate function
        response = input("Enter the donor's name: ")

        # This is displaying a list of all existing donors
        # This could be tested comparing the list created here, with a list created by the same code in a test
        if response == 'list':
            new_donor_list = print_list(donor_list)
            print(new_donor_list)
            print(f'Above is a list of all donors.')
            continue

        print(f'You have entered {response}.')

        # This stops this functionality and returns to the main menu
        if response == 'quit':
            break

        donation_amount = int(input('Please enter a donation amount: '))

        # This adds a donation to an existing donor's record; if the donor is new, it creates a new record
        # This could be tested by entering a set user name and new donation and comparing it the expected outcome
        add_new_record(donor_list, response, donation_amount)


        # This prints the letter for a given donor
        # How can this be tested?
        print(f"\nDear {response},\n"
              f"We wanted to thank you for your generous donation of {donation_amount}!\n"
              f"We really appreciate every contribution. You should know that it does a world of good.\n"
              f"Please keep this letter if you intend to take a tax deduction with the IRS.")

        break


def switchboard(command):
    menu_options = {'1': send_thank_you,
                    '2': create_report,
                    '3': send_all_letters
                    }
    run_item = menu_options.get(command)
    try:
        run_item()
    except TypeError:
        print("That is not a valid response.\n")


if __name__ == '__main__':

    while True:
        command = input(f"\nWhat would you like to do today?\n"
                        f"\nPlease indicate:\n\n1.) 'Send a Thank You or \"1\"'\n2.) 'Create a Report or \"2\"'\n3.) 'Send letters to all donors or \"3\"'\n4.) 'Quit or \"4\"': \n").lower()
        if command == 'quit' or command == '4':
            break
        switchboard(command)