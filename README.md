# qvidianapi
A Nice Python API to [Qvidian.com](http://Qvidian.com/)

# Install
Install Python [PIP](https://packaging.python.org/installing/).

using pip install the package qvidianapi to your envirenement 
```sh
~$ pip install git+http://gitlab.cisco.com/agabdelb/qvidianapi.git
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
Abdellbar@gmail.com

## License
Please see [LICENSE](https://github.com/Abdellbar/qvidianapi/blob/master/LICENSE).
24 February 2017
