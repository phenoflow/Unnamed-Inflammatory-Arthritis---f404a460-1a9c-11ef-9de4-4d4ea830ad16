# Amanda Nicholson, Elizabeth Ford, Kevin A Davies, Helen E Smith, Greta Rait, A Rosemary Tate, Irene Petersen, Jackie Cassell, 2024.

import sys, csv, re

codes = [{"code":"N093200","system":"readv2"},{"code":"N093600","system":"readv2"},{"code":"N093700","system":"readv2"},{"code":"N093300","system":"readv2"},{"code":"N093400","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('unnamed-inflammatory-arthritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["other-unnamed-inflammatory-arthritis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["other-unnamed-inflammatory-arthritis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["other-unnamed-inflammatory-arthritis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
