// Copyright (c) 2025, Ahmed Fathi and contributors
// For license information, please see license.txt

frappe.query_reports["Human Resource Attendance Report"] = {
	"filters": [
	{'fieldname' : 'employee' , 'label' : 'Employee' , "fieldtype" : "Link", "options" : "Employee"},
	{'fieldname' : 'attendance_date' , 'label' : 'Attendance Date' , "fieldtype" : "Data"}
	]
};
