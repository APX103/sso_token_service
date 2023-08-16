# sso_token_service

get openxlab sso token, served with fastapi, unicorn

## Getting started

### Add your config

like this:

``` yaml
# config.yaml
ak: xxxx
sk: xxxx
```

- get `ak`, `sk` from sso website
- must name as `config.yaml`

### Start your service

``` shell
sh build.sh
```

In `build.sh` we can see:

1. build a docker image
2. run a docker container with `-d` 

> And then, we can delete whole dir. (cause all codes are in image(container))

## Get token

``` shell
# wiht curl
curl -X GET 127.0.0.1:10086
```

Get response like this

``` json
{
    "token":"Bearer xxxxxxx"
}
```
