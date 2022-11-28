#question posed by Chandrali Sarkar on LinkedIn (Oct 13th 2022)
# https://www.linkedin.com/feed/update/urn:li:activity:6986196530995060736/
def make_stars(N):
    no_of_rows = list(range(1,N+1)) #no of rows are from 1 to N. we need N+1 because the range function excludes the upper limit. Therefore, taking N+1 as upper limit actually stops the count at N
    for n in no_of_rows:
        if n == 1:
            no_of_stars = [n]
        else:
            no_of_stars = list(range(1,2*n))
            #the number of stars in a given row are the current row number + (current row number -1). But because range is exclusive of the upper limit, we have to include one extra star which means
            #current row number + (current row number -1) + 1. This will simplify down to 2 * current row number of stars.
        stars = ['*' for i in no_of_stars]
        print(''.join(stars))

make_stars(6)
