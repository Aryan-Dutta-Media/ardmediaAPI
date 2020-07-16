from csv import writer
from conStrings import db1

dbContact = db1.contact
dbSub = db1.subscribe
dbLand = db1.landing

con = dbContact.find()
lan = dbLand.find()
sub = dbSub.find()

# opening csv files
contact_file = open('./csv_data/contact-data.csv', 'w')
landing_file = open('./csv_data/landing-data.csv', 'w')
subscribe_file = open('./csv_data/subscribe-data.csv', 'w')

# writer objects
contact_writer = writer(contact_file)
landing_writer = writer(landing_file)
subscribe_writer = writer(subscribe_file)

# Counters to write headers
i=0
p=0
q=0


# Writing to contact-data-csv
for doc in con:
    if i == 0:

        header = doc.keys()
        contact_writer.writerow(header)
        i += 1

    contact_writer.writerow(doc.values())
contact_file.close()


# Writing to landing-data-csv
for doc in lan:
    if p == 0:

        header = doc.keys()
        landing_writer.writerow(header)
        p += 1

    landing_writer.writerow(doc.values())
landing_file.close()

# Writing to subscribe-data-csv_data
for doc in sub:
    if q == 0:

        header = doc.keys()
        subscribe_writer.writerow(header)
        q += 1

    subscribe_writer.writerow(doc.values())
subscribe_file.close()
