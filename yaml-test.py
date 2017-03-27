import yaml

f = open('test.yaml', 'r')
data = yaml.safe_load(f.read())
f.close()

print(data)
print(data['certificates'])

for certificate in data['certificates']:
    print(certificate['name'])
    for host in certificate['hosts']:
        print("\t" + host['hostname'])
