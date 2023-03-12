from datetime import datetime

def convert_date_format(date_string):
    # Parse the input string into a datetime object
    date_obj = datetime.strptime(date_string, '%m/%d/%Y')
    
    # Format the datetime object into the desired output string
    new_date_string = date_obj.strftime('%Y-%m-%d')
    
    return new_date_string
