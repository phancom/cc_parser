import csv
import sys
import csv

#budget filter sort and sum based on text filters
#takes one arg, the CC csv file to be filtered 

filters= [
    'filter_grocery.csv',
    'filter_restaurants.csv',
    'filter_air_travel.csv',
    'filter_alcohol.csv',
    'filter_amazon.csv',
    'filter_bryan.csv',
    'filter_camping.csv',
    'filter_costco.csv',
    'filter_gasoline.csv',
    'filter_hailey.csv',
    'filter_home_improv.csv',
    'filter_jill.csv',
    'filter_local_retail.csv',
    'filter_payments.csv',
    'filter_subscriptions.csv',
    ]

desc_col = []
date_col = []


def filter_parser(trans,fltr_file):
    global desc_col
    global date_col

    with open(fltr_file, 'r') as fltr_f:
        fltr_list = list(csv.reader(fltr_f,delimiter = ','))
    
    for fltr_item in fltr_list:
        print(fltr_item)
    
    #find match to filter and get indexes of match
    match_idx =[]
    for fltr_item in fltr_list:
        i = 0
#        print(fltr_item)
        for row in trans:
            if any(x in row[desc_col] for x in fltr_item):
#                print('Match: ' + str(i))
#                print(row)
                match_idx.append(i)
            i += 1
    
    #pull out the matches, bottom to top
    filter_matches = []
    match_idx.sort(reverse = True)
    for i in match_idx:
        filter_matches.append(trans.pop(int(i)))

    for i in filter_matches:
        print(i)

    return trans, filter_matches

def write_results(fname,header,data):
    with open(fname,'a+') as f:
        fwriter = csv.writer(f)
        fwriter.writerow(header)
        fwriter.writerows(data)
        fwriter.writerow(' ') #blank line for next appened entry

def main_test(fname):
    #manually filter name entry test
    grocery_filter = 'filter_grocery.csv'
    rest_filter = 'filter_restaurants.csv'
    airtravel_filter =  'filter_air_travel.csv'
    alch_filter = 'filter_alcohol.csv'
    amazon_filter = 'filter_amazon.csv'
    bryan_filter = 'filter_bryan.csv'
    camping_filter = 'filter_camping.csv'
    costco_filter = 'filter_costco.csv'
    gas_filter = 'filter_gasoline.csv'
    hailey_filter = 'filter_hailey.csv'
    homeimprov_filter = 'filter_home_improv.csv'
    jill_filter = 'filter_jill.csv'
    localretail_filter = 'filter_local_retail.csv'
    payment_filter = 'filter_payments.csv'
    subscrip_filter = 'filter_subscriptions.csv'
    fname = str(fname)

    global desc_col
    global date_col
    data = []

    print('input file: ' + str(fname))
    with open(str(fname), 'r') as csv_file:
        data = list(csv.reader(csv_file, delimiter=','))

    header = data.pop(0)
    for i in range(len(header)):
        if 'Date' in header[i]:
            dat_col = i
            print('Date found Col: ' + str(i) + ' ' + header[i])
        if 'Description' in header[i]:
            desc_col = i
            print('Descripton found Col: ' + str(i) + ' ' + header[i])

    ub_data, grocery_match = filter_parser(data,grocery_filter)
    write_results('grocery_match.csv',header,grocery_match)

    ub_data, rest_match = filter_parser(ub_data,rest_filter)
    ub_data, airtravel_match = filter_parser(ub_data,airtravel_filter)
    ub_data, alch_match = filter_parser(ub_data,alch_filter)
    ub_data, amazon_match = filter_parser(ub_data,amazon_filter)
    ub_data, bryan_match = filter_parser(ub_data,bryan_filter)
    ub_data, camping_match = filter_parser(ub_data,camping_filter)
    ub_data, costco_match = filter_parser(ub_data,costco_filter)
    ub_data, gas_match = filter_parser(ub_data,gas_filter)
    ub_data, hailey_match = filter_parser(ub_data,hailey_filter)
    ub_data, homeimprov_match = filter_parser(ub_data,homeimprov_filter)
    ub_data, jill_match = filter_parser(ub_data,jill_filter)
    ub_data, localretail_match = filter_parser(ub_data,localretail_filter)
    ub_data, payment_match = filter_parser(ub_data,payment_filter)
    ub_data, subscrip_match = filter_parser(ub_data,subscrip_filter)
   
    print("\n Unbudgeted Transactions\n")
    for i in ub_data:
        print(i)

    return data

def main(fname, write_flag):

    fname = str(fname)

    global desc_col
    global date_col
    data = []

    print('input file: ' + str(fname))
    with open(str(fname), 'r') as csv_file:
        data = list(csv.reader(csv_file, delimiter=','))

    header = data.pop(0)
    for i in range(len(header)):
        if 'Date' in header[i]:
            dat_col = i
            print('Date found Col: ' + str(i) + ' ' + header[i])
        if 'Description' in header[i]:
            desc_col = i
            print('Descripton found Col: ' + str(i) + ' ' + header[i])
    
    #run one filter first on input data
    ub_data, match = filter_parser(data,filters[0])
    if write_flag:
        write_results(filters[0]+'_matches.csv', header, match)

    for fltr in filters[1:]:
        ub_data, match = filter_parser(ub_data,fltr)
        if write_flag:
            write_results(fltr+'_matches.csv', header, match)

    print("\n Unbudgeted Transactions\n")
    for i in ub_data:
        print(i)
    if write_flag:
        write_results('unmatched_resuts.csv', header, ub_data)

    return data
if __name__=='__main__':

    write_data_to_files = 1 # write out results to individual files
    main(sys.argv[1],write_data_to_files)

