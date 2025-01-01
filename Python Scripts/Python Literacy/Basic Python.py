#Python Syntax
#Initial variables
age= 28
sex= 0
smoker= 0
bmi= 26.2
num_of_children= 3


# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("This person's insurance cost is ", insurance_cost, " dollars.")
# Age Factor
age += 4
new_insurance_cost =  250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in cost of insurance after increasing the age by 4 years is", change_in_insurance_cost,"dollars." )
# BMI Factor
age = 28 #age -= 4
bmi += 3.1
new_insurance_cost =  250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost after increasing BMI by 3.1 is", change_in_insurance_cost,"dollars.")
# Male vs. Female Factor
bmi = 26.2 #bmi -+ 3.1
sex = 1
new_insurance_cost =  250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost for a male instead of female is", change_in_insurance_cost,"dollars.")
# Extra Practice
#Children Factor
sex = 0
num_of_children -= 2
new_insurance_cost =  250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost for the amount of children is " + str(change_in_insurance_cost) + " dollars.")
#Smoker factor
num_of_children += 2
smoker = 1
new_insurance_cost =  250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost for a smoker is " + str(change_in_insurance_cost) + " dollars.")




#Python Functions
# Calculate_insurance_cost() function below: 
def calculate_insurance_cost(age,sex,bmi,num_of_children,smoker, name="N/A"):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print('The Estimated insurance cost for '+name+ " is " +str(estimated_cost)+" dollars.")
  return estimated_cost

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(28,0,26.2,3,0, "Maria's")
# Alternativly: maria_insurance_cost = calculate_insurance_cost(age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0, name="Maria's") 
# Estimate Omar's insurance cost 
Omar_insurance_cost = calculate_insurance_cost(35,1,22.2,0,1)
# Alternativly: omar_insurance_cost = calculate_insurance_cost(age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1) 
#Linda
Linda_insurance_cost = calculate_insurance_cost(19,0,18.2,1,0, "Linda's")
#Your Cost
user_insurance_cost = calculate_insurance_cost(26,1,20.1,0,0, "Rashad's")




#Python Control Flow
#Control flow
def analyze_smoker(smoker_status):
  #smoker_status
  if smoker_status==1:
    print('To lower your cost, you should consider quitting smoking.')
  else:
    print('Smoking is not an issue for you.')

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
  estimated_cost = 400*age - 128*sex + 425*num_of_children + 10000*smoker - 2500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  return estimated_cost
 
# Estimate Keanu's and Emma's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, num_of_children = 3, smoker = 1)
emma_insurance_cost = estimate_insurance_cost(name = 'Emma', age = 24, sex = 0, num_of_children = 3, smoker = 0)
# Programmer's Insursance
insurance_cost = estimate_insurance_cost(name = 'J', age = 26, sex = 1, num_of_children = 0, smoker = 0)




#Python List
# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
    return estimated_cost

# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = "Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

akira_insurance_cost = estimate_insurance_cost(name = "Akira", age = 19, sex = 1, bmi = 27.1, num_of_children = 0, smoker = 0)

names = ["Maria", "Rohan", "Valentina", 'Akira']
insurance_costs = [4150.0, 5320.0, 35210.0, 2930.0]

insurance_data = list(zip(names, insurance_costs))
print(insurance_data)

estimate_only = []
estimated_insurance_data = []
estimate_only.append( maria_insurance_cost)
estimate_only.append(rohan_insurance_cost)
estimate_only.append(valentina_insurance_cost)
estimate_only.append(akira_insurance_cost)
estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina",valentina_insurance_cost))
estimated_insurance_data.append(("Akira", akira_insurance_cost))

print("Here is the actual insurance cost data: " + str(insurance_data))
print("Here is the estimated insurance cost data: " + str(estimated_insurance_data))
"""
#print(estimate_only)
#print(insurance_costs)
#insurance_cost_totals = list()
#total_dif = list()
#for actual in insurance_costs:
  #for estimate in estimate_only:
    #total = estimate - actual
    #print(total)
    #insurance_cost_totals.append(int(total))
#total_dif.append(insurance_cost_totals[0])
#total_dif.append(insurance_cost_totals[5])
#total_dif.append(insurance_cost_totals[10])
#total_dif.append(insurance_cost_totals[15])
#print(total_dif)
"""
#Using while loop to find insurance difference instead
print(estimate_only)
print(insurance_costs)
#s_insurance = ' '.join(str(i) for i in insurance_costs)
#print(s_insurance)
total_dif = list() 
i=0
while i < len(insurance_costs):
  for estimate in estimate_only:
    total = estimate - int(insurance_costs[i])
    total_dif.append(total)
    i += 1
    #print(total)

print('Insurance differences:', total_dif)
#Workking with List 
names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]


names.append('Priscilla')
insurance_costs.append(8320.0)
#print(names, insurance_costs)

#Numerical and Alphbetical Order
medical_records_nameorder = list(zip(names, insurance_costs))
print(medical_records_nameorder)
print(sorted(medical_records_nameorder))
medical_records_numorder = list(zip(insurance_costs, names))
print(medical_records_numorder)

#Length of List
num_medical_records = len(medical_records_numorder)
print('There are '+ str(num_medical_records) +' medical records present.')

#Returns first and last records
first_medical_record = medical_records_numorder[0]
last_medical_record = medical_records_numorder[-1]
print("Here is the first medical record and last records without sort:" + str(first_medical_record)+', '+str(last_medical_record))

#medical_records.sort()
  #print("Here are the medical records sorted by insurance cost: " + str(medical_records))
medsort = sorted(medical_records_numorder)
print("Here are the medical records sorted by insurance cost:" , medsort)

cheapest_three = medsort[:3]
print("Here are the three cheapest insurance costs in our medical records: " , cheapest_three)

priciest_three = medsort[-3:]
print("Here are the three most expensive insurance costs in our medical records: " , priciest_three)

middle_five_records = medsort[3:8]
print("Here are the middle five records: ", middle_five_records)

occurrences_paul = names.count('Paul')
print('There are ' + str(occurrences_paul) + ' individuals with the name Paul in our medical records.')





#Python Loops
names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]


total_cost = 0
index = 0
 
while index < len(actual_insurance_costs):
  total_cost += actual_insurance_costs[index]
  index += 1
average_cost = total_cost/len(actual_insurance_costs)
#for actual in actual_insurance_costs:
  #total_cost += actual
  #average_cost = total_cost/len(actual_insurance_costs)
print("Average Insurance Cost: "+ str(average_cost) +" dollars.")

for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  estimate_cost = estimated_insurance_costs[i]
  print("The insurance cost for " +str(name)+ " is " +str(insurance_cost)+ " dollars")
  #Checks if estimate average is above, below, or standard. 
  if estimate_cost > average_cost:
    print("The estimate cost for is above average.")
  elif estimate_cost < average_cost:
    print("The estimate cost for is below average.")
  else:
    print("The estimate cost for is equal to the average.")
  #Checks if insurance average is above, below, or standard. 
  if insurance_cost > average_cost:
    print("The insurance cost for is above average.")
  elif insurance_cost < average_cost:
    print("The insurance cost for is below average.")
  else:
    print("The insurance cost for is equal to the average.")

updated_estimated_costs = [estimate*11/10 for estimate in estimated_insurance_costs] 
print()
print('Regular: ' + str(estimated_insurance_costs))
print('10% Difference: ' + str(updated_estimated_costs))


