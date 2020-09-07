#stripping_whitespace#
greet = ' - Hello Bob  '
print(greet.lstrip('l'))
print(greet.strip('l'))

' - Hello Bob  '.strip('-')

#removes whitespace at the left of the string#
greet.lstrip()

#removes whitespace at the right of the string#
greet.rstrip()

#removes both beginning and ending whitespace#
greet.strip()
