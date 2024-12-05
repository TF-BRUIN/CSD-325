import json

print("")
print("---------------------------------")
print("")

json_file = open("student.json")
student_data = json.load(json_file)

###########################################

def initial_print():
	printed_lines = 0
	while printed_lines < len(student_data):
		print(
			student_data[printed_lines]["F_Name"] + " , " + student_data[printed_lines]["L_Name"] + " : ID = " + str(student_data[printed_lines]["Student_ID"]) + " , Email = " + student_data[printed_lines]["Email"] 
		)
		printed_lines += 1
	print("This is the original student list.")

###########################################

def modified_print():
	truman_info = {
	"F_Name": "Truman",
	"L_Name": "Forey",
	"Student_ID": 68002,
	"Email": "tforey@gmail.com"
	}
	student_data.append(truman_info)
	printed_lines = 0
	while printed_lines < len(student_data):
		print(
			student_data[printed_lines]["F_Name"] + " , " + student_data[printed_lines]["L_Name"] + " : ID = " + str(student_data[printed_lines]["Student_ID"]) + " , Email = " + student_data[printed_lines]["Email"] 
		)
		printed_lines += 1
	print("This is the modified student list.")

###########################################

def json_dump_func():
	json.dump(student_data, json_file, indent = 4)
	print("JSON file has been successfully updated.")

###########################################

initial_print()
print("")
print("---------------------------------")
print("")
modified_print()
print("")
print("---------------------------------")
print("")
print("Closing and re-opening file for updating process . . .")
print("")
json_file.close()
json_file = open("student.json", "w")
json_dump_func()
print("")
print("---------------------------------")
json_file.close()





