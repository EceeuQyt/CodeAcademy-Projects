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

# Add your code here
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


