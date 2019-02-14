Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> math.cos(45)
0.5253219888177297
>>> math.sin(45)
0.8509035245341184
>>> math.sin(90)
0.8939966636005579
>>> math.sin(0)
0.0
>>> math.tan(45)
1.6197751905438615
>>> math.tan(42)
2.2913879924374863
>>> math.acos(0)
1.5707963267948966
>>> math.degrees(45)
2578.3100780887044
>>> math.sin(2578.3100780887044)
0.8060754911159176
>>> # see changes in sin(45) and degree of 45 in sine function
>>> math.log(1024, 2)
10.0
>>> math.log(1024, 3)
6.309297535714574
>>> import random
>>> random.choice([1,3,2,6,43,232,223,322])
1
>>> print(random.choice.__doc__)
Choose a random element from a non-empty sequence.
>>> random.choices([1,3,2,6,43,232,223,322])
[1]
>>> print(random.choices.__doc__)
Return a k sized list of population elements chosen with replacement.

        If the relative weights or cumulative weights are not specified,
        the selections are made with equal probability.

        
>>> random.sample([1,3,2,6,43,232,223,322])
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    random.sample([1,3,2,6,43,232,223,322])
TypeError: sample() missing 1 required positional argument: 'k'
>>> random.sample([1,3,2,6,43,232,223,322], 5)
[1, 43, 223, 322, 232]
>>> random.sample([1,3,2,6,43,232,223,322], 5)
[3, 223, 1, 322, 2]
>>> random.sample([1,3,2,6,43,232,223,322], 10)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    random.sample([1,3,2,6,43,232,223,322], 10)
  File "C:\Users\Sinha\AppData\Local\Programs\Python\Python37-32\lib\random.py", line 321, in sample
    raise ValueError("Sample larger than population or is negative")
ValueError: Sample larger than population or is negative
>>> print(random.sample.__doc__)
Chooses k unique random elements from a population sequence or set.

        Returns a new list containing elements from the population while
        leaving the original population unchanged.  The resulting list is
        in selection order so that all sub-slices will also be valid random
        samples.  This allows raffle winners (the sample) to be partitioned
        into grand prize and second place winners (the subslices).

        Members of the population need not be hashable or unique.  If the
        population contains repeats, then each occurrence is a possible
        selection in the sample.

        To choose a sample in a range of integers, use range as an argument.
        This is especially fast and space efficient for sampling from a
        large population:   sample(range(10000000), 60)
        
>>> # used to sample randomly from a large population, k or 5 or 10 is no of
>>> # samples to be displayed/sampled.
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> print(math.__doc__)
This module is always available.  It provides access to the
mathematical functions defined by the C standard.
>>> import statistics
>>> print(statistics.__doc__)

Basic statistics module.

This module provides functions for calculating statistics of data, including
averages, variance, and standard deviation.

Calculating averages
--------------------

==================  =============================================
Function            Description
==================  =============================================
mean                Arithmetic mean (average) of data.
harmonic_mean       Harmonic mean of data.
median              Median (middle value) of data.
median_low          Low median of data.
median_high         High median of data.
median_grouped      Median, or 50th percentile, of grouped data.
mode                Mode (most common value) of data.
==================  =============================================

Calculate the arithmetic mean ("the average") of data:

>>> mean([-1.0, 2.5, 3.25, 5.75])
2.625


Calculate the standard median of discrete data:

>>> median([2, 3, 4, 5])
3.5


Calculate the median, or 50th percentile, of data grouped into class intervals
centred on the data values provided. E.g. if your data points are rounded to
the nearest whole number:

>>> median_grouped([2, 2, 3, 3, 3, 4])  #doctest: +ELLIPSIS
2.8333333333...

This should be interpreted in this way: you have two data points in the class
interval 1.5-2.5, three data points in the class interval 2.5-3.5, and one in
the class interval 3.5-4.5. The median of these data points is 2.8333...


Calculating variability or spread
---------------------------------

==================  =============================================
Function            Description
==================  =============================================
pvariance           Population variance of data.
variance            Sample variance of data.
pstdev              Population standard deviation of data.
stdev               Sample standard deviation of data.
==================  =============================================

Calculate the standard deviation of sample data:

>>> stdev([2.5, 3.25, 5.5, 11.25, 11.75])  #doctest: +ELLIPSIS
4.38961843444...

If you have previously calculated the mean, you can pass it as the optional
second argument to the four "spread" functions to avoid recalculating it:

>>> data = [1, 2, 2, 4, 4, 4, 5, 6]
>>> mu = mean(data)
>>> pvariance(data, mu)
2.5


Exceptions
----------

A single exception is defined: StatisticsError is a subclass of ValueError.


>>> print(statistics.variance.__doc__)
Return the sample variance of data.

    data should be an iterable of Real-valued numbers, with at least two
    values. The optional argument xbar, if given, should be the mean of
    the data. If it is missing or None, the mean is automatically calculated.

    Use this function when your data is a sample from a population. To
    calculate the variance from the entire population, see ``pvariance``.

    Examples:

    >>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
    >>> variance(data)
    1.3720238095238095

    If you have already calculated the mean of your data, you can pass it as
    the optional second argument ``xbar`` to avoid recalculating it:

    >>> m = mean(data)
    >>> variance(data, m)
    1.3720238095238095

    This function does not check that ``xbar`` is actually the mean of
    ``data``. Giving arbitrary values for ``xbar`` may lead to invalid or
    impossible results.

    Decimals and Fractions are supported:

    >>> from decimal import Decimal as D
    >>> variance([D("27.5"), D("30.25"), D("30.25"), D("34.5"), D("41.75")])
    Decimal('31.01875')

    >>> from fractions import Fraction as F
    >>> variance([F(1, 6), F(1, 2), F(5, 3)])
    Fraction(67, 108)

    
>>> print(statistics.StatisticsError.__doc__)
None
>>> print(statistics.harmonic_mean.__doc__)
Return the harmonic mean of data.

    The harmonic mean, sometimes called the subcontrary mean, is the
    reciprocal of the arithmetic mean of the reciprocals of the data,
    and is often appropriate when averaging quantities which are rates
    or ratios, for example speeds. Example:

    Suppose an investor purchases an equal value of shares in each of
    three companies, with P/E (price/earning) ratios of 2.5, 3 and 10.
    What is the average P/E ratio for the investor's portfolio?

    >>> harmonic_mean([2.5, 3, 10])  # For an equal investment portfolio.
    3.6

    Using the arithmetic mean would give an average of about 5.167, which
    is too high.

    If ``data`` is empty, or any element is less than zero,
    ``harmonic_mean`` will raise ``StatisticsError``.
    
>>> from urllib.request import urlopen
>>> with urlopen("https://www.google.com//") as res:
	for line in res:
		line = line.decode('utf-8')
		if 'EST' in line or 'EDT' in line:
			print(line)

			
Traceback (most recent call last):
  File "<pyshell#38>", line 3, in <module>
    line = line.decode('utf-8')
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 5723: invalid start byte
>>> with urlopen("https://www.google.com//") as res:
	for line in res:
		line = line.decode('utf-8')
			print(line)
			
SyntaxError: unexpected indent
>>> with urlopen("https://www.google.com//") as res:
	for line in res:
		line = line.decode('utf-8')
		print(line)

		
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en-IN"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="3QqxO9ceHS3Vpur2RA+GtQ==">(function(){window.google={kEI:'69A7XKucFJmCyAPBoZqoCg',kEXPI:'0,18168,1335579,57,1958,1016,1406,698,527,591,139,326,1123,350,30,695,533,805,95,546,352,2335250,245,32,68,329226,1294,12383,4855,32691,15248,867,12163,6381,3335,2,2,6801,364,1165,6,3411,4242,224,2218,260,5107,575,835,284,2,578,728,2432,58,2,2,2,1297,4323,3390,8,300,1269,774,2115,140,972,195,235,2487,455,1541,5,2,2,1963,1747,1030,283,556,2580,669,1050,464,1344,386,743,268,81,7,3,25,447,16,620,29,989,406,458,1847,93,676,536,696,1456,1,2832,314,876,412,2,554,2165,470,380,194,92,948,101,941,178,38,363,557,573,145,155,499,288,430,42,1294,28,484,47,1081,2368,367,1,801,9,1,247,499,765,431,49,258,2,366,265,217,942,1403,2,4,2,670,46,332,707,738,408,349,167,82,247,879,279,94,274,531,695,104,1,181,1315,5,12,620,198,249,17,87,123,130,45,565,6,38,331,170,42,344,89,346,104,20,492,80,2,83,323,17,10,4,593,2,682,155,131,953,1,1,2,92,942,7,263,88,238,5968489,2554,235,20,5997346,90,2800095,4,1572,549,332,445,1,2,80,1,508,392,583,3,310,1,8,1,2,2132,1,1,1,1,1,414,1,748,141,59,726,3,7,443,3,117,1,2,140,302,22306694',authuser:0,kscs:'c9c918f0_69A7XKucFJmCyAPBoZqoCg',kGL:'IN'};google.kHL='en-IN';})();google.time=function(){return(new Date).getTime()};(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||google.kEI};google.getLEI=function(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b};google.https=function(){return"https:"==window.location.protocol};google.ml=function(){return null};google.log=function(a,b,e,c,g){if(a=google.logUrl(a,b,e,c,g)){b=new Image;var d=google.lc,f=google.li;d[f]=b;b.onerror=b.onload=b.onabort=function(){delete d[f]};google.vel&&google.vel.lu&&google.vel.lu(a);b.src=a;google.li=f+1}};google.logUrl=function(a,b,e,c,g){var d="",f=google.ls||"";e||-1!=b.search("&ei=")||(d="&ei="+google.getEI(c),-1==b.search("&lei=")&&(c=google.getLEI(c))&&(d+="&lei="+c));c="";!e&&google.cshid&&-1==b.search("&cshid=")&&"slh"!=a&&(c="&cshid="+google.cshid);a=e||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+b+d+f+"&zx="+google.time()+c;/^http:/i.test(a)&&google.https()&&(google.ml(Error("a"),!1,{src:a,glmm:1}),a="");return a};}).call(this);(function(){google.y={};google.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.lm=[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};}).call(this);google.f={};</script><script nonce="3QqxO9ceHS3Vpur2RA+GtQ==">var a=window.location,b=a.href.indexOf("#");if(0<=b){var c=a.href.substring(b+1);/(^|&)q=/.test(c)&&-1==c.indexOf("#")&&a.replace("/search?"+c.replace(/(^|&)fp=[^&]*/g,"")+"&cad=h")};</script><style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}

</style><style>body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#36c}.q{color:#00c}.ts td{padding:0}.ts{border-collapse:collapse}em{font-weight:bold;font-style:normal}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}input{font-family:inherit}a.gb1,a.gb2,a.gb3,a.gb4{color:#11c !important}body{background:#fff;color:black}a{color:#11c;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#36c}a:visited{color:#551a8b}a.gb1,a.gb4{text-decoration:underline}a.gb3:hover{text-decoration:none}#ghead a.gb2:hover{color:#fff !important}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#eee;border:solid 1px;border-color:#ccc #999 #999 #ccc;height:30px}.lsbb{display:block}.ftl,#fll a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;border:none;color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#ccc}.lst:focus{outline:none}</style><script nonce="3QqxO9ceHS3Vpur2RA+GtQ=="></script></head><body bgcolor="#fff"><script nonce="3QqxO9ceHS3Vpur2RA+GtQ==">(function(){var src='/images/nav_logo229.png';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new Image().src=src;}

if (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}

}

Traceback (most recent call last):
  File "<pyshell#41>", line 3, in <module>
    line = line.decode('utf-8')
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 5723: invalid start byte
>>> # seems as if it returns code for that webpage.
>>> import smtplib
>>> print(smtplib.__doc__)
SMTP/ESMTP client class.

This should follow RFC 821 (SMTP), RFC 1869 (ESMTP), RFC 2554 (SMTP
Authentication) and RFC 2487 (Secure SMTP over TLS).

Notes:

Please remember, when doing ESMTP, that the names of the SMTP service
extensions are NOT the same thing as the option keywords for the RCPT
and MAIL commands!

Example:

  >>> import smtplib
  >>> s=smtplib.SMTP("localhost")
  >>> print(s.help())
  This is Sendmail version 8.8.4
  Topics:
      HELO    EHLO    MAIL    RCPT    DATA
      RSET    NOOP    QUIT    HELP    VRFY
      EXPN    VERB    ETRN    DSN
  For more info use "HELP <topic>".
  To report bugs in the implementation send email to
      sendmail-bugs@sendmail.org.
  For local information send email to Postmaster at your site.
  End of HELP info
  >>> s.putcmd("vrfy","someone@here")
  >>> s.getreply()
  (250, "Somebody OverHere <somebody@here.my.org>")
  >>> s.quit()

>>> server = smtplib.SMTP("https://mail.google.com/mail/")
Traceback (most recent call last):
  File "C:\Users\Sinha\AppData\Local\Programs\Python\Python37-32\lib\smtplib.py", line 329, in connect
    port = int(port)
ValueError: invalid literal for int() with base 10: '//mail.google.com/mail/'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    server = smtplib.SMTP("https://mail.google.com/mail/")
  File "C:\Users\Sinha\AppData\Local\Programs\Python\Python37-32\lib\smtplib.py", line 251, in __init__
    (code, msg) = self.connect(host, port)
  File "C:\Users\Sinha\AppData\Local\Programs\Python\Python37-32\lib\smtplib.py", line 331, in connect
    raise OSError("nonnumeric port")
OSError: nonnumeric port
>>> server = smtplib.SMTP(host='https://mail.google.com/mail/u/0/#inbox', port=443)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    server = smtplib.SMTP(host='https://mail.google.com/mail/u/0/#inbox', port=443)
  File "C:\Users\Sinha\AppData\Local\Programs\Python\Python37-32\lib\smtplib.py", line 251, in __init__
    (code, msg) = self.connect(host, port)
  File "C:\Users\Sinha\AppData\Local\Programs\Python\Python37-32\lib\smtplib.py", line 336, in connect
    self.sock = self._get_socket(host, port, self.timeout)
  File "C:\Users\Sinha\AppData\Local\Programs\Python\Python37-32\lib\smtplib.py", line 307, in _get_socket
    self.source_address)
  File "C:\Users\Sinha\AppData\Local\Programs\Python\Python37-32\lib\socket.py", line 707, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "C:\Users\Sinha\AppData\Local\Programs\Python\Python37-32\lib\socket.py", line 748, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed
>>> server = smtplib.SMTP('localhost')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    server = smtplib.SMTP('localhost')
  File "C:\Users\Sinha\AppData\Local\Programs\Python\Python37-32\lib\smtplib.py", line 251, in __init__
    (code, msg) = self.connect(host, port)
  File "C:\Users\Sinha\AppData\Local\Programs\Python\Python37-32\lib\smtplib.py", line 336, in connect
    self.sock = self._get_socket(host, port, self.timeout)
  File "C:\Users\Sinha\AppData\Local\Programs\Python\Python37-32\lib\smtplib.py", line 307, in _get_socket
    self.source_address)
  File "C:\Users\Sinha\AppData\Local\Programs\Python\Python37-32\lib\socket.py", line 727, in create_connection
    raise err
  File "C:\Users\Sinha\AppData\Local\Programs\Python\Python37-32\lib\socket.py", line 716, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it
>>> # no mailserver running at localhost so this Connection Refused Error
>>> 
