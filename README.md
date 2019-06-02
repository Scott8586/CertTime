## CertTime
Determine time left on a certificate.  This code is a compilation of a couple of things I saw
on the internet and stack overflow for extracting the time left on a certificate.  Here I
added printing the serial number, and take multiple certs on the command line.
The function

```
	ssl._ssl._test_decode_cert()
```

is undocumented and not guarenteed to exist?
