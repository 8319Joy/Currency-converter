#!/usr/bin/env python
# coding: utf-8

# # Currency Converter:

# In[6]:


# Currency Converter without API
def currency_converter(amount, from_currency, to_currency):
    # Define some conversion rates
    conversion_rates = {
        'USD': {'EUR': 0.85, 'GBP': 0.75, 'INR': 73.5, 'JPY': 110.5},
        'EUR': {'USD': 1.18, 'GBP': 0.88, 'INR': 86.5, 'JPY': 130.5},
        'GBP': {'USD': 1.33, 'EUR': 1.14, 'INR': 99.5, 'JPY': 150.5},
        'INR': {'USD': 0.014, 'EUR': 0.012, 'GBP': 0.010, 'JPY': 1.52},
        'JPY': {'USD': 0.0091, 'EUR': 0.0077, 'GBP': 0.0066, 'INR': 0.66}
    }

    # Check if both currencies exist in the conversion rates
    if from_currency in conversion_rates and to_currency in conversion_rates[from_currency]:
        converted_amount = amount * conversion_rates[from_currency][to_currency]
        return f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
    else:
        return "Conversion not available for the selected currencies."

# User input
amount = float(input("Enter the amount: "))
from_currency = input("Enter the currency you want to convert from (USD, EUR, GBP, INR, JPY): ").upper()
to_currency = input("Enter the currency you want to convert to (USD, EUR, GBP, INR, JPY): ").upper()

# Convert and display the result
result = currency_converter(amount, from_currency, to_currency)
print(result)


# In[ ]:




