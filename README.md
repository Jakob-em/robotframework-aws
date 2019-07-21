# robotframework-aws

#### Contributors are welcome. This package is at the beginning of development.
 [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)
 ![PyPI](https://img.shields.io/pypi/v/robotframework-aws.svg)

A library of keywords for interacting with AWS services.


#### Instructions

1. Install the package

```
pip install robotframework-aws
```

2. Import Package
  ##### Pass in your AWS Credentials as parameters as shown below.
```
*** Settings ***
Library  AWSLibrary  ${access_key}  ${secret_key}
```

3. Creating a Test Case
   ##### When creating a test case, start with creating a session in AWS for your test.
   ```
   ***Test Case***
   Example Test Case
        Create Session  us-east-1
        Key Should Not Exist  bucky  static/test.html  test.html
        Upload File  bucky  static/test.html  test.html
        Key Should Exist  bucky static/test.html  test.html
        Delete Session  us-east-1
   ```

> ## Session
####  Keywords

 - | `Create Session` | region | profile=optional |
 - | `Delete Session` | region | profile=optional |
 - | `Delete All Sessions` |

 > ### S3 
 ####  Keywords
#####  A key represents the path of the file located in the S3 bucket and Object Path represents the local path of the file on your host.

 - | `Get Bucket` | bucket_name |
 - | `Get Object` | bucket_name | object_path |
 - | `Upload File` | bucket_name | object_path | key |
 - | `Key Should Exist` | bucket_name | object_path | key |
 - | `Key Should Not Exist` | bucket_name | object_path | key |

