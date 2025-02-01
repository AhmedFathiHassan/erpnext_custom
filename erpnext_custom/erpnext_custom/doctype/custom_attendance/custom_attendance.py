# Copyright (c) 2025, Ahmed Fathi and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document
from datetime import datetime

class customAttendance(Document):
    def validate(self):
        settings = frappe.get_doc("Attendance Setting")

        if self.check_in and self.check_out:
            check_in_time = datetime.strptime(self.check_in, "%H:%M:%S")
            check_out_time = datetime.strptime(self.check_out, "%H:%M:%S")
            self.work_hours = (check_out_time - check_in_time).total_seconds() / 3600  

        if self.check_in and settings.start_time:
            start_time = datetime.strptime(settings.start_time, "%H:%M:%S")
            check_in_time = datetime.strptime(self.check_in, "%H:%M:%S")
            self.late_hours = (check_in_time - start_time).total_seconds() / 3600  

        if self.work_hours <= settings.working_hours_threshold_for_absent:
            self.status = "Absent"
        else:
            self.status = "Present"