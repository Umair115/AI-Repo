a = {}
try:
    with open('data.csv', 'w'):
        print('')
    print('I am After open File')
    if 'Name' in a:
        print(a['Name'])
    else:
        print('Inside Else')
        print('Key does not Exist')

except KeyError:
    print('This key does not exist in this ADT')

except FileNotFoundError as e:
    print(e)
    print('File does not Exist')

except Exception:
    print('This is un-known Exception')
finally:
    print('I am Finally Block!!')
print('Ending')