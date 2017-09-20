#!/usr/bin/env python3

import csv
import sys


def main():
    with open(sys.argv[1]) as f:
        enpass_export_csv = csv.reader(f)

        enpass_export = []
        for login_csv in enpass_export_csv:
            if login_csv[0] == "Title":
                continue
            login = {}
            login['title'] = login_csv[0]
            login["note"] = login_csv[-1]
            print('Importing {}'.format(login['title']))
            for i in range(1, len(login_csv) - 1, 2):
                field_name = login_csv[i]
                field_value = login_csv[i + 1]
                login[field_name] = field_value
                print('    - {}'.format(field_name))
            enpass_export.append(login)

    onepassword_import = []
    for enpass_login in enpass_export:
        onepassword_login = []
        # Field order documented at https://support.1password.com/create-csv-files/
        print("Exporting {}".format(enpass_login['title']))
        for field_name in ['title', 'url', 'username', 'password', 'note']:
            # Check for common alernate capitalizations
            if not enpass_login.get(field_name):
                if enpass_login.get(field_name.title(), None):
                    field_name = field_name.title()
                elif enpass_login.get(field_name.capitalize(), None):
                    field_name = field_name.capitalize()
            print("    - {}".format(field_name))
            onepassword_login.append(enpass_login.pop(field_name, ""))
        for field_name, field_value in enpass_login.items():
            print("    - {}".format(field_name))
            onepassword_login.append("{}: {}".format(field_name, field_value))
        onepassword_import.append(onepassword_login)

    with open('out.csv', 'w') as f:
        csv.writer(f).writerows(onepassword_import)

    print("Import out.csv into 1Password")


if __name__ == "__main__":
    main()
