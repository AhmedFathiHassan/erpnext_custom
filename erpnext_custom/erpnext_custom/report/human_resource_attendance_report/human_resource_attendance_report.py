# Copyright (c) 2025, Ahmed Fathi and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []
	data = get_all_custom_attendance(filters)
	columns = get_columns()
	return columns, data
	


def get_all_custom_attendance(filters):
	return frappe.db.get_all("custom Attendance", 
						  ['employee_name' , 'department' , 'status' , 'check_in' , 'check_out' , 'work_hours' ,'late_hours','attendance_date'], filters = filters)

def get_columns():
	columns = [
		{'fieldname' : 'employee_name' , 'label' : 'Employee Name' , "fieldtype" : "Data"},
		{'fieldname' : 'department' , 'label' : 'Department' , "fieldtype" : "Link" , "options" : "Department"},
		{'fieldname' : 'status' , 'label' : 'Status' , "fieldtype" : "Select" , "options" : "Present, Absent"},
		{'fieldname' : 'check_in' , 'label' : 'Check In ' , "fieldtype" : "Time"},
		{'fieldname' : 'check_out' , 'label' : 'Check Out ' , "fieldtype" : "Time"},
		{'fieldname' : 'work_hours' , 'label' : 'Work Hours' , "fieldtype" : "Float"},
		{'fieldname' : 'late_hours' , 'label' : 'Late Hours' , "fieldtype" : "Float"},
		{'fieldname' : 'attendance_date' , 'label' : 'Attendance Date' , "fieldtype" : "Data"}
	]
	return columns

