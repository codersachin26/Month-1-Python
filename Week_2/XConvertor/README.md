
# XConvertor

**XConvertor** is a class, this class take list of dictionary as data and export to Pdf,CSV,Excel,XML and HTML file.




## Examples

 create a object of XConvertor class.
 
```python 
    dummy_data = [{'name':'John','age':23,'hobby':'reading'},{'name':'Tom','age':23,'hobby':'coding'}]

    # create XConvertor object
    x_convertor_obj = XConverter(dummy_data)

```

 To generate csv file, call to_csv() methods
 ```python
    x_convertor_obj.to_csv()

```


 To generate html file, call to_html() methods
 ```python
    x_convertor_obj.to_html()

```


 To generate excel file, call to_excel() methods
 ```python
    x_convertor_obj.to_excel()

```


 To generate pdf file, call to_pdf() methods
 ```python
    x_convertor_obj.to_pdf()

```

 To generate xml file, call to_xml() methods
 ```python
    x_convertor_obj.to_xml()

```


 
