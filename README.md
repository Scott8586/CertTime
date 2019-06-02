[![Build Status](https://travis-ci.org/Scott8586/CertTime.svg?branch=master)](https://travis-ci.org/Scott8586/CertTime)

## CertTime

Determine time left on a certificate.  This code is a compilation of a couple of things I saw
on the internet and stack overflow for extracting the time left on a certificate.  Here I
added printing the serial number, issued to entity, and take multiple certs on the command line.
Should work with either python2 or python3.

### Example usage:

```
	% i./cert_decode.py testcert.pem 
	Cert A53B46070E3B110D issued to 'www.example.com' is valid for 3649 more days
```

### Notes

The function

```
	ssl._ssl._test_decode_cert()
```

is undocumented and not guarenteed to exist?

