#question posed by Chandrali Sarkar on LinkedIn (14th Oct)
# https://www.linkedin.com/feed/update/urn:li:activity:6986533881776623616/

string = '200 plus 500 is equal to'

def find_ints(incoming_string):
    ints_in_str = []
    str_as_list = incoming_string.split(" ")
    for s in str_as_list:
        try:

            to_int = int(s)
            ints_in_str.append(to_int)

            print(f'added {s} to int list')
        except:
            print(f"trying to convert {s} to int")
            print("conversion to int failed")
    return sum(ints_in_str)
print(find_ints(string))

