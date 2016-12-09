from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes

# Generate our key
key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=1024,
    backend=default_backend()
)
# Write our key to disk for safe keeping
with open("part2-key.pem", "wb") as f:
    f.write(key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(b"passphrase"),
    ))

# Get key used from root certificate
with open("part1-key.pem", "r") as f:
    rootKey = serialization.load_pem_private_key(f.read(), "passphrase", default_backend())

# Generate a CSR
csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
    # Provide various details about who we are.
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"IE"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Dublin"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"Dublin"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"CoderDojo"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"localhost"),
])).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
    critical=False,
# Sign our certificate with key used in root certificate
).sign(rootKey, hashes.SHA256(), default_backend())
# Write our CSR out to disk.
with open("csr.pem", "wb") as f:
    f.write(csr.public_bytes(serialization.Encoding.PEM))