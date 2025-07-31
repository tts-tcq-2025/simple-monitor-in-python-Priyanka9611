# check_limits.py

def is_temperature_within_limit(temperature):
    if temperature < 0 or temperature > 45:
        print("Temperature out of range!")
        return False
    return True

def is_soc_within_limit(soc):
    if soc < 20 or soc > 80:
        print("State of Charge out of range!")
        return False
    return True

def is_charge_rate_within_limit(charge_rate):
    if charge_rate > 0.8:
        print("Charge rate out of range!")
        return False
    return True

def battery_is_ok(temperature, soc, charge_rate):
    return (
        is_temperature_within_limit(temperature) and
        is_soc_within_limit(soc) and
        is_charge_rate_within_limit(charge_rate)
    )
