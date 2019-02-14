Python 3.6.5rc1 (v3.6.5rc1:f03c5148cf, Mar 14 2018, 03:12:11) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("""\
lets see if it works:
Multiple Line String-   No of Lines is  = 2""")
lets see if it works:
Multiple Line String-   No of Lines is  = 2
>>> print("""
lets see if it works:
Multiple Line String-   No of Lines is  = 2""")

lets see if it works:
Multiple Line String-   No of Lines is  = 2
>>> # 3 times 'un' followed by 'ium'
>>> 3*'un'+'ium'
'unununium'
>>> 3*"un"+'ium'
'unununium'
>>> 'Py' "thon" "is being studied" ' space is added here but not in the
SyntaxError: EOL while scanning string literal
>>> 'Py' "thon" "is being studied" ' space is added here but not in the previous case'
'Pythonis being studied space is added here but not in the previous case'
>>> 'Py' "thon" "is being studied" '. Space is added here but not in the previous case'
'Pythonis being studied. Space is added here but not in the previous case'
>>> 
