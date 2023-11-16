def describe_city (city, country= 'South Korea'):
    message = f'{city.title()} is in {country.title()}.'
    print (message)

describe_city('Seoul')
describe_city('Manila', 'Philippines')
describe_city('Incheon')
