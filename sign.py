import hashlib

def sign(mail):
    mail +="-31-eucalyptus"
    return hashlib.new('md4', mail.encode()).hexdigest()

print(sign("bfdanstgnsrtzjmrstzjs@gmail.com")) #use the email that is used to register the account
