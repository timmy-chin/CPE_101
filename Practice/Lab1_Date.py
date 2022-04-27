from datetime import datetime

now = datetime.now()
print('Day:', now.strftime('%d'))
print('Month:', now.strftime('%m'))
print('Year:', now.strftime('%Y'))
print('Hour:', now.strftime('%H'))
print('Minute:', now.strftime('%M'))
print('Second:', now.strftime('%S'))
