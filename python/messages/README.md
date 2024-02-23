# Neo4j Setup

## Message

```cypher
CREATE (m:Message {
  content: "Hello, Bob!",
  timestamp: datetime("2022-05-18T12:34:56"),
  platform: "IRC"
})
```
### Reading messages in chronological order

```
MATCH (m:Message)-[:POSTED_IN]->(chan:Channel {name: '#!chases'})
RETURN m.content AS message, datetime(m.timestamp) AS time
ORDER BY time DESC
LIMIT 25
```

### Showing a complete graph

```
MATCH (chan:Channel)-[:POSTED_IN]-(msg:Message)-[:SENT]-(user:User)
OPTIONAL MATCH (msg)-[:MENTIONED]->(mentioned:User)
RETURN chan, user, msg, mentioned
LIMIT 25
```

### Show a more complete graph

```
MATCH (chan:Channel)-[:POSTED_IN]-(msg:Message)-[:SENT]-(user:User)
OPTIONAL MATCH (msg)-[:MENTIONED]->(mentioned:User)

// Order messages in the channel by timestamp (descending)
WITH chan, user, msg, mentioned
ORDER BY msg.timestamp DESC

// Limit results, preserving the relationships
WITH  chan,
      collect({user: user, msg: msg, mentioned: mentioned})[..25] as recentChannelActivity
UNWIND recentChannelActivity as result
RETURN chan, result.user, result.msg, result.mentioned
```

### Delete everything

```
MATCH (n)
DETACH DELETE n
```

## Ontology

```
CREATE CONSTRAINT unique_user_name IF NOT EXISTS FOR (u:User) REQUIRE u.name IS UNIQUE
CREATE CONSTRAINT channel_name_uniqueness ON (c:Channel) ASSERT c.name IS UNIQUE;
CREATE INDEX message_timestamp FOR (m:Message) ON (m.timestamp);
```
