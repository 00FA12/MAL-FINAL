import re

def read_properties(path):
    props = {}
    property_regex = re.compile(r'#{0}(.+)[:=]([^\n\r#]+)#?')
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            match = property_regex.match(line)
            if match:
                key = match.group(1).strip()
                value = match.group(2).strip()
                #print('Found property: {}={}'.format(key, value))
                props[key] = value
    return props
