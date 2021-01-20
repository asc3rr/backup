# backup-system
Backup system, that requires only ssh access

# configuration
Default configuration
```json
{
    "host_data":{
        "address":"<HOST_ADDRESS>",
        "username":"<USERNAME>",
        "port":22
    },
    "remote_path":"<PATH>", # starting at ~/
    "files":[
        "<LIST_OF_FILES>"
    ]
}
```
After you configure, copy that into `config.json` by executing:
```sh
cp config.json.example config.json
```

It should work now.