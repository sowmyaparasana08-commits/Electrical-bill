"""
Progressive Electricity Billing System
-------------------------------------
Calculates monthly household electricity bills using progressive slabs,
fixed charges, a surcharge, and a low-consumption rebate. Compares bills
across months and flags unusually large increases.

Sample academic tariff (edit these constants for your local tariff):
    0-100 units       : Rs. 1.50 per unit
    101-200 units     : Rs. 2.50 per unit
    201-300 units     : Rs. 4.00 per unit
    Above 300 units   : Rs. 6.00 per unit
    Fixed charge      : Rs. 50.00 per month
    Surcharge         : 5% of (energy charge - rebate + fixed charge)
    Rebate            : 10% of energy charge when usage is 100 units or less
    Unusual increase  : Bill increases by more than 30% over previous month
"""

# ------------------------- TARIFF SETTINGS -------------------------

SLAB_1_LIMIT = 100
SLAB_2_LIMIT = 200
SLAB_3_LIMIT = 300

SLAB_1_RATE = 1.50
SLAB_2_RATE = 2.50
SLAB_3_RATE = 4.00
SLAB_4_RATE = 6.00

FIXED_CHARGE = 50.00
SURCHARGE_RATE = 5.0
REBATE_RATE = 10.0
REBATE_USAGE_LIMIT = 100
UNUSUAL_INCREASE_LIMIT = 30.0


def calculate_energy_charge(units):
    """Calculate energy cost progressively across the four slabs."""
    remaining = units
    energy_charge = 0.0
    slab_details = []

    slab_1_units = min(remaining, SLAB_1_LIMIT)
    slab_1_cost = slab_1_units * SLAB_1_RATE
    energy_charge += slab_1_cost
    slab_details.append(("0-100", slab_1_units, SLAB_1_RATE, slab_1_cost))
    remaining -= slab_1_units

    slab_2_units = min(max(remaining, 0), SLAB_2_LIMIT - SLAB_1_LIMIT)
    slab_2_cost = slab_2_units * SLAB_2_RATE
    energy_charge += slab_2_cost
    slab_details.append(("101-200", slab_2_units, SLAB_2_RATE, slab_2_cost))
    remaining -= slab_2_units

    slab_3_units = min(max(remaining, 0), SLAB_3_LIMIT - SLAB_2_LIMIT)
    slab_3_cost = slab_3_units * SLAB_3_RATE
    energy_charge += slab_3_cost
    slab_details.append(("201-300", slab_3_units, SLAB_3_RATE, slab_3_cost))
    remaining -= slab_3_units

    slab_4_units = max(remaining, 0)
    slab_4_cost = slab_4_units * SLAB_4_RATE
    energy_charge += slab_4_cost
    slab_details.append(("Above 300", slab_4_units, SLAB_4_RATE, slab_4_cost))

    return energy_charge, slab_details


def calculate_bill(units):
    """Return a dictionary containing the full bill calculation."""
    energy_charge, slab_details = calculate_energy_charge(units)

    rebate = 0.0
    if units <= REBATE_USAGE_LIMIT:
        rebate = energy_charge * REBATE_RATE / 100

    taxable_amount = energy_charge - rebate + FIXED_CHARGE
    surcharge = taxable_amount * SURCHARGE_RATE / 100
    total_bill = taxable_amount + surcharge

    return {
        "units": units,
        "slab_details": slab_details,
        "energy_charge": energy_charge,
        "fixed_charge": FIXED_CHARGE,
        "rebate": rebate,
        "surcharge": surcharge,
        "total_bill": total_bill
    }


def display_bill(month, bill):
    """Display the itemized bill for one month."""
    print("\n" + "=" * 58)
    print("                 ELECTRICITY BILL")
    print("=" * 58)
