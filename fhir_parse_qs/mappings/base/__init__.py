__all__=['base_types', 'base_references']

from .appointment import mapping as appt
from .appointment import references as r_appt
from .appointment_response import mapping as apptr
from .appointment_response import references as r_apptr
from .encounter import mapping as enc
from .encounter import references as r_enc
from .location import mapping as loc
from .location import references as r_loc
from .organization import mapping as org
from .organization import references as r_org
from .patient import mapping as patient
from .patient import references as r_patient
from .practitioner import mapping as hp
from .practitioner import references as r_hp
from .schedule import mapping as sch
from .schedule import references as r_sch
from .slot import mapping as slot
from .slot import references as r_slot

base_types = {
        'Appointment': appt,
        'AppointmentResponse': apptr,
        'Encounter': enc,
        'Location': loc,
        'Organization': org,
        'Patient': patient,
        'Practitioner': hp,
        'Schedule': sch,
        'Slot': slot,
        }

base_references = {
        'Appointment': r_appt,
        'AppointmentResponse': r_apptr,
        'Encounter': r_enc,
        'Location': r_loc,
        'Organization': r_org,
        'Patient': r_patient,
        'Practitioner': r_hp,
        'Schedule': r_sch,
        'Slot': r_slot,
        }
