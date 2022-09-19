
import csv #import csv

def FileOpener(file): #make a file opener procedure
 f = open(file)
 csv_f = csv.reader(f)

 Contact_List = []
 for row in csv_f:
  Contact_List.append(row)

 f.close()

 return Contact_List

print("Hello, please choose a contact list to view:") #create a menu for user to choose an option
print("ENTER 1 FOR CONTACT LIST 1")
print("ENTER 2 FOR CONTACT LIST 2")
print("ENTER 3 FOR CONTACT LIST 3")
selection = input()

if selection == '1': #if selection == 1

 Contact_List_1 = FileOpener('Contact_List_1.csv') #open the first list csv
 next_step = False

#get rid of the word 'Contact' in the subject names in the first list in Contact_List_1
 position = 1
 for subject in Contact_List_1[0]:
  word_destroyer_inator_3000 = subject.endswith('Contact')
  if word_destroyer_inator_3000 == True:
   subject = subject.replace('Contact', '')
   Contact_List_1[0].pop(position)
   Contact_List_1[0].insert(position,subject)
   position = position + 1
   
   
#replace all of the '' items with 'none'
 for student in Contact_List_1:
  for element in student:
   if element == '':
    space_place = student.index(element)
    student.insert(space_place,'none')
    student.pop(space_place + 1)
 #remove the unwanted item in Lidia's list
 Contact_List_1[-1].reverse()
 Contact_List_1[-1].pop(0)
 Contact_List_1[-1].reverse()
 print(Contact_List_1)



#make a list of the kids who do not have a contact
 no_contacts = []
 for student in Contact_List_1:
  none_list = []
  for element in student:
   if element == 'none':
    none_list.append(element)
  if len(none_list) > len(student) - 2:
   no_contacts.append(student[0])
   
 print('')
 print('STUDENTS NOT IN CONTACT:')
 print(no_contacts)
 print('')
#remove the students who are found in the no_contact list from Contact_List_1
 for non_contact_student in no_contacts:
  for student in Contact_List_1:
   if non_contact_student == student[0]:
     Contact_List_1.remove(student)
#make the first list in Contact_List_1 into its own list (subject_list)
 subject_list = Contact_List_1[0]
 subject_list.remove(subject_list[0])     
 Contact_List_1.remove(Contact_List_1[0])
#print the students in contact from Contact_List_1
 print('STUDENTS IN CONTACT:')
 for student in Contact_List_1:
  print(student[0], 'is in contact!')
  student.remove(student[0])
  print("METHODS OF CONTACT:")
  index = 0
  while index < len(student):
   for method in student:
    contact_method = []
    if method != 'none':
     contact_method.append(subject_list[index])
     contact_method.append(method)
     print(contact_method)
    index = index + 1
   
  
   

elif selection == '2': #elif selection == 2
 
 Contact_List_2 = FileOpener('Contact_List_2.csv') #open the second list csv
 Contact_List_2.remove(Contact_List_2[0]) #remove the first list in Contact_List_2

 for student in Contact_List_2: #remove all unwanted spaces ('')
  for string in student:
   if string == '':
    student.remove(string) 
 Contact_List_2[0].remove(Contact_List_2[0][10]) #fix any unwanted bugs
 Contact_List_2.pop(-1)
 print(Contact_List_2)
 
 #subject list = first list in Contact_List_2
 subject_list = Contact_List_2[0]
 Contact_List_2.remove(Contact_List_2[0])
 #remove the first list from Contact_List_2

 #display students who are not in contact
 print('')
 print('STUDENTS WHO ARE NOT IN CONTACT:')
 print('')
 non_contact_list = []
 for student in Contact_List_2:
  if student[1] == 'FALSE':
   non_contact_list.append(student[0])
   Contact_List_2.remove(student)
 print(non_contact_list)
 print('')

#remove the last 2 items in each list from Contact_List_2
 for student in Contact_List_2:
  student.reverse()
  student.pop(0)
  student.pop(1)
  student.reverse() 

#remove any unwanted bugs
 Contact_List_2[5].reverse()
 Contact_List_2[5].pop(0)
 Contact_List_2[5].pop(1)
 Contact_List_2[5].insert(0,'FALSE')
 Contact_List_2[5].insert(1,'FALSE')
 Contact_List_2[5].reverse()

 Contact_List_2[6].reverse()
 Contact_List_2[6].pop(0)
 Contact_List_2[6].pop(1)
 Contact_List_2[6].insert(0,'FALSE')
 Contact_List_2[6].insert(1,'FALSE')
 Contact_List_2[6].reverse()

 Contact_List_2[8].reverse()
 Contact_List_2[8].pop(0)
 Contact_List_2[8].pop(1)
 Contact_List_2[8].insert(0,'FALSE')
 Contact_List_2[8].insert(1,'FALSE')
 Contact_List_2[8].reverse()

#display students in contact
 print('')
 print('STUDENTS IN CONTACT:')
 for student in Contact_List_2:
  print('')
  print(student[0], 'is in contact!')
  student.pop(0) #remove student[0]
  print("METHODS OF CONTACT:")
  index = 0 #index = 0
  while index < len(student): #while index < len(student)
   for method in student: #for method in student
    contact_method = [] #make a new list
    if method != 'FALSE': #if the method != 'FALSE' and != 'Student'
     if subject_list[index] != 'Student':
      contact_method.append(subject_list[index]) #append subject_list[index] to contact_method
      contact_method.append(method) #append the method to contact_method
      print(contact_method)
    index = index + 1 #add 1 to index

elif selection == '3':  #elif selection = 3

 Contact_List_3 = FileOpener('Contact_List_3.csv') #open the third list csv
 
 #remove any unwanted spaces in the data ('')
 remover_counter = 0
 while remover_counter < 5:
  for student in Contact_List_3:
   for element in student:
    if element == '':
     student.remove(element)
  remover_counter = remover_counter + 1
 print('')

#remove the first list in Contact_List_3
 Contact_List_3.pop(0)

#print a list of students not in contact
 print('STUDENTS WHO ARE NOT IN CONTACT:')
 print('')
 not_contacted = []
 for student in Contact_List_3:
  if len(student) == 1:
   not_contacted.append(student)
   Contact_List_3.remove(student)
 print(not_contacted)
 print('')
 print('')

#make a list of students
 student_list = []
 for student in Contact_List_3:
  student_list.append(student[0])
  student.remove(student[0])

#print the students in contact with their contacts
#make an index variable that initially equals 0
#for each student in the list of students
#print the students name and their contact(Contact_List_3[index])
#add 1 to index
 index = 0
 print('STUDENTS WHO ARE IN CONTACT:')
 print('')
 for student in student_list:
  print('STUDENT NAME:',student)
  print('CONTACT:',Contact_List_3[index])
  print('')
  index = index + 1
else: #if user dose not pick 1,2,or 3 inform the user to try again
 print('Sorry that is not an option; please try again...')
 


      


    
    
    
   


  

   
  


  
 
 
   
  

  
 
 
 