import yaml

yaml_file = 'dsets_info_2.yaml'

with open(yaml_file) as f:
    d = yaml.load(f)

# convert to xml
#def print_xml_node(name, content="", attributes={}, indent=0):
#    print(' '*indent + '<{name} {attrs}>')

def xml_value(value):
    try:
        value = str(float(value))
    except:
        value = str(value)

    value = '"%s"' % value
    return value

indent = ' '*2
print('<hard_processes>')
for hard_proc in d['hard_processes']:

    attributes = []
    for k, v in hard_proc.items():
        if k != 'dsets':
            value = xml_value(v)
            attributes.append('='.join((k, value)))
    print(indent + '<hard_process %s>' % ' '.join(attributes))
    for dset in hard_proc['dsets']:
        dset_attr = '<dset dtag={dtag} logic_path={lp}>'.format(
                dtag = xml_value(dset['dtag']),
                lp   = xml_value(dset['logic_path']))
        print(indent*2 + dset_attr)

print('</hard_processes>')
