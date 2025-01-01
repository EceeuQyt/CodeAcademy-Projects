medical_cost = dict()
medical_cost['Marina'] = 6607.0
medical_cost['Vinay'] = 3225.0
medical_cost.update({'Connie':8886.0, 'Isaac':16444.0, 'Valentina':6420.0})

medical_cost['Vinay'] = 3325.0
print(medical_cost)
print()

total_cost = 0
for cost in medical_cost.values():
  total_cost+=cost
average_cost = total_cost/len(medical_cost)
print("Average Insurance Cost:", average_cost)
print()

names = ['Marina', 'Vinay', 'Connie', 'Isaac', 'Valentina']
ages = [27, 24, 43, 35, 52]
zipped_ages = list(zip(names, ages))
names_to_ages = {name:age for name,age in zipped_ages}
print(names_to_ages)

clients_age = 'Marina\'s is {}'.format(names_to_ages.get("Marina"))
print(clients_age)
print()

def indiviuals_medical_database(name, age, sex, BMI, num_of_children, smoker, insurance):
  indiviuals_record = dict()
  indiviuals_record.update({name:{'Age':age, 'Sex':sex, 'BMI':BMI, 'Children':num_of_children, 'Smoker':smoker, 'Insurance Cost': insurance}})
  
  return indiviuals_record, '{} is a {} year old {} {} with a BMI of {} and insurance cost of {}'.format(name, age, sex, smoker, BMI, insurance)
  
 
Marina = indiviuals_medical_database('Marina', 27, 'Female', 31.1, 2, 'Non-smoker', 6607.0)
Vinay = indiviuals_medical_database('Vinay', 24, 'Male', 26.9, 0, 'Non-smoker', 3225.0)
Connie = indiviuals_medical_database('Connie', 43, 'Female', 25.3, 3, 'Non-smoker', 8886.0)
Isaac = indiviuals_medical_database('Isaac', 35, 'Male', 20.6, 4, 'Smoker', 16444.0)
Valentina = indiviuals_medical_database('Valentina', 52, 'Female', 18.7, 1, 'Non-smoker', 6420.0)
print(Marina, Vinay, Connie, Isaac, Valentina)


