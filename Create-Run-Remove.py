#創建文件+內容
def build_creds():
    Output1="creds.json"
    with open(Output1, 'w') as outfile:
            outfile.write('{\n')
            outfile.write(' "type": "service_account",\n')
            outfile.write(' "project_id": "hr-department-282500",\n')
            outfile.write(' "private_key_id": "402999e424a628f561ca9b78044aa98dda78c48d",\n')
            outfile.write(' "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDVmVs1FAV9gqHE\\nzW7KRSeAx1Q3HArE6zTFt45wgKZZxU/VFGmqd8fTi6E0QCk4nECWlGvxJ5K4s7RN\\nBvqWx9GQNB2kla4t/IxHC403NCYZZIkld5XH13zvyNzf4QYxiGukp3bLROmvU6SO\\nmNmCHk44+g7nK+hvv/x77YU2xat3a6ZV3SgTi5HLbxgymdJ6PcNXe/Z2FIUBRmG0\\nIqxSkE25o7HdndFvfAQbR7faTKEDhPojBcb1ETCBj64fvB4SXyq/0I+sc1vmeYUz\\nW9UuPJclT4z0krv08eDhlD8pS846CTVfkuS54929MhxFgLkg09Sq31Z0RPVoCkBj\\nhA77+9LHAgMBAAECggEAQyk1nvJdKZIuCEHp4Iqu+ZRzO+LC1hj4nmRxUpl49MgQ\\nKnkBInsIJ1GDjfjQnT6wJkijyg892HqUqhWULF3G3FcurOXtfwMmHl6Y9+8bPae5\\nYcEApPXyEDkxjelkt6Vj50FKnm5cJecgWj/gQEQEJ3Ekx3YsXxrYKiVMWiT8HY91\\n1shg25DUlBHutgghCGtO/bpenG7J2YF/xu9NHJfXHG0n7VW0hvMNS0Wse5s3RTUE\\nNEy3GAzy1tQdHKk7FwVNUIFg/hHBiz5ybeloSoyFPF7A62/Z8f888k5NzY3YxWJS\\n7HiyXMoztSPlQMRYVzjAiB0kiPawuIp0XqMCLyLkrQKBgQD3CG3IGtgZtyUMWHfM\\nJP06E8eWfPzds1NtosZEe6iXOM5I5c7bvZ6YQsEx825Mr1zF4uG3Li1PcrbYNfdo\\nvVQomvaHET7o3PiU2liQW2VhT7L78Ass1Bpumr9aH1SA+JTDC/oabLZinXXP4xEZ\\njs8A7R8FMHnnlWvkaYu0/XGd0wKBgQDdWj2hYXOhXO2NNbNYVqB4Qa5rgRdTt5Ro\\nqTWk+1yel2QWOqs2qQseApDy/9ySs2C3+HJ8HFY6/iaWW8jsQ8aoWdpoBhdwi9er\\nczWRcDu8XggWEx+dd3RNoKR62LyqiGvtNrxw3D/XsqhyhAVnL8MZQ3LAPZKRv6vC\\nRlGda3W6vQKBgAcZ+u3xt5yloy8DrA32UkFFKEuvNCW7bf6M215En8gZHfUChjvS\\n66g84wjokpcpw2T87LgzX6IVDiSRCJe+OZkhO00OtdxD3fGJhVpBBl0RyXdsoyWa\\nw1fCoxWYKPm8K6qfwYTY8zVKiYR8ZpVxgYnpRycDCb4akYtzbUy6rHV5AoGAI/lV\\niNPIshHjPY7breCuRb0O9sPNIbr1MKlHYZ/EZrXd+0rfpouElgT+v69bjq/+aQfE\\nu2zzirThWpBiMBu3voaT21IaHx1rGJ8ptpBR9QQnNkc3XSUbzr3r3Vc6GlD/kVbS\\n+1igO5L6k1nncuStRX7TuHCJUIyhAnrhKr9bK9UCgYALpjtERFkmUOJ1uUhmY+iP\\nyVVGuBtiQLgTaMgj/62bKYv4URlG+Or3vF3f31zbQ5pXtNQidHs3iM1xlYIUYCQ3\\nWjnzy35ywMEhKRslZZANfmVHa+cMDXIyQMbBm8wZ9ZULpiP26XG3v13ITaIzQskk\\n3MtrOpW2WsVssVZoLmSp/Q==\\n-----END PRIVATE KEY-----\\n",\n')
            outfile.write(' "client_email": "es-728@hr-department-282500.iam.gserviceaccount.com",\n')
            outfile.write(' "client_id": "106031428464360725980",\n')
            outfile.write(' "auth_uri": "https://accounts.google.com/o/oauth2/auth",\n')
            outfile.write(' "token_uri": "https://oauth2.googleapis.com/token",\n')
            outfile.write(' "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",\n')
            outfile.write(' "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/es-728%40hr-department-282500.iam.gserviceaccount.com"\n')
            outfile.write('}')

#移除文件
def remove_creds():
    import os, sys
    os.remove("creds.json")

#執行
build_creds()
remove_creds()
