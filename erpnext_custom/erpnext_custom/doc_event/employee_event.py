import frappe 

def validate_reason_for_leaving(doc, method):
    if doc.status == "Left" :
        if not doc.reason_for_leaving:
            frappe.throw("Must be enter reason_for_leaving")