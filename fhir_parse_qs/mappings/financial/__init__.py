__all__=['financial_types', 'financial_references']

from .account import mapping as ac
from .account import references as r_ac
from .claim import mapping as cl
from .claim import references as r_cl
from .coverage import mapping as cov
from .coverage import references as r_cov
from .payment_notice import mapping as pn
from .payment_notice import references as r_pn

financial_types = {
        'Account': ac,
        'Claim': cl,
        'Coverage': cov,
        'PaymentNotice': pn,
        }

financial_references = {
        'Account': r_ac,
        'Claim': r_cl,
        'Coverage': r_cov,
        'PaymentNotice': r_pn,
        }
