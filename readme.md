# description
Short tools for using in interactive-python

# install 
<pre>sudo wget -v -N raw.githubusercontent.com/jen-soft/tools/master/p.py  "$(python -m site --user-site)/p.py"</pre>

# using 
```python
import p
p.dir( str, True, 7 )
```

<pre>
>>> p.dir( str, True, 7 )
_formatter_field_name_split    decode        format     islower    ljust        rfind         rstrip        swapcase 
_formatter_parser              encode        index      isspace    lower        rindex        split         title    
capitalize                     endswith      isalnum    istitle    lstrip       rjust         splitlines    translate
center                         expandtabs    isalpha    isupper    partition    rpartition    startswith    upper    
count                          find          isdigit    join       replace      rsplit        strip         zfill    
</pre>


<pre>
data = {'id': 1, 'name': 'jen'}
>>> p.json(data)
{
  "id": 1,
  "username": "jen-soft"
}
</pre>


# license 
Licensed under the Apache License, Version 2.0 
<pre>http://www.apache.org/licenses/LICENSE-2.0</pre>

