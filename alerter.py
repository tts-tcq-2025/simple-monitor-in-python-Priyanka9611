alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Simulate a response: 200 for success, 500 for failure
    return 200 if celcius <= 200 else 500

def increment_failure_count(returnCode):
    global alert_failure_count
    alert_failure_count += 1 if returnCode != 200 else 0

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    increment_failure_count(returnCode)

# Test cases
alert_in_celcius(400.5)  # Should fail (temperature > 200°C)
alert_in_celcius(303.6)  # Should fail (temperature > 200°C)
alert_in_celcius(100.0)  # Should pass (temperature <= 200°C)

print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
