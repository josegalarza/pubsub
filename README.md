# Pubsub

A simple pub/sub service over HTTP

## Server

### How to run

```bash
./bin/server.sh
```

### API Endpoints

Method | Endpoint                     | Docs
-------|------------------------------|-----
`GET`  | `/api/pubsub/`               | Get help. Returns: this help message.
`GET`  | `/api/pubsub/ping`           | Check status. Returns: `Pong`
`GET`  | `/api/pubsub/topic/new`      | Create new topic. Returns: `{"id": <id>, "pub_key": <pub_key>, "sub_key": <sub_key>}`
`POST` | `/api/pubsub/topic/pub/<id>` | Post message to topic. Requires header: `{"pub_key": <pub_key>}`
`GET`  | `/api/pubsub/topic/sub/<id>` | Get (and remove) oldest message from topic. Requires header: `{"sub_key": <sub_key>}`.
