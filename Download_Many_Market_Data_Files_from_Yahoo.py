#########################################################################
# Downlod many market data files from Yahoo Finance website and save 
# the data in a local folder for further data processing/visualization
#########################################################################
import os
import webbrowser
from datetime import date
tdy  = date.today()
yyyy = tdy.year
mm   = tdy.month
dd   = tdy.day

temp = input('Enter the day (today default) = ')
if temp != '' :
    dd = int(temp)
    temp = input('Enter the month (1-12, default this month) = ')
    if temp != '': mm = int(temp)
    temp = input('Enter the year (default this year) = ')
    if temp != '': yyyy = int(temp)
#print ( yyyy, mm, dd)

filename = 'symb.txt'   # Default ticker symbol file name
temp = input('Enter the filename that has a list of ticker symbols? (symb default) = ')
if temp != '' : filename = temp + '.txt'  # If not the default name
#print( filename )

symb = ['']    # init ticker symbol List with symbol_0 = ''
file = open('C:/Users/kuang/Documents/Python/' + filename, 'r')
m=0;
for line in file:
        symb[m]=line.rstrip('\n')    # read a ticker symbol from the opened file 
        symb.append('')              # add a ticker symbol to the list for next one
        m = m + 1                    # update the index
file.close()
nn = m-1                             # number of ticker symbols in the list 

# If a data file of the same name exists, remove it so that
# the same name will be saved every time.
fd = 'C:/Users/Andy/Downloads/'    # A local file folder for storing the data files.
for i in range(nn+1):
    if os.path.exists(fd+symb[i]+'.csv'): os.remove(fd+symb[i]+'.csv')
print(nn+1,symb[nn]) # Print out number of tickers and the last ticker symbol
# d20211020 = 1634774400;
prd2 = date.toordinal(date(1970,1,1))
prd2 = date.toordinal(date(yyyy,mm,dd)) - prd2 + 1
prd1 = ( prd2 - 399 )*24*3600
prd2 = prd2*24*3600

#webbrowser.open("https://finance.yahoo.com/quote/spy/history?p=spy");
url1 = 'https://query1.finance.yahoo.com/v7/finance/download/' 
url2 = ( '?period1=' + str(prd1) + '&period2=' + str(prd2) + 
         '&interval=1d&events=history&includeAdjustedClose=true' )
for i in range(nn+1): webbrowser.open( url1+symb[i]+url2 )
for i in range(nn+1): print( symb[i] )
print( yyyy,'-',mm,'-',dd,'  ', filename + ' Data Saved' )
########################################################################
