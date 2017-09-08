# Qvidianapi V1
A Nice Python API V1 to [Qvidian.com](http://Qvidian.com/)

# Install
Install Python [PIP](https://packaging.python.org/installing/).

using pip install the package qvidianapi to your environment 
```sh
~$ pip install git+https://github.com/cisco-gve/Qvidian-API-v1.git
```

run basic login to qvidian and chek permissions

```python
import qvidianapi

auth = qvidianapi.QvidianAuthentication()

auth.Connect('your user','your password')

common_client = qvidianapi.Common(auth)

common_client.HasPermissions('AllowPreviewHTML')

print common_client.HasPermissionsResponse

```


## Contacts:
Contributions needed to complete the API
CISCO Global Virtual Engineering


## License
Please see [LICENSE](https://github.com/Abdellbar/qvidianapi/blob/master/LICENSE).
24 February 2017
