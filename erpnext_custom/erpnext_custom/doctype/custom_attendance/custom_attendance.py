# Copyright (c) 2025, Ahmed Fathi and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document
from datetime import datetime

class customAttendance(Document):
    def validate(self):
        self.get_work_hours()
        self.update_status()

    def get_work_hours(self):
        if self.check_out and self.check_in:
            start_time = datetime.strptime(str(frappe.db.get_single_value('Attendance Setting', 'start_time')), '%H:%M:%S')
            end_time = datetime.strptime(str(frappe.db.get_single_value('Attendance Setting', 'end_time')), '%H:%M:%S')
            late_entry_grace_period = frappe.db.get_single_value('Attendance Setting', 'late_entry_grace_period')  
            early_exit_grace_period = frappe.db.get_single_value('Attendance Setting', 'early_exit_grace_period') 
            check_in = datetime.strptime(self.check_in, '%H:%M:%S')
            check_out = datetime.strptime(self.check_out, '%H:%M:%S')

            late_entry_delta = (check_in - start_time).total_seconds() / 60  
            if late_entry_delta <= late_entry_grace_period:
                late_entry_delta = 0 
            else:
                late_entry_delta = late_entry_delta - late_entry_grace_period  

            early_exit_delta = (end_time - check_out).total_seconds() / 60 
            if early_exit_delta <= early_exit_grace_period:
                early_exit_delta = 0  
            else:
                early_exit_delta = early_exit_delta - early_exit_grace_period 

            self.late_hours = (late_entry_delta + early_exit_delta) / 60


            self.late_hours = int(self.late_hours) 

            self.work_hours = 8 - self.late_hours

            frappe.msgprint(f'Attendance For <b>{self.employee_name}</b> inserted successfully')

        else:
            frappe.throw("Attendance Date, Check In, and Check Out are required")

    def update_status(self):
        grace_period_minutes = 30

        if self.late_hours * 60 > grace_period_minutes:
            self.status = "Absent"
        else:
            self.status = "Present"
