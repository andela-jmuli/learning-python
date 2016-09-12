## Python Strings  

Python has a built-in string class 'str' (there's another module named 'string', avoid the confusion). Python strings are 'immutable' which means they cannot be changed after they are created. Thus we construct new strings as we go to represent computed values.  

Characters in a string can be accessed using thr standard[] syntax. Python uses zero-based indexing so if str is 'hello', str[1] is 'e'. Python raises an error if the index is out of bounds for the string. The **len(string)** function returns the length of a string. The [] syntax and len() function actually work on any sequence type -- strings, lists...etc.The **'+'** operator can concatenate two strings.  
```
s = "bruh"
print s[1]				# r
print len(s) 			# 4
print s + ' whats up?'	# bruh whats up?

```

The "print" operator prints out one or more python items followed by a newline. A 'raw' string literal is prefixed by an 'r' and passes all the chars without special treatment of backslashes, so r'x\nx' evaluates to the length-4 string 'x\nx'. A 'u' prefix allows you to write a unicode string literal.  


### String Methods  
* s.lower(), s.upper() - returns the lowercase or uppercase  
* s.strip() - returns a string with whitespace removed from start to end  
* s.isalpha()/ s.isdigit()/ s.isspace() - tests if all the string chars are in the various character classes.  
* s.startswith('other'), s.endswith('other') - tests if string starts or ends with given...  
* s.find('other') - searches for the given other string(not a regex btw) within s, and returns the first index where it begins or -1 if not found  
* s.replace('old', 'new') - returns a string where all occurences of 'old' have been replaced by 'new'  
* s.split('delim') - returns a list of substrings seperated by the given delimeter.  
* s.join(list) - opposite of split(), joins the elements in the given list together using the string as the delimeter. e.g. '---'.join(['aaa','bbb','ccc']) > aaa-bbb-ccc  
* s.swapcase() - returns a copy of the string with uppercase characters converted to lowercase and vice versa