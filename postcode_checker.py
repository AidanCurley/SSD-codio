import re

postcodes = ['M1 1AA', 'M60 1NW', 'CR2 6XH', 'DN55 1PT', 'W1A 1HQ', 'EC1A 1BB']


my_pattern = r"^[A-Z][A-Z\d]{1,3}\b [\d][A-Z]{2}$"
stack_overflow_pattern = r"^([A-Z][A-HJ-Y]?[\d][A-Z\d]? ?[\d][A-Z]{2}|GIR ?0[A]{2})$"
# https://stackoverflow.com/questions/164979/regex-for-matching-uk-postcodes

for postcode in postcodes:
    if re.match(my_pattern, postcode, re.IGNORECASE):
        print(f'{postcode}: valid')
    else: print(f'{postcode}: not valid')




