#File and Array Assortion
with open('checklist.txt','r') as f:
    array=[line.replace('\n','') for line in f]

#Add Item to Array
def add_item_to_checklist(item):
    array.append(item)
    
#Remove Item from Array    
def remove_item_from_checklist(item):
    if item in array:
        array.remove(item)
    else:
        print('This item does not exist')
        
#View the Array        
def view_checklist():
    if len(array)==0:
        print('The checklist is empty')
    else:
        print('\n'.join(array))

#Finish with checklist, insert into file    
def finish_with_checklist():
    new_array = [sel + '\n' for sel in array]
    with open('checklist.txt','w') as f:
        f.writelines(new_array)
    print(new_array)
#Menu
while True:
    try:
        selection=int(input('Main Menu\n1. View Checklist\n2. Add item to Checklist\n3. Remove item from Checklist\n4. Finish with Checklist'))
    except ValueError:
        print('Input Error. Please try a number instead of anything else');continue
    if selection==1:
        view_checklist()
    elif selection==2:
        item=input('Item (A): ')
        add_item_to_checklist(item)
    elif selection==3:
        item=input('Item (R): ')
        remove_item_from_checklist(item)
    else:
        finish_with_checklist()
    
    
