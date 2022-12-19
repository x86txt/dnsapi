# import libraries
import dns.resolver
import dns.reversename

# simple A query
a = dns.resolver.resolve('google.com', 'A')
for val in a:
    print(val)

# simple PTR query
ptr = dns.resolver.resolve_address(a[0].to_text())
for val in ptr:
    print(val)

