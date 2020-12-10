client = hvac.Client(url='http://0.0.0.0:8200')
login_response = client.auth.userpass.login(
        username="vin",
        password="pass"
    )
client.token = login_response['auth']['client_token']
read_all_secrets = client.secrets.kv.v1.read_secret(
      path='vin/secret',
        mount_point=''
    )
print(read_all_secrets)