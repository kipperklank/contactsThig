
class Contact:
    def __init__(self,
                 name, personalPhone, workPhone,
                 personalEmail, workEmail, address):

        self.name = name
        self.personalEmail = personalEmail
        self.workPhone = workPhone
        self.personalPhone = personalPhone
        self.workEmail = workEmail
        self.address = address


Dave = Contact('Dave',
               '434-444-4322',
               '555-444-3333',
               'DaveTheMan@Dave.com',
               'DaveIsAtWork@DaveWork.com',
               '4324 Yeet Street')

print(Dave.name)
print(Dave.address)
print(Dave.personalPhone)
