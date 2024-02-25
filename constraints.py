constraints = [ # chatGPT helped write these constraints.
    lambda value: value['A'] == value['B']**2 - value['C']**2 if all(k in value for k in ['A', 'B', 'C']) else True,
    lambda value: value['E'] + value['F'] > value['B'] if all(k in value for k in ['E', 'F', 'B']) else True,
    lambda value: value['D'] == value['B']**2 - 3*value['A'] if all(k in value for k in ['D', 'B', 'A']) else True,
    lambda value: (value['B'] - value['C'])**2 == value['E']*value['F']*value['C'] - 1861 if all(k in value for k in ['B', 'C', 'E', 'F']) else True,
    lambda value: value['C'] + value['D'] + value['E'] + value['F'] < 120 if all(k in value for k in ['C', 'D', 'E', 'F']) else True,

    lambda value: (value['G'] + value['I'])**3 == (value['H'] - value['A'] - 1)**2 if all(k in value for k in ['G', 'I', 'H', 'A']) else True,
    lambda value: value['B']*value['E']*value['F'] == value['H']*value['B'] - 200 if all(k in value for k in ['B', 'E', 'F', 'H']) else True,
    lambda value: (value['C'] + value['I'])**2 == value['B']*value['E']*(value['G']+1) if all(k in value for k in ['C', 'I', 'B', 'E', 'G']) else True,
    lambda value: value['G'] + value['I'] < value['E'] if all(k in value for k in ['G', 'I', 'E']) else True,
    lambda value: value['D'] + value['H'] > 180 if all(k in value for k in ['D', 'H']) else True,
    lambda value: value['J'] < value['H'] - value['C'] - value['G'] if all(k in value for k in ['J', 'H', 'C', 'G']) else True,
    lambda value: value['J'] > value['B']*value['G'] + value['D'] + value['E'] + value['G'] if all(k in value for k in ['J', 'B', 'G', 'D', 'E']) else True,

    lambda value: value['K']*value['L']*value['M'] == value['B']*(value['B']+5) if all(k in value for k in ['K', 'L', 'M', 'B']) else True,
    lambda value: value['F']**3 == value['K']**2 * value['M']**2 * 10 + 331 if all(k in value for k in ['F', 'K', 'M']) else True,
    lambda value: value['H']*value['M']**2 == value['J']*value['K'] - 20 if all(k in value for k in ['H', 'M', 'J', 'K']) else True,
    lambda value: value['J'] + value['L'] == value['I']*value['L'] if all(k in value for k in ['J', 'L', 'I']) else True,
    lambda value: value['A'] + value['D'] + value['M'] == value['B']*(value['F']-2) if all(k in value for k in ['A', 'D', 'M', 'B', 'F']) else True,
]